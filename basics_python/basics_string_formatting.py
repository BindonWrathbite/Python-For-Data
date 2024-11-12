#1
job_title = 'Data Scientist'
print(f'Job Title: {job_title}')

#2
position = 'Data Scientist'
company = 'DataWiz Inc'
print(f'{position} at {company}')

#3
role = 'Data Analyst'
skill = 'Python'
result = f'Role: {role}, Skill: {skill}'
print(result)
#or
new_result = 'Role: {}, Skill: {}'.format(role, skill)
print(new_result)

#4
role = 'Data Engineer'
skill = 'SQL'
result = 'Role: %s, Skill: %s' % (role, skill)
print(result)