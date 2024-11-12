#1
python_experience = 3
skill_level = None
if python_experience < 2:
    skill_level = 'Beginner'
else:
    skill_level = 'Intermediate'
print(skill_level)

#2
tools_known = 3
skill_level = None
if 0 <= tools_known <= 1: # tools_known <= 1
    skill_level = 'Beginner'
elif 2 <= tools_known <= 4: # tools_known <= 4
    skill_level = 'Intermediate'
else:
    skill_level = 'Advanced'
print(skill_level)

#3
job_experience = 4
sql_experience = 2
job_title = None

if job_experience < 2:
    job_title = 'Junior Analyst'
elif 2 <= job_experience <= 5 and sql_experience == 1:
    job_title = 'Intermediate Analyst'
elif 2 <= job_experience <= 5 and sql_experience == 2:
    job_title = 'Senior Analyst'
elif job_experience > 5 and sql_experience >= 3:
    job_title = 'Lead Analyst'
else:
    job_title = 'Data Analyst'
print(job_title)