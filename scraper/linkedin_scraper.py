
# First install:
# installation pip install linkedin-jobs-scraper to

import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, RemoteFilters
from pathlib import Path

from db_functions import *

chromedriver_path = str(Path(__file__).parent / "chromedriver")

data_list = []

# Change root logger level (default is WARN)
logging.basicConfig(level = logging.WARN)


def on_data(data: EventData):
    #print('[ON_DATA]', data.title, data.company, data.date, data.link, len(data.description))
    print('Data scraped:', data.title, data.company, data.date, data.link, len(data.description))
    print(type(data))

    data_list.append(data)
    formatted_data = preformat_data(data)

def on_error(error):
    print('[ON_ERROR]', error)


def on_end():
    #print('[ON_END]')
    print('Ended.')
    for data in data_list:
        print('Data scraped:', data.title, data.company, data.date, data.link, len(data.description))
    save_to_db(data_list)


scraper = LinkedinScraper(
    chrome_executable_path=chromedriver_path, # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver) 
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
        query='Ingeniero',
        options=QueryOptions(
            locations=['Argentina'],
            optimize=False,
            limit=5,
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