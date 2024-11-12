class JobPosting():
    def __init__(self, title: str, company: str, location: str, salary: int):
        self.title = title
        self.company = company
        self.location = location
        self.salary = salary
    
    def to_dict(self):
        return {
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'salary': self.salary
        }
    
    def compare_salary(self, other_job):
        if self.salary > other_job.salary:
            return self.title
        else:
            return other_job.salary

job = JobPosting('Data Scientist', 'Tech Innovations', 'New York', 120_000)
print(job)
print(job.title, job.company, job.location)
print(job.to_dict())

job1 = JobPosting('Data Scientist', 'Tech Innovations', 'New York', 120000)
job2 = JobPosting('Data Analyst', 'Data Driven Co', 'San Francisco', 100000)

higher_job = job1.compare_salary(job2)
print(higher_job)