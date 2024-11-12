#1
job_postings = {'Data Scientist': 120, 'Data Analyst': 80, 'Machine Learning Engineer': 50}
print(job_postings['Data Analyst'])

#2
job_postings['AI Specialist'] = 30
print(job_postings)

#3
job_postings = {'Data Scientist': 120, 'Data Analyst': 80, 'Machine Learning Engineer': 50}
job_postings.pop('Machine Learning Engineer')
print(job_postings)

#4
job_postings1 = {'Data Scientist': 120, 'Data Analyst': 80}
job_postings2 = {'Machine Learning Engineer': 50, 'AI Specialist': 30}
job_postings1.update(job_postings2)
print(job_postings1)

#5
"""
Create a nested dictionary job_details where each key is a job role and the value is another dictionary containing 'postings' and 'average_salary'. 
The details for each are: 'Data Scientist' has 120 postings and an average salary of 120000; 
'Data Analyst' has 80 postings and an average salary of 80000; Machine Learning Engineer has 50 postings and average salary of 110000. 
Print the nested dictionary.
"""
job_details = {
    'Data Scientist': {
        'postings': 120,
        'average salary': 120_000
    },
    'Data Analyst': {
        'postings': 80,
        'average salary': 80_000
    },
    'Machine Learning Engineer':{
        'postings': 50,
        'average salary': 110_000
    }
}
print(job_details)