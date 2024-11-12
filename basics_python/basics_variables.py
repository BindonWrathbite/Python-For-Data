job_count = 42
print(job_count)

job_title, company_name, isRemote = 'Data Engineer', 'DataWorks', True
print(job_title, company_name, isRemote)

base_salary, bonus = 120_000, 20_000
total_compensation = base_salary + bonus
print(total_compensation)

annual_salary = 72_000
monthly_salary = annual_salary / 12
print(f'${monthly_salary:.2f}')

# Create variables to store the job title, company name, and salary for a Data Scientist position at AI Solutions for $110K. 
# Then, calculate the total compensation by adding a 10% bonus to the salary and print the total compensation, 
# along with the job and company name.
job_title, company_name, salary = 'Data Scientist', 'AI Solutions', 110_000
bonus = salary * .1
total_compensation = salary + bonus
print(f'{job_title}, {company_name}, {total_compensation:.2f}')