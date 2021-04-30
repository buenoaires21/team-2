from models import Job
from scrapers.linkedin_scraper import job_data_list

job_data = job_data_list()

for job in job_data:
    Job.objects.create(
        title=job.title,
        company=job.company,
        place=job.place,
        description=job.description,
        description_html=job.description_html,
        date=job.date,
        seniority_level=job.seniority_level,
        job_function=job.job_function,
        employment_type=job.employment_type,
        industries=job.industries,
        processed=job.processed
    )

