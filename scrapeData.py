import requests
from requests import get
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from time import sleep
import csv
from random import randint 

postings = [] 

def getPosts(pos, loc, province, page):
    url = (f'https://ca.indeed.com/jobs?q={pos}&l={loc}%2C+{province}&start={page}')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    posts = soup.find_all('div', class_ = 'job_seen_beacon')
    for item in posts:
        info = {
        #getting the title
        'title': item.find('h2').text,
        #getting the company
        'company': item.find('span', 'companyName').text,
        #getting the location
        'location': item.find('div', class_ = 'companyLocation').text,
        #getting the job description
        'description': item.find('div', class_ = 'job-snippet').text,
        #getting the post date
        'postDate': item.find('span', 'date').text,
        }
        postings.append(info)
    return

for i in range(1, 11):
    getPosts('developer', 'Toronto', 'ON', i)
    time.sleep(5)
    #getPosts('engineer', 'Toronto', 'ON', i)

print(len(postings))
'''
jobs = pd.DataFrame(postings)
jobs.to_csv('jobs.csv')
'''