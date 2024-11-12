def filter_by_location(job_postings: list, location: str) -> list:
    return [job for job in job_postings if job['location'] == location]
