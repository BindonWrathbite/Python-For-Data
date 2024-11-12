#1
salaries = [95000, 120000, 105000, 90000, 130000]
avg = lambda x: sum(x) / len(x)
average = avg(salaries)
print(int(average))

#2
print('-' * 80)
job_titles = ['Data Scientist', 'Data Engineer', 'Machine Learning Engineer', 'Data Analyst']
hasData = lambda title: 'Data' in title
data_jobs = list(filter(hasData, job_titles))
print(data_jobs)

#3 Create a lambda function to filter remote job postings that require Python skills from a list of job postings
print('-' * 80)
job_postings = [
    {'title': 'Data Scientist', 'skills': ['Python', 'SQL'], 'remote': True},
    {'title': 'Data Analyst', 'skills': ['Excel', 'SQL'], 'remote': False},
    {'title': 'Machine Learning Engineer', 'skills': ['Python', 'TensorFlow'], 'remote': True},
    {'title': 'Software Developer', 'skills': ['Java', 'C++'], 'remote': True}
]

filtered_jobs = lambda posting: 'Python' in posting['skills'] and posting['remote'] 
remote_jobs = list(filter(filtered_jobs, job_postings))
print(remote_jobs)