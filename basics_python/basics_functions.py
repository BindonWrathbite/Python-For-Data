#1
def job_title_contains(job_title: str, keyword: str) -> bool:
    return keyword in job_title

job_title = 'Data Scientist'
keyword = 'Data'
print(job_title_contains(job_title, keyword))

#2
print('-' * 80)
def average_salary(salaries: list) -> float:
    return sum(salaries) / len(salaries)

salaries = [95000, 120000, 105000, 90000, 130000]
print(average_salary(salaries))

#3
print('-' * 80)
def salary_statistics(salaries: list) -> dict:
    return {'min': min(salaries), 'max': max(salaries), 'average': average_salary(salaries)}

salaries = [95000, 120000, 105000, 90000, 130000]
print(salary_statistics(salaries))

#4
print('-' * 80)
def job_postings_summary(job_postings: list) -> dict:
    total_postings = len(job_postings)
    salary_sum = sum(posting['salary'] for posting in job_postings)
    average_salary = float(f'{salary_sum / total_postings:.2f}')
    unique_locations = list(set(posting['location'] for posting in job_postings))
        
    summary_dict = {
        'Total Postings': total_postings,
        'Average Salary': average_salary,
        'Unique Locations': unique_locations
        }
    return summary_dict

job_postings = [
    {'title': 'Data Scientist', 'location': 'New York', 'salary': 95000},
    {'title': 'Data Analyst', 'location': 'San Francisco', 'salary': 85000},
    {'title': 'Machine Learning Engineer', 'location': 'New York', 'salary': 115000}
]
print(job_postings_summary(job_postings))
