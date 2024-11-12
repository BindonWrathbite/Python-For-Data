#1
job_roles = ('Data Scientist', 'Data Analyst', 'Machine Learning Engineer')
print(job_roles[1])

#2
extended_job_roles = job_roles + ('AI Specialist',)
print(extended_job_roles)

#3
job_roles = ('Data Scientist', 'Data Analyst', 'Machine Learning Engineer')
job_roles_list = list(job_roles)
job_roles_list.remove('Data Analyst')
updated_job_roles = tuple(job_roles_list)
print(updated_job_roles)

#4
job_postings = (120, 80, 50)
data_scientist_postings, data_analyst_postings, ml_engineer_postings = job_postings
print(data_scientist_postings, data_analyst_postings, ml_engineer_postings)

#5
job_details = (('Data Scientist', 120), ('Data Analyst', 80), ('Machine Learning Engineer', 50))
print(job_details[2][1])