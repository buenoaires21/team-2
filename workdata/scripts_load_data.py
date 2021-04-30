import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, RemoteFilters
from pathlib import Path

def fetch(query, limit):
    data_list = []

    # Change root logger level (default is WARN)
    logging.basicConfig(level = logging.WARN)

    def on_data(data: EventData):

        data_dict = {
            "title": data.title,
            "company": data.company,
            "place": data.place,
            "description":data.description,
            "description_html": "",
            "date": data.date,
            "seniority_level": data.seniority_level,
            "job_function": data.job_function,
            "employment_type": data.employment_type,
            "industries": data.industries,
            "query": query
        }

        data_list.append(data_dict)
        

    def on_error(error):
        pass

    def on_end():
        if len(data_list) == 0:
            print("no se encontraron resulados")
            return fetch(query, limit)
        


    scraper = LinkedinScraper(
        # no es necesario. si no esta, agarra del path directamente.
        #chrome_executable_path='/usr/bin/chromedriver', # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver) 
        chrome_options=None,  # Custom Chrome options here
        headless=True,  # Overrides headless mode only if chrome_options is None
        max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
        slow_mo=1.3,  # Slow down the scraper to avoid 'Too many requests (429)' errors
    )

    # Add event listeners
    scraper.on(Events.DATA, on_data)
    scraper.on(Events.ERROR, on_error)
    scraper.on(Events.END, on_end)

    queries = [
        Query(
            query=query,
            options=QueryOptions(
                locations=['Argentina'],
                optimize=False,
                limit=limit,
                filters=QueryFilters(
                    company_jobs_url= None,  # Filter by companies
                    relevance=RelevanceFilters.RECENT,
                    time=TimeFilters.MONTH,
                    type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                    experience=None,                
                )
            )
        ),
    ]

    scraper.run(queries)


    return data_list

def load_job_data(query, limit):
    job_data = fetch(query, limit)

    for job in job_data:
        Job.objects.create(
            title=job["title"],
            company=job["company"],
            place=job["place"],
            description=job["description"],
            description_html=job["description_html"],
            date=job["date"],
            seniority_level=job["seniority_level"],
            job_function=job["job_function"],
            employment_type=job["employment_type"],
            industries=job["industries"],
            query=job["query"]
        )

DATA_TO_BE_FETCHED = [("ingeniero software", 50),("contador", 30),("administracion", 30), ("diseno", 30)]

for data in DATA_TO_BE_FETCHED:
    load_job_data(data[0], data[1])
