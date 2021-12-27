from pandas.core.frame import DataFrame
from pandas.io import excel
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import *


# website we are scraping from
URL = "https://gtaguide.net/gta3/walkthrough/story-missions/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# results is the object we will be scraping the contents from
results = soup.find(class_="articles-list")

full_lst = results.find_all("a")

# initializing arrays to store data in
missions_arr = []
employer_arr = []
description_arr = []
rewards_arr = []

# scraping the data into respective arrays
for i in full_lst:
    missions = i.find("h2").get_text()
    missions_arr.append(missions)
    employer = i.find("li", {"title": "Employer"}).get_text().strip()
    employer_arr.append(employer)
    description = i.find("p").get_text()
    description_arr.append(description)
    rewards = i.find("li", {"title": "Rewards"}).get_text().strip()
    rewards_arr.append(rewards)


col = ["Missions", "Employer", "Description", "Rewards"]

# creating columns and rows for pandas to use
data_helper = {"Missions": missions_arr, "Employer": employer_arr,
               "Description": description_arr, "Rewards": rewards_arr}

# creating the full table using pandas
data_full = pd.DataFrame(data=data_helper)

# use to_csv to export in csv file
data_full.to_excel("missionlist.xlsx")
