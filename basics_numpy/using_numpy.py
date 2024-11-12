import numpy as np

applications_list = [10, 15, 7, 20, 25, 30, 5]
application = np.array(applications_list)
print(application)

print('-' * 80)
postings_list = [10, 15, 7, 20, 25, 30, 5]
postings = np.array(postings_list)
print(postings)
print(postings[:3])

print('-' * 80)
salaries_list = [70000, 85000, 60000, 95000, 80000]
salaries = np.array(salaries_list)
print(salaries)
print(np.max(salaries))
print(np.min(salaries))