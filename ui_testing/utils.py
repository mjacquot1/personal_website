# Helper functions and classes

class ResumeLineHandler():
    def __init__(self, resume_experience_lines={}):

        # If there is no 'lines', or it equals an empty array, set to none
        if ('lines' in resume_experience_lines.keys()):
            self.lines = resume_experience_lines['lines'] if (len(resume_experience_lines['lines']) > 0) else None
        else:
            self.lines = None

    def return_lines_dict(self):
        if self.lines == None:
            return
        
        sorted_experience_lines = {
            'summary':[],
            'detail':[]
        }

        for line in self.lines:
            if line['is_summary']:
                sorted_experience_lines['summary'].append(line)
            else:
                sorted_experience_lines['detail'].append(line)
        
        return sorted_experience_lines