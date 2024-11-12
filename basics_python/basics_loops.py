#1
print('1', '-'*80)
job_titles = ['Data Scientist', 'Data Analyst', 'Machine Learning Engineer']
for job in job_titles:
    print(job)

#2
print('2', '-'*80)
job_postings = [5, 10, 15, 20, 25]
total_postings = 0
i = 0
while i < len(job_postings):
    total_postings += job_postings[i]
    i += 1
print(total_postings)

#3
print('3', '-'*80)
job_titles = ['Data Scientist', 'Data Analyst', 'Machine Learning Engineer']
for index, title in enumerate(job_titles):
    print(f'{index}: {title}')

#4
print('4', '-'*80)
job_titles = ['Data Scientist', 'Data Analyst', 'Machine Learning Engineer', 'Software Engineer']
i = 0
first_titles = None
while i < len(job_titles):
    if 'Engineer' in job_titles[i]:
        first_titles = job_titles[i]
        break
    i += 1
print(first_titles)

#5
print('5', '-'*80)
positions_skills = {
    'Data Scientist': ['Python', 'R'],
    'Data Analyst': ['SQL', 'Excel'],
    'Machine Learning Engineer': ['Python', 'TensorFlow']
}

for job, skills in positions_skills.items():
    print(f'The role of {job} requires proficiency in: ', end=' ')
    for skill in skills:
        print(f'{skill}', end=' ')
    print()
