# Code for Good

## Fundacion SES Challenge

### Grupo 2

- Fichera, Giuliano
- Galli, Milagros
- Gonzalez, Federico
- Passeggi, Franco
- Vazquez, Francisco

#### Challenge

Fundación SES is looking for innovative ways that technology can help them stay connected with the needs of the job market, and at the same time, with the youth themselves, who are looking for job opportunities. In order to keep their training courses and curriculum updated with the best information to direct youths to enter the workforce, they need a way to learn, collect, and analyze the current needs of hiring companies and in-demand job profiles. What are effective ways to keep youths who are preparing for the job market engaged in this content?

#### Introduction

Our solutions tries to keep up with the ever-changing job hunting world, predicting which are the skills that employers are looking for in their aplicants. We take advantage of modern technologies and data analisis to extract conclucions.

Utilizing web scraping technologies we gather information from popular job hunting webpages(like linkedin, zonajobs, bumeran) and break down the qualifications that the employers are looking from their applicants. Based on the results, we can define the skills that young people should be spending their times on improving.

#### Main

We do the data collection with a web scraping algorithm implemented in python, based on a public github repository, from Linkedin. In future deploys, we could broaden our data source, and scrape different job hunting sites, like ZonaJobs, Bumeran, Stackoverflow; and/or get access to some APIs to facilitate the data acquisition and get better results.

Once all the data is saved, we count the amount of occurrences of determined buzzwords in the job descriptions in the database. The buzzwords we use were determined by the team, but in the future we could implement machine learning algorithms to detect them automatically and connect them with the desired abilities.
We could implement a more robust algorithm as well, to determine the importance of said skill. On top of calculating the frequency of the buzzwords, we could estimate the amount of jobs that are looking for said skill as well, and compute a weighted ranking to predict better results.

##### The code ("Code") in this repository was created solely by the student teams during a coding competition hosted by JPMorgan Chase Bank, N.A. ("JPMC").						JPMC did not create or contribute to the development of the Code.  This Code is provided AS IS and JPMC makes no warranty of any kind, express or implied, as to the Code,						including but not limited to, merchantability, satisfactory quality, non-infringement, title or fitness for a particular purpose or use.