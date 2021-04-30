from models import job
from scrapers.linkedin_scraper import job_data_list

job_data = job_data_list()

for job in job_data:
    pass

# Falta poner las cosas en la base de datos como corresponde

