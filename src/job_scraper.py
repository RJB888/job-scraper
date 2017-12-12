"""Implement a job scraper for StackOverflow."""

import requests
from bs4 import BeautifulSoup as Soup

job_pages = []
for i in range(1, 11):
    print(i)
    url_page = 'https://stackoverflow.com/jobs?pg={}'.format(str(i))
    job_pages.append(requests.get(url_page))

# """
# https://stackoverflow.com/jobs
# https://stackoverflow.com/jobs?pg=2

# """
