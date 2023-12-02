# Helper functions and classes
from django.utils.html import format_html
import json

from jsonschema import validate

class ResumeLineHandler():
    resume_block_default_schema={
        'lines':        []
    }

    resume_line_default_schema={
        'text':         '',
        'skills':       [],
        'sub_text':     [],
        'is_summary':   False,
        'anchor_tag':   [],
    }

    resume_subtext_default_schema={
        'text':         '',
        'skills':       [],
        'anchor_tag':   [],
    }

    resume_anchor_tag_default_schema={
        "type": "object",
        "properties": {
            'url':                  '',
            'string_to_replace':    '',
            'replacement_string':   '',
        }, 
    }

    resume_block_validation_schema={
    "type": "object",
        "properties": {
            'lines':         {'type': 'array'},
        }, 
    }

    resume_line_validation_schema={
        "type": "object",
        "properties": {
            'text':         {'type': 'string'},
            'skills':       {'type': 'array'},
            'sub_text':     {'type': 'array'},
            'is_summary':   {'type': 'boolean'},
            'anchor_tag':   {'type': 'array'},
        }, 
    }

    resume_subtext_validation_schema={
        "type": "object",
        "properties": {
            'text':         {'type': 'string'},
            'skills':       {'type': 'array'},
            'anchor_tag':   {'type': 'array'},
        }, 
    }

    resume_anchor_tag_validation_schema={
        "type": "object",
        "properties": {
            'url':                  {'type': 'string'},
            'string_to_replace':    {'type': 'string'},
            'replacement_string':   {'type': 'string'},
        }, 
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

    def return_formated_anchor_tag_text(self, text='', url='', string_to_replace='', replacement_string=''):
        # format_html() allows it to render the anchor tag
        return format_html(text.replace(
                string_to_replace,
                f'<a href="{url}" target="_blank" rel="noopener noreferrer">{replacement_string}</a>'
            ))


    def return_aggregate_skills_set(self):
        if self.lines == None: return

        skills_set = set()

        for line in self.lines:
            for skill in line['skills']:
                skills_set.add(skill.upper())

        # Return a set of all unique skills in the resume experience lines
        return skills_set
    
    def validate_lines(self):
        if self.lines == None: return
        
        # # Make sure there are line objects
        # invalid_lines_object= self.__validate_schema(self.lines, self.resume_block_validation_schema)
        # if invalid_lines_object: 
        #     return "top Level " + self.__validate_error_return_message(invalid_lines_object)

        # Go through each line to validate it
        for count, line in enumerate(self.lines):
            invalid_line_object = self.__validate_schema(line, self.resume_line_validation_schema)
            if invalid_line_object: 
                return self.__validate_error_return_message(invalid_line_object,
                                                            count)

            # Go through each anchor tag nested in the line to validate it.
            for anchor_tag_count, anchor_tag in enumerate(line['anchor_tags']):
                invalid_anchor_tag = self.__validate_schema(anchor_tag, self.resume_anchor_tag_validation_schema)
                if invalid_anchor_tag:
                    return self.__validate_error_return_message(invalid_anchor_tag,
                                                                count,
                                                                None,
                                                                anchor_tag_count)

            # Repeat for sub_text lines
            for sub_text_count, sub_text in enumerate(line['sub_text']):
                invalid_sub_text = self.__validate_schema(sub_text, self.resume_subtext_validation_schema)
                if invalid_sub_text: 
                    return self.__validate_error_return_message(invalid_sub_text,
                                                                count,
                                                                sub_text_count,
                                                                None)

                for anchor_tag_count, anchor_tag in enumerate(sub_text['anchor_tags']):
                    invalid_anchor_tag = self.__validate_schema(anchor_tag, self.resume_anchor_tag_validation_schema)
                    if invalid_anchor_tag:
                        return self.__validate_error_return_message(invalid_anchor_tag,
                                                                    count,
                                                                    sub_text_count,
                                                                    anchor_tag_count)
            
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

    def __validate_schema(self, object_to_validate, validation_schema):
        try:
            validate(object_to_validate, validation_schema)
        except Exception as e:
            return e
        
        return None
        
    def __insert_anchor_tags_to_text(self, line_dict):
        if 'anchor_tags' not in line_dict.keys(): return

        for anchor_tag in line_dict['anchor_tags']:
            line_dict['text'] = self.return_formated_anchor_tag_text(line_dict['text'],anchor_tag["url"],anchor_tag['string_to_replace'],anchor_tag["replacement_string"])
        
    def __add_object_key(self, passed_object, key=[], default_value=None):
        if key not in passed_object.keys(): 
            passed_object[key] = default_value
            return f'Added the following key: "{key}"\nWith value: {None}.\nReturning object:{passed_object}'
        else:
            return f'Passed object already has key: "{key}".'

    def __remove_object_key(self, passed_object, key):
        if key in passed_object.keys(): 
            del passed_object[key]
            return f'Removed the following key: "{key}".\nReturning object:{passed_object}'
        else:
            return f'Passed object missing key: "{key}".'