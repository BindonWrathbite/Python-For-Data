#1
unique_job_titles = {'Data Scientist', 'Data Analyst', 'Machine Learning Engineer'}
unique_job_titles.add('AI Specialist')
print(unique_job_titles)

#2
unique_job_titles = {'Data Scientist', 'Data Analyst', 'Machine Learning Engineer'}
unique_job_titles.remove('Data Analyst')
print(unique_job_titles)

#3
job_locations = ['New York', 'San Francisco', 'New York', 'Austin', 'San Francisco']
unique_job_locations = set(job_locations)
print(unique_job_locations)

#4
skills_set1 = {'Python', 'SQL', 'Tableau'}
skills_set2 = {'R', 'SQL', 'Machine Learning'}
skills_3 = skills_set1.union(skills_set2)
print(skills_3)