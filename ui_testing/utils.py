# Helper functions and classes
from django.utils.html import format_html

class ResumeLineHandler():
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
            self.insert_anchor_tags_to_text(line)

            # Add anchor tags to subtext
            for sub_text in line['sub_text']:
                self.insert_anchor_tags_to_text(sub_text)

            if line['is_summary']:
                sorted_experience_lines['summary'].append(line)
            else:
                sorted_experience_lines['detail'].append(line)
        
        return sorted_experience_lines

    def insert_anchor_tags_to_text(self, line_dict):
        if 'anchor_tags' not in line_dict.keys(): return

        for anchor_tag in line_dict['anchor_tags']:
            line_dict['text'] = self.return_formated_anchor_tag_text(line_dict['text'],anchor_tag["url"],anchor_tag['string_to_replace'],anchor_tag["replacement_string"])
        
    def return_formated_anchor_tag_text(self, text='', url='', string_to_replace='', replacement_string=''):
        return format_html(text.replace(
                string_to_replace,
                f'<a href="{url}" target="_blank" rel="noopener noreferrer">{replacement_string}</a>'
            ))


    def return_aggregate_skills_set(self):
        if self.lines == None: return

        skills_set = set()

        for line in self.lines:
            for skill in line['skills']:
                skills_set.add(skill)

        # Return a set of all unique skills in the resume experience lines
        return skills_set
    
    