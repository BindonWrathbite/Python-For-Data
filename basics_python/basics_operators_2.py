#1
job_title1 = 'Data Engineer'
job_title2 = 'Data Scientist'
print(job_title1 != job_title2) #or
print(f"2nd way: {job_title1 is not job_title2}")

#2
job_locations = ['New York', 'San Francisco', 'Austin']
print('New York' in job_locations)

#3
job_title = 'Data Analyst'
job_description = 'Data Scientist at Tech Corp'
print(job_title not in job_description)

#4
job_titles = ['Data Scientist', 'Data Analyst', 'Machine Learning Engineer']
print(('Data Scientist' in job_titles) and ('Machine Learning Engineer' in job_titles))

#5
salary1 = 100000
salary2 = 50000
print(salary1 | salary2)