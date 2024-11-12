#1
monthly_salary = 8000
annual_salary = monthly_salary * 12
print(annual_salary)

#2
avg_salary_analyst = 70000
avg_salary_scientist = 85000
analyst_higher_pay = avg_salary_analyst > avg_salary_scientist
print(analyst_higher_pay)

#3
total_applications = 123
job_openings = 67
remaining_apps = total_applications % job_openings
print(remaining_apps)

#4
job_postings = 20
job_postings += 5
print(job_postings)

#5
min_salary = 50000
max_salary = 120000
avg_salary = format((min_salary + max_salary) / 2, '.2f')
print(f'${avg_salary}')
