# Helper functions and classes
from django.utils.html import format_html
from django.db.models import F
import json

def enforce_display_order(passed_object, old_display_order, new_display_order):
        
        # If no display order is passed this cannot function
        if new_display_order == None and old_display_order == None:
            return

        
        object_model = type(passed_object)
        lower_bound, upper_bound = None, None
        increment = 1

        record_count = object_model.objects.all().count()

        # If the new display order is None, this record is being deleted.
        # Set the new display order to be more than the count of records.
        if new_display_order == None: new_display_order = record_count +1

        # If the order is more than count of records, set the count to be last
        # Since count starts at 0, it needs to be (count - 1)
        if new_display_order >= record_count: new_display_order = (record_count - 1) if passed_object.pk else record_count
        

        # If there is no primary key, then this object is brand new
        if passed_object.pk:
            # Display order moves closer to 0: All order between previous value and up to the new value must be incremented to fill the gap
            if old_display_order> new_display_order: lower_bound, upper_bound = new_display_order, old_display_order
                
            # Display order moved further away from 0: All order between previous value and up to the new value must be decremented to fill gap
            if old_display_order < new_display_order: lower_bound, upper_bound, increment = old_display_order, new_display_order, -1
            
        else:
            # Increment all display orders equal or more by 1 to display after
            if new_display_order < record_count: lower_bound, upper_bound = new_display_order, (record_count+1)
        
        # Since value can be '0', we need to check explicitly if it equals None
        if lower_bound != None and upper_bound != None:
            object_model.objects.filter(display_order__gte=lower_bound, display_order__lte=upper_bound).update(display_order=F('display_order')+increment)

    


class ResumeLineHandler():
    resume_line_default_schema={
        'text':         '',
        'skills':       [],
        'sub_text':     [],
        'is_summary':   False,
        'anchor_tags':   [],
    }

    resume_subtext_default_schema={
        'text':         '',
        'skills':       [],
        'anchor_tags':   [],
    }

    resume_anchor_tag_default_schema={
        'url':                  '',
        'string_to_replace':    '',
        'replacement_string':   '',
    }

    def __init__(self, resume_experience_lines={}):

        # If there is no 'lines', or it equals an empty array, set to none
        if ('lines' in resume_experience_lines.keys()):
            self.lines = resume_experience_lines['lines'] if (len(resume_experience_lines['lines']) > 0) else None
        else:
            self.lines = None

    def return_formatted_lines_dict(self):
        if self.lines == None: return
        
        sorted_experience_lines = {
            'summary':[],
            'detail':[]
        }

        for line in self.lines:
            # Add anchor tags to text
            self.__insert_anchor_tags_to_text(line)

            # Add anchor tags to subtext
            for sub_text in line['sub_text']:
                self.__insert_anchor_tags_to_text(sub_text)

            if line['is_summary']:
                sorted_experience_lines['summary'].append(line)
            else:
                sorted_experience_lines['detail'].append(line)
        
        return sorted_experience_lines

    def return_aggregate_skills_set(self):
        if self.lines == None: return

        skills_set = set()

        for line in self.lines:
            for skill in line['skills']:
                skills_set.add(skill.upper())

        # Return a set of all unique skills in the resume experience lines
        return skills_set
 
    def enforce_schema(self):
        if self.lines == None: return
        error_message = ""

        for count, line in enumerate(self.lines):
            invalid_line_fields = self.__add_and_validate_schema_fields(line, self.resume_line_default_schema)
            if invalid_line_fields: error_message += f'Line "{count}" has the following errors: {invalid_line_fields}'

            if self.__has_key(line, 'anchor_tags') and self.__validate_schema_field(line, 'anchor_tags', self.resume_line_default_schema) == None:
                for anchor_tag_count, anchor_tag in enumerate(line['anchor_tags']):
                    invalid_anchor_tag_fields = self.__add_and_validate_schema_fields(anchor_tag, self.resume_anchor_tag_default_schema)
                    if invalid_anchor_tag_fields: error_message += f'Line ({count}) anchor tag ({anchor_tag_count}) has the following errors: {invalid_anchor_tag_fields}'

            if self.__has_key(line, 'sub_text') and self.__validate_schema_field(line, 'sub_text', self.resume_line_default_schema) == None:
                for sub_text_count, sub_text in enumerate(line['sub_text']):
                    invalid_sub_text_fields = self.__add_and_validate_schema_fields(sub_text, self.resume_subtext_default_schema)
                    if invalid_sub_text_fields: error_message += f'Line ({count}) subjext ({sub_text_count}) has the following errors: {invalid_sub_text_fields}'

                    if self.__has_key(sub_text, 'anchor_tags') and self.__validate_schema_field(sub_text, 'anchor_tags', self.resume_subtext_default_schema)  == None:
                        for anchor_tag_count, anchor_tag in enumerate(sub_text['anchor_tags']):
                            invalid_sub_text_anchor_tag_fields = self.__add_and_validate_schema_fields(anchor_tag, self.resume_anchor_tag_default_schema)
                            if invalid_sub_text_anchor_tag_fields: 
                                error_message += f'Line ({count}) subjext ({sub_text_count}) anchor tag ({anchor_tag_count}) has the following errors: {invalid_sub_text_anchor_tag_fields}'

        if len(error_message) > 0: return error_message
        return None

    def __has_key(self, passed_object, key):
        try:
            test = passed_object[key]
        except:
            return False
        return True
            
    def __validate_error_return_message(self, error, line_count=None, sub_text_count=None, anchor_tag_count=None):
        error_message = f'Invalid Resume Line: "{error.message}"'
        for_field = f'for field {str(error.absolute_path).replace("deque([","").replace("])","").replace(", ", "/")}.'

        line_number         = ''
        sub_text_number     = ''
        anchor_tag_number   = ''

        if line_count:          line_number         = f'at line {line_count}'
        if sub_text_count:      sub_text_number     = f'for sub text {sub_text_count}'
        if anchor_tag_count:    anchor_tag_number   = f'for anchor tag {anchor_tag_count}'

        return " ".join((error_message, line_number, sub_text_number, anchor_tag_number, for_field))

    def __insert_anchor_tags_to_text(self, line_dict):
        if 'anchor_tags' not in line_dict.keys(): return

        for anchor_tag in line_dict['anchor_tags']:
            line_dict['text'] = self.return_formated_anchor_tag_text(line_dict['text'],anchor_tag["url"],anchor_tag['string_to_replace'],anchor_tag["replacement_string"])
        
    def return_formated_anchor_tag_text(self, text='', url='', string_to_replace='', replacement_string=''):
        # format_html() allows it to render the anchor tag
        return format_html(text.replace(
                string_to_replace,
                f'<a href="{url}" target="_blank" rel="noopener noreferrer">{replacement_string}</a>'
            ))
    
    
    def __add_and_validate_schema_fields(self, passed_object, passed_schema):
        invalid_fields_flags = []

        for schema_key in passed_schema.keys():
            # If the schema key is not in the object keys, add it. 
            # If it is, validate the type.
            if self.__has_key(passed_object, schema_key):
                invalid_field =  self.__validate_schema_field(passed_object,schema_key, passed_schema)
                if invalid_field: invalid_fields_flags.append(invalid_field)

            else:
                passed_object[schema_key] = passed_schema[schema_key]

        if len(invalid_fields_flags) > 0: return invalid_fields_flags
        return None
    
    def __validate_schema_field(self, passed_object, passed_key, passed_schema):
        # Assume the key is present
        if type(passed_object[passed_key]) != type(passed_schema[passed_key]): 
            return f'Field "{passed_key}" must be of type "{type(passed_schema[passed_key])}"'

        return None
        
    def __add_object_key(self, passed_object, key, default_value=None):
        if self.__has_key(passed_object, key) == False:
            passed_object[key] = default_value
            return f'Added the following key: "{key}" with value: {None}.\nReturning object:{passed_object}'
        else:
            return f'Passed object already has key: "{key}".'

    def __remove_object_key(self, passed_object, key):
        if self.__has_key(passed_object, key):
            del passed_object[key]
            return f'Removed the following key: "{key}".\nReturning object:{passed_object}'
        else:
            return f'Passed object missing key: "{key}".'