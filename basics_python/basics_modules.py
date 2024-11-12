#1
from salary_calculator import calculate_annual_salary
print(calculate_annual_salary(50, 40))

#2
print('-' * 80)
from job_filter import filter_by_location
job_postings = [
    {'title': 'Data Scientist', 'location': 'New York'},
    {'title': 'Data Analyst', 'location': 'San Francisco'},
    {'title': 'Machine Learning Engineer', 'location': 'New York'}
]
print(filter_by_location(job_postings, 'New York'))
