# 1
job_title = 'Data Scientist'
print(type(job_title)) #str

# 2
salary = 85_000.50
print(type(salary)) #float

# 3
salary_rate = 120_000.75
salary_rate = int(salary_rate) #cast as int
print(type(salary_rate)) #returns type 'int'

# 4
company_name = 'DataWiz Inc'
print(isinstance(company_name, str))