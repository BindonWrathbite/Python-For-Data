#1
print('-'*80)
salaries_usd = [100000, 120000, 80000, 90000]
salaries_eu = [x * 0.85 for x in salaries_usd]
print(salaries_eu)

#2
print('-'*80)
job_experience = {'Data Scientist': 3, 'Data Analyst': 1, 'Machine Learning Specialist': 4, 'Data Engineer': 2}
print([x for x in job_experience.items()])
two_years_exp = [job for job, exp in job_experience.items() if exp > 2]
print(two_years_exp)

#3
print('-'*80)
job_salary_dicts = [{'job_title': 'Data Scientist', 'salary': 100000}, 
                    {'job_title': 'Data Analyst', 'salary': 120000}, 
                    {'job_title': 'Data Engineer', 'salary': 80000}, 
                    {'job_title': 'Machine Learning Engineer', 'salary': 90000}]

high_pay_jobs = [job['job_title'] for job in job_salary_dicts if job['salary'] > 90_000]
print(high_pay_jobs)