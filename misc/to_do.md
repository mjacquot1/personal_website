## To Do

1. - [x] Rename CSS Classes
2. - [x] Strip unused CSS and Javascript
3. - [x] Turn resume dynamic
4. - [x] Turn skills dynamic
5. - [x] Make "resume" app
6. Determine what static files to load
7. - [X] Set cache for production
8. Pytest files for email
9. Pytest files for dynamic elements
10. Use Https to secure site
11. - [X] See how to serve media in production
12. - [X] Find a way to secure /media/
13. Why do some recreation photos not enlarge?
14. - [x] Buy Iportfolio template
15. - [x] Add filters to skills
16. - [x] Cache elements
17. Test traffic volume capabilities
18. - [x] Determine webpage size in memory
19. Deploy to AWS with terraform
20. - [x] Add clear Github link
21. - [x] Make emailing asynchronous
22. - [x] Make a way to replace a words  with an anchor tags. 
23. - [x] Create resume_lines_skill function to restrict what is saved in json
24. - [x] Make javascript highlight relevant experience
24. - [] Clean up text
25. - [x] Add functions to change display_order in database
26. Add boot instructions to readme
27. Add views to flowchart
28. - [x] Rename database tables for Resume
29. - Remove mutable global from javascript
30. - [x] Get flower and redis UI working
31. - [] Add redis-commander variables to prod env file
32. Add variable for css colors
33. Have pytest.ini vary between dev and production 
34. - [X] Redirect head to resume
35. - [] Limit nginx requests

## Testing
1. - [] enforce diplay order: Old_display > new_display, New_Display > old_display, old_display == new_display, new_display > record count, old_display > record count, new_display is negative, old_display is negative, old_display is not integer, new_dsiplay is not integer, old_display is none, new_display is none, both are none, no passed_object, correct pased_object, incorrect passed_object, no current records
2. - [] ResumeLineHander: Passed json not proper (no 'lines', not an array), Double check schemas (resume_line_default_schema, resume_subtext_default_schema, resume_anchor_tag_default_schema), return_formatted_lines_dict (no lines, return 'summary' array, return 'detail' array, 'is summary' exists, 'is summary' goes to summary, the rest goes to 'detail), __insert_anchor_tags_to_text(check for line_dict type,check for 'anchor tags' array, return properly formatted anchor text, ensure "return_formated_anchor_tag_text" is called), return_formated_anchor_tag_text (ensure type of (text, url, string_to_replace, and replacement_string), ensure return type is formatted html, double check anchor tag is in text), return_aggregate_skills_set ( check for self.lines array, check for "skills", check set of skills, make sure all skills are .upper), enforce_schema (check for self.lines, check for error message return, ensure "__add_and_validate_schema_fields" is called, ensure "__has_key" is called and ensure "__validate_schema_field" is called for the following (line array, anchor_tags, sub_text, sub_text anchor_tags), ensure error message is made for (line array, anchor_tags, sub_text, sub_text anchor_tags),  call "__add_and_validate_schema_fields" for (line array elements, anchor_tags elements, sub_text elements, sub_text anchor_tags elements), test missing tags ('anchor_tags','sub_text','sub text anchor_tags')), test __has_key (incorrect passed_object, incorrect key), __add_and_validate_schema_fields (check passed_object type, check passed_schema as strign array, Make sure "__has_key" is called for each element, make sure "__validate_schema_field" is called with proper arguments, add to "invalid_fields_flags" for errors, add blank schema fields to objects missing fields, return error if errors exist, return none if no errors), __validate_schema_field: ()
3. - []
4. - []
5. - []
6. - []
7. - []
8. - []
9. - []
10. - []

