# Define imports
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Spreadsheet
RACERATINGS_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS9a9ZQ1fuEJTJDaHr_l020mLxarOYN_DmeLNc9VmqCDqtARStP6bF1PuFNI5GlwqBiATcCR3mwtiaB/pubhtml?gid=4758905&amp;single=true#'
SPREADSHEET_PAGE_CONTENT = requests.get(RACERATINGS_URL)
SPREADSHEET_SOUP = BeautifulSoup(SPREADSHEET_PAGE_CONTENT.content, 'html5lib')

## Create Data Frame and Collection Structure for the house
HOUSE_COLUMN_NAME = ['Key','Name', 'Party', 'District', 'Status', 'Date Declared', 'Retiring', 'Seeking other Office', 'Running Senate', 'Cooke','Inside', 'Sabato']
HOUSE_DATA_FRAME = pd.DataFrame(columns=HOUSE_COLUMN_NAME)
HOUSE_FILE_NAME = 'house_data.csv'
HOUSE_URL = 'https://ballotpedia.org/United_States_House_of_Representatives_elections,_2024'
HOUSE_PAGE_CONTENT = requests.get(HOUSE_URL)
HOUSE_SOUP = BeautifulSoup(HOUSE_PAGE_CONTENT.content, 'html5lib')
RETIRINGHOUSE_HEADER = 'Retiring from public office, 2024'
RUNNINGSENATE_HEADER = 'Running for Senate, 2024'
OTHEROFFICE_HEADER = 'Running for another office, 2024'

## Create Data Frame and Collection Structure for the senate
SENATE_COLUMN_NAME = ['Key', 'Name', 'State', 'Retiring', 'Seeking other Office', 'Cooke','Inside', 'Sabato']
SENATE_DATA_FRAME = pd.DataFrame(columns=SENATE_COLUMN_NAME)
SENATE_FILE_NAME = 'senate_data.csv'
SENATE_URL = 'https://ballotpedia.org/United_States_Senate_elections,_2024'
SENATE_PAGE_CONTENT = requests.get(SENATE_URL)
SENATE_SOUP = BeautifulSoup(SENATE_PAGE_CONTENT.content, 'html5lib')
RETIRINGSENATE_HEADER = 'Retiring from public office, 2024'
RUNNINGGOVERNER_HEADER = 'Running for governor, 2024'

## Create Data Frame and Collection Structure for the governers office
GOVERNER_COLUMN_NAME = ['Key','Name', 'State', 'Incumbent Running', 'Cooke','Inside', 'Sabato']
GOVERNER_DATA_FRAME = pd.DataFrame(columns=GOVERNER_COLUMN_NAME)
GOVERNER_FILE_NAME = 'governer_data.csv'
GOVERNER_URL = 'https://ballotpedia.org/Gubernatorial_elections,_2024'
GOVERNER_PAGE_CONTENT = requests.get(GOVERNER_URL)
GOVERNER_SOUP = BeautifulSoup(GOVERNER_PAGE_CONTENT.content, 'html5lib')
CANDIDATESSENATE_HEADER = '2024 Senate elections'
GUBERNATORIALELECTIONS_HEADER = 'Gubernatorial elections, 2022'

# Create Python dictionary for districts
us_house_dict = {
    "CA-01": "U.S. House California District 1",
    "CA-02": "U.S. House California District 2",
    "CA-03": "U.S. House California District 3",
    "CA-04": "U.S. House California District 4",
    "CA-05": "U.S. House California District 5",
    "CA-06": "U.S. House California District 6",
    "CA-07": "U.S. House California District 7",
    "CA-08": "U.S. House California District 8",
    "CA-09": "U.S. House California District 9",
    "CA-10": "U.S. House California District 10",
    "CA-11": "U.S. House California District 11",
    "CA-12": "U.S. House California District 12",
    "CA-13": "U.S. House California District 13",
    "CA-14": "U.S. House California District 14",
    "CA-15": "U.S. House California District 15",
    "CA-16": "U.S. House California District 16",
    "CA-17": "U.S. House California District 17",
    "CA-18": "U.S. House California District 18",
    "CA-19": "U.S. House California District 19",
    "CA-20": "U.S. House California District 20",
    "CA-21": "U.S. House California District 21",
    "CA-22": "U.S. House California District 22",
    "CA-23": "U.S. House California District 23",
    "CA-24": "U.S. House California District 24",
    "CA-25": "U.S. House California District 25",
    "CA-26": "U.S. House California District 26",
    "CA-27": "U.S. House California District 27",
    "CA-28": "U.S. House California District 28",
    "CA-29": "U.S. House California District 29",
    "CA-30": "U.S. House California District 30",
    "CA-31": "U.S. House California District 31",
    "CA-32": "U.S. House California District 32",
    "CA-33": "U.S. House California District 33",
    "CA-34": "U.S. House California District 34",
    "CA-35": "U.S. House California District 35",
    "CA-36": "U.S. House California District 36",
    "CA-37": "U.S. House California District 37",
    "CA-38": "U.S. House California District 38",
    "CA-39": "U.S. House California District 39",
    "CA-40": "U.S. House California District 40",
    "CA-41": "U.S. House California District 41",
    "CA-42": "U.S. House California District 42",
    "CA-43": "U.S. House California District 43",
    "CA-44": "U.S. House California District 44",
    "CA-45": "U.S. House California District 45",
    "CA-46": "U.S. House California District 46",
    "CA-47": "U.S. House California District 47",
    "CA-48": "U.S. House California District 48",
    "CA-49": "U.S. House California District 49",
    "CA-50": "U.S. House California District 50",
    "CA-51": "U.S. House California District 51",
    "CA-52": "U.S. House California District 52",
    "CA-53": "U.S. House California District 53",
    "GA-01": "U.S. House Georgia District 1",
    "GA-02": "U.S. House Georgia District 2",
    "GA-03": "U.S. House Georgia District 3",
    "GA-04": "U.S. House Georgia District 4",
    "GA-05": "U.S. House Georgia District 5",
    "GA-06": "U.S. House Georgia District 6",
    "GA-07": "U.S. House Georgia District 7",
    "GA-08": "U.S. House Georgia District 8",
    "GA-09": "U.S. House Georgia District 9",
    "GA-10": "U.S. House Georgia District 10",
    "GA-11": "U.S. House Georgia District 11",
    "GA-12": "U.S. House Georgia District 12",
    "GA-13": "U.S. House Georgia District 13",
    "GA-14": "U.S. House Georgia District 14",
    "KS-01": "U.S. House Kansas District 1",
    "KS-02": "U.S. House Kansas District 2",
    "KS-03": "U.S. House Kansas District 3",
    "KS-04": "U.S. House Kansas District 4",
    "MN-01": "U.S. House Minnesota District 1",
    "MN-02": "U.S. House Minnesota District 2",
    "MN-03": "U.S. House Minnesota District 3",
    "MN-04": "U.S. House Minnesota District 4",
    "MN-05": "U.S. House Minnesota District 5",
    "MN-06": "U.S. House Minnesota District 6",
    "MN-07": "U.S. House Minnesota District 7",
    "MN-08": "U.S. House Minnesota District 8",
    "NY-01": "U.S. House New York District 1",
    "NY-02": "U.S. House New York District 2",
    "NY-03": "U.S. House New York District 3",
    "NY-04": "U.S. House New York District 4",
    "NY-05": "U.S. House New York District 5",
    "NY-06": "U.S. House New York District 6",
    "NY-07": "U.S. House New York District 7",
    "NY-08": "U.S. House New York District 8",
    "NY-09": "U.S. House New York District 9",
    "NY-10": "U.S. House New York District 10",
    "NY-11": "U.S. House New York District 11",
    "NY-12": "U.S. House New York District 12",
    "NY-13": "U.S. House New York District 13",
    "NY-14": "U.S. House New York District 14",
    "NY-15": "U.S. House New York District 15",
    "NY-16": "U.S. House New York District 16",
    "NY-17": "U.S. House New York District 17",
    "NY-18": "U.S. House New York District 18",
    "NY-19": "U.S. House New York District 19",
    "NY-20": "U.S. House New York District 20",
    "NY-21": "U.S. House New York District 21",
    "NY-22": "U.S. House New York District 22",
    "NY-23": "U.S. House New York District 23",
    "NY-24": "U.S. House New York District 24",
    "NY-25": "U.S. House New York District 25",
    "NY-26": "U.S. House New York District 26",
    "NY-27": "U.S. House New York District 27",
    "OR-01": "U.S. House Oregon District 1",
    "OR-02": "U.S. House Oregon District 2",
    "OR-03": "U.S. House Oregon District 3",
    "OR-04": "U.S. House Oregon District 4",
    "OR-05": "U.S. House Oregon District 5",
    "DC-01": "U.S. House District of Columbia At-Large",
    "AL-01": "U.S. House Alabama District 1",
    "AL-02": "U.S. House Alabama District 2",
    "AL-03": "U.S. House Alabama District 3",
    "AL-04": "U.S. House Alabama District 4",
    "AL-05": "U.S. House Alabama District 5",
    "AL-06": "U.S. House Alabama District 6",
    "AL-07": "U.S. House Alabama District 7",
    "AK-01": "U.S. House Alaska At-Large District",
    "AS-01": "U.S. House American Samoa At-Large District",
    "AZ-01": "U.S. House Arizona District 1",
    "AZ-02": "U.S. House Arizona District 2",
    "AZ-03": "U.S. House Arizona District 3",
    "AZ-04": "U.S. House Arizona District 4",
    "AZ-05": "U.S. House Arizona District 5",
    "AZ-06": "U.S. House Arizona District 6",
    "AZ-07": "U.S. House Arizona District 7",
    "AZ-08": "U.S. House Arizona District 8",
    "AZ-09": "U.S. House Arizona District 9",
    "AR-01": "U.S. House Arkansas District 1",
    "AR-02": "U.S. House Arkansas District 2",
    "AR-03": "U.S. House Arkansas District 3",
    "AR-04": "U.S. House Arkansas District 4",
    "CO-01": "U.S. House Colorado District 1",
    "CO-02": "U.S. House Colorado District 2",
    "CO-03": "U.S. House Colorado District 3",
    "CO-04": "U.S. House Colorado District 4",
    "CO-05": "U.S. House Colorado District 5",
    "CO-06": "U.S. House Colorado District 6",
    "CO-07": "U.S. House Colorado District 7",
    "CT-01": "U.S. House Connecticut District 1",
    "CT-02": "U.S. House Connecticut District 2",
    "CT-03": "U.S. House Connecticut District 3",
    "CT-04": "U.S. House Connecticut District 4",
    "CT-05": "U.S. House Connecticut District 5",
    "DE-01": "U.S. House Delaware At-Large District",
    "FL-01": "U.S. House Florida District 1",
    "FL-02": "U.S. House Florida District 2",
    "FL-03": "U.S. House Florida District 3",
    "FL-04": "U.S. House Florida District 4",
    "FL-05": "U.S. House Florida District 5",
    "FL-06": "U.S. House Florida District 6",
    "FL-07": "U.S. House Florida District 7",
    "FL-08": "U.S. House Florida District 8",
    "FL-09": "U.S. House Florida District 9",
    "FL-10": "U.S. House Florida District 10",
    "FL-11": "U.S. House Florida District 11",
    "FL-12": "U.S. House Florida District 12",
    "FL-13": "U.S. House Florida District 13",
    "FL-14": "U.S. House Florida District 14",
    "FL-15": "U.S. House Florida District 15",
    "FL-16": "U.S. House Florida District 16",
    "FL-17": "U.S. House Florida District 17",
    "FL-18": "U.S. House Florida District 18",
    "FL-19": "U.S. House Florida District 19",
    "FL-20": "U.S. House Florida District 20",
    "FL-21": "U.S. House Florida District 21",
    "FL-22": "U.S. House Florida District 22",
    "FL-23": "U.S. House Florida District 23",
    "FL-24": "U.S. House Florida District 24",
    "FL-25": "U.S. House Florida District 25",
    "FL-26": "U.S. House Florida District 26",
    "FL-27": "U.S. House Florida District 27",
    "GU-01": "U.S. House Guam At-Large District",
    "HI-01": "U.S. House Hawaii District 1",
    "HI-02": "U.S. House Hawaii District 2",
    "ID-01": "U.S. House Idaho District 1",
    "ID-02": "U.S. House Idaho District 2",
    "IL-01": "U.S. House Illinois District 1",
    "IL-02": "U.S. House Illinois District 2",
    "IL-03": "U.S. House Illinois District 3",
    "IL-04": "U.S. House Illinois District 4",
    "IL-05": "U.S. House Illinois District 5",
    "IL-06": "U.S. House Illinois District 6",
    "IL-07": "U.S. House Illinois District 7",
    "IL-08": "U.S. House Illinois District 8",
    "IL-09": "U.S. House Illinois District 9",
    "IL-10": "U.S. House Illinois District 10",
    "IL-11": "U.S. House Illinois District 11",
    "IL-12": "U.S. House Illinois District 12",
    "IL-13": "U.S. House Illinois District 13",
    "IL-14": "U.S. House Illinois District 14",
    "IL-15": "U.S. House Illinois District 15",
    "IL-16": "U.S. House Illinois District 16",
    "IL-17": "U.S. House Illinois District 17",
    "IL-18": "U.S. House Illinois District 18",
    "LA-01": "U.S. House Louisiana District 1",
    "LA-02": "U.S. House Louisiana District 2",
    "LA-03": "U.S. House Louisiana District 3",
    "LA-04": "U.S. House Louisiana District 4",
    "LA-05": "U.S. House Louisiana District 5",
    "LA-06": "U.S. House Louisiana District 6",
    "MD-01": "U.S. House Maryland District 1",
    "MD-02": "U.S. House Maryland District 2",
    "MD-03": "U.S. House Maryland District 3",
    "MD-04": "U.S. House Maryland District 4",
    "MD-05": "U.S. House Maryland District 5",
    "MD-06": "U.S. House Maryland District 6",
    "MD-07": "U.S. House Maryland District 7",
    "MD-08": "U.S. House Maryland District 8",
    "MA-01": "U.S. House Massachusetts District 1",
    "MA-02": "U.S. House Massachusetts District 2",
    "MA-03": "U.S. House Massachusetts District 3",
    "MA-04": "U.S. House Massachusetts District 4",
    "MA-05": "U.S. House Massachusetts District 5",
    "MA-06": "U.S. House Massachusetts District 6",
    "MA-07": "U.S. House Massachusetts District 7",
    "MA-08": "U.S. House Massachusetts District 8",
    "MA-09": "U.S. House Massachusetts District 9",
    "IN-01": "U.S. House Indiana District 1",
    "IN-02": "U.S. House Indiana District 2",
    "IN-03": "U.S. House Indiana District 3",
    "IN-04": "U.S. House Indiana District 4",
    "IN-05": "U.S. House Indiana District 5",
    "IN-06": "U.S. House Indiana District 6",
    "IN-07": "U.S. House Indiana District 7",
    "IN-08": "U.S. House Indiana District 8",
    "IN-09": "U.S. House Indiana District 9",
    "ME-01": "U.S. House Maine District 1",
    "ME-02": "U.S. House Maine District 2",
    "MS-01": "U.S. House Mississippi District 1",
    "MS-02": "U.S. House Mississippi District 2",
    "MS-03": "U.S. House Mississippi District 3",
    "MS-04": "U.S. House Mississippi District 4",
    "MO-01": "U.S. House Missouri District 1",
    "MO-02": "U.S. House Missouri District 2",
    "MO-03": "U.S. House Missouri District 3",
    "MO-04": "U.S. House Missouri District 4",
    "MO-05": "U.S. House Missouri District 5",
    "MO-06": "U.S. House Missouri District 6",
    "MO-07": "U.S. House Missouri District 7",
    "MO-08": "U.S. House Missouri District 8",
    "NC-01": "U.S. House North Carolina District 1",
    "NC-02": "U.S. House North Carolina District 2",
    "NC-03": "U.S. House North Carolina District 3",
    "NC-04": "U.S. House North Carolina District 4",
    "NC-05": "U.S. House North Carolina District 5",
    "NC-06": "U.S. House North Carolina District 6",
    "NC-07": "U.S. House North Carolina District 7",
    "NC-08": "U.S. House North Carolina District 8",
    "NC-09": "U.S. House North Carolina District 9",
    "NC-10": "U.S. House North Carolina District 10",
    "NC-11": "U.S. House North Carolina District 11",
    "NC-12": "U.S. House North Carolina District 12",
    "NC-13": "U.S. House North Carolina District 13",
    "ND-01": "U.S. House North Dakota At-Large District",
    "MP-01": "U.S. House Northern Mariana Islands At-Large District",
    "OH-01": "U.S. House Ohio District 1",
    "OH-02": "U.S. House Ohio District 2",
    "OH-03": "U.S. House Ohio District 3",
    "OH-04": "U.S. House Ohio District 4",
    "OH-05": "U.S. House Ohio District 5",
    "OH-06": "U.S. House Ohio District 6",
    "OH-07": "U.S. House Ohio District 7",
    "OH-08": "U.S. House Ohio District 8",
    "OH-09": "U.S. House Ohio District 9",
    "OH-10": "U.S. House Ohio District 10",
    "OH-11": "U.S. House Ohio District 11",
    "OH-12": "U.S. House Ohio District 12",
    "OH-13": "U.S. House Ohio District 13",
    "OH-14": "U.S. House Ohio District 14",
    "OH-15": "U.S. House Ohio District 15",
    "OH-16": "U.S. House Ohio District 16",
    "IA-01": "U.S. House Iowa District 1",
    "IA-02": "U.S. House Iowa District 2",
    "IA-03": "U.S. House Iowa District 3",
    "IA-04": "U.S. House Iowa District 4",
    "KY-01": "U.S. House Kentucky District 1",
    "KY-02": "U.S. House Kentucky District 2",
    "KY-03": "U.S. House Kentucky District 3",
    "KY-04": "U.S. House Kentucky District 4",
    "KY-05": "U.S. House Kentucky District 5",
    "KY-06": "U.S. House Kentucky District 6",
    "MI-01": "U.S. House Michigan District 1",
    "MI-02": "U.S. House Michigan District 2",
    "MI-03": "U.S. House Michigan District 3",
    "MI-04": "U.S. House Michigan District 4",
    "MI-05": "U.S. House Michigan District 5",
    "MI-06": "U.S. House Michigan District 6",
    "MI-07": "U.S. House Michigan District 7",
    "MI-08": "U.S. House Michigan District 8",
    "MI-09": "U.S. House Michigan District 9",
    "MI-10": "U.S. House Michigan District 10",
    "MI-11": "U.S. House Michigan District 11",
    "MI-12": "U.S. House Michigan District 12",
    "MI-13": "U.S. House Michigan District 13",
    "MI-14": "U.S. House Michigan District 14",
    "MT-01": "U.S. House Montana At-Large District",
    "NE-01": "U.S. House Nebraska District 1",
    "NE-02": "U.S. House Nebraska District 2",
    "NE-03": "U.S. House Nebraska District 3",
    "NV-01": "U.S. House Nevada District 1",
    "NV-02": "U.S. House Nevada District 2",
    "NV-03": "U.S. House Nevada District 3",
    "NV-04": "U.S. House Nevada District 4",
    "NH-01": "U.S. House New Hampshire District 1",
    "NH-02": "U.S. House New Hampshire District 2",
    "NJ-01": "U.S. House New Jersey District 1",
    "NJ-02": "U.S. House New Jersey District 2",
    "NJ-03": "U.S. House New Jersey District 3",
    "NJ-04": "U.S. House New Jersey District 4",
    "NJ-05": "U.S. House New Jersey District 5",
    "NJ-06": "U.S. House New Jersey District 6",
    "NJ-07": "U.S. House New Jersey District 7",
    "NJ-08": "U.S. House New Jersey District 8",
    "NJ-09": "U.S. House New Jersey District 9",
    "NJ-10": "U.S. House New Jersey District 10",
    "NJ-11": "U.S. House New Jersey District 11",
    "NJ-12": "U.S. House New Jersey District 12",
    "NM-01": "U.S. House New Mexico District 1",
    "NM-02": "U.S. House New Mexico District 2",
    "NM-03": "U.S. House New Mexico District 3",
    "OK-01": "U.S. House Oklahoma District 1",
    "OK-02": "U.S. House Oklahoma District 2",
    "OK-03": "U.S. House Oklahoma District 3",
    "OK-04": "U.S. House Oklahoma District 4",
    "OK-05": "U.S. House Oklahoma District 5",
    "PA-01": "U.S. House Pennsylvania District 1",
    "PA-02": "U.S. House Pennsylvania District 2",
    "PA-03": "U.S. House Pennsylvania District 3",
    "PA-04": "U.S. House Pennsylvania District 4",
    "PA-05": "U.S. House Pennsylvania District 5",
    "PA-06": "U.S. House Pennsylvania District 6",
    "PA-07": "U.S. House Pennsylvania District 7",
    "PA-08": "U.S. House Pennsylvania District 8",
    "PA-09": "U.S. House Pennsylvania District 9",
    "PA-10": "U.S. House Pennsylvania District 10",
    "PA-11": "U.S. House Pennsylvania District 11",
    "PA-12": "U.S. House Pennsylvania District 12",
    "PA-13": "U.S. House Pennsylvania District 13",
    "PA-14": "U.S. House Pennsylvania District 14",
    "PA-15": "U.S. House Pennsylvania District 15",
    "U.S. House North Carolina District 9": "NC-09",
    "U.S. House North Carolina District 10": "NC-10",
    "U.S. House North Carolina District 11": "NC-11",
    "U.S. House North Carolina District 12": "NC-12",
    "U.S. House North Carolina District 13": "NC-13",
    "U.S. House North Dakota At-Large District": "ND-01",
    "U.S. House Northern Mariana Islands At-Large District": "MP-01",
    "U.S. House Ohio District 1": "OH-01",
    "U.S. House Ohio District 2": "OH-02",
    "U.S. House Ohio District 3": "OH-03",
    "U.S. House Ohio District 4": "OH-04",
    "U.S. House Ohio District 5": "OH-05",
    "U.S. House Ohio District 6": "OH-06",
    "U.S. House Ohio District 7": "OH-07",
    "U.S. House Ohio District 8": "OH-08",
    "U.S. House Ohio District 9": "OH-09",
    "U.S. House Ohio District 10": "OH-10",
    "U.S. House Ohio District 11": "OH-11",
    "U.S. House Ohio District 12": "OH-12",
    "U.S. House Ohio District 13": "OH-13",
    "U.S. House Ohio District 14": "OH-14",
    "U.S. House Ohio District 15": "OH-15",
    "U.S. House Ohio District 16": "OH-16",
    "U.S. House Ohio District 17": "OH-17",
    "U.S. House Ohio District 18": "OH-18",
    "U.S. House Rhode Island District 1": "RI-01",
    "U.S. House Rhode Island District 2": "RI-02",
    "U.S. House South Carolina District 1": "SC-01",
    "U.S. House South Carolina District 2": "SC-02",
    "U.S. House South Carolina District 3": "SC-03",
    "U.S. House South Carolina District 4": "SC-04",
    "U.S. House South Carolina District 5": "SC-05",
    "U.S. House South Carolina District 6": "SC-06",
    "U.S. House South Carolina District 7": "SC-07",
    "U.S. House South Dakota At-Large District": "SD-01",
    "U.S. House Tennessee District 1": "TN-01",
    "U.S. House Tennessee District 2": "TN-02",
    "U.S. House Tennessee District 3": "TN-03",
    "U.S. House Tennessee District 4": "TN-04",
    "U.S. House Tennessee District 5": "TN-05",
    "U.S. House Tennessee District 6": "TN-06",
    "U.S. House Tennessee District 7": "TN-07",
    "U.S. House Tennessee District 8": "TN-08",
    "U.S. House Tennessee District 9": "TN-09",
    "U.S. House Texas District 1": "TX-01",
    "U.S. House Texas District 2": "TX-02",
    "U.S. House Texas District 3": "TX-03",
    "U.S. House Texas District 4": "TX-04",
    "U.S. House Texas District 5": "TX-05",
    "U.S. House Texas District 6": "TX-06",
    "U.S. House Texas District 7": "TX-07",
    "U.S. House Texas District 8": "TX-08",
    "U.S. House Texas District 9": "TX-09",
    "U.S. House Texas District 10": "TX-10",
    "U.S. House Texas District 11": "TX-11",
    "U.S. House Texas District 12": "TX-12",
    "U.S. House Texas District 13": "TX-13",
    "U.S. House Texas District 14": "TX-14",
    "U.S. House Texas District 15": "TX-15",
    "U.S. House Texas District 16": "TX-16",
    "U.S. House Texas District 17": "TX-17",
    "U.S. House Texas District 18": "TX-18",
    "U.S. House Texas District 19": "TX-19",
    "U.S. House Texas District 20": "TX-20",
    "U.S. House Texas District 21": "TX-21",
    "U.S. House Texas District 22": "TX-22",
    "U.S. House Texas District 23": "TX-23",
    "U.S. House Texas District 24": "TX-24",
    "U.S. House Texas District 25": "TX-25",
    "U.S. House Texas District 26": "TX-26",
    "U.S. House Texas District 27": "TX-27",
    "U.S. House Texas District 28": "TX-28",
    "U.S. House Texas District 29": "TX-29",
    "U.S. House Texas District 30": "TX-30",
    "U.S. House Texas District 31": "TX-31",
    "U.S. House Texas District 32": "TX-32",
    "U.S. House Texas District 33": "TX-33",
    "U.S. House Texas District 34": "TX-34",
    "U.S. House Texas District 35": "TX-35",
    "U.S. House Texas District 36": "TX-36",
    "U.S. House Utah District 1": "UT-01",
    "U.S. House Utah District 2": "UT-02",
    "U.S. House Utah District 3": "UT-03",
    "U.S. House Utah District 4": "UT-04",
    "U.S. House Vermont At-Large District": "VT-01",
    "U.S. House Virginia District 1": "VA-01",
    "U.S. House Virginia District 2": "VA-02",
    "U.S. House Virginia District 3": "VA-03",
    "U.S. House Virginia District 4": "VA-04",
    "U.S. House Virginia District 5": "VA-05",
    "U.S. House Virginia District 6": "VA-06",
    "U.S. House Virginia District 7": "VA-07",
    "U.S. House Virginia District 8": "VA-08",
    "U.S. House Virginia District 9": "VA-09",
    "U.S. House Virginia District 10": "VA-10",
    "U.S. House Virginia District 11": "VA-11",
    "U.S. House U.S. Virgin Islands At-Large District": "VI-01",
    "U.S. House Washington District 1": "WA-01",
    "U.S. House Washington District 2": "WA-02",
    "U.S. House Washington District 3": "WA-03",
    "U.S. House Washington District 4": "WA-04",
    "U.S. House Washington District 5": "WA-05",
    "U.S. House Washington District 6": "WA-06",
    "U.S. House Washington District 7": "WA-07",
    "U.S. House Washington District 8": "WA-08",
    "U.S. House Washington District 9": "WA-09",
    "U.S. House Washington District 10": "WA-10",
    "U.S. House West Virginia District 1": "WV-01",
    "U.S. House West Virginia District 2": "WV-02",
    "U.S. House West Virginia District 3": "WV-03",
    "U.S. House Wisconsin District 1": "WI-01",
    "U.S. House Wisconsin District 2": "WI-02",
    "U.S. House Wisconsin District 3": "WI-03",
    "U.S. House Wisconsin District 4": "WI-04",
    "U.S. House Wisconsin District 5": "WI-05",
    "U.S. House Wisconsin District 6": "WI-06",
    "U.S. House Wisconsin District 7": "WI-07",
    "U.S. House Wisconsin District 8": "WI-08",
    "U.S. House Wyoming At-Large District": "WY-01"
}

retiring_house = []
running_senate =[]
other_office = []

retiring_senate = []
running_governor = []

house_candidates = []
senate_candidates = []
governor_candidates = []

spreadsheet_house = []
spreadsheet_senate = []
spreadsheet_governor = []


house = []
senate = []
governers = []

# Algorithm for the HOUSE data:
# Create 3d array to store data
# Parse 1st 3 tables, store date in 3 seperate arrays.
# Parse Candiates list, add data to profile in an array, compare to 3 arrays to see if user exists, if so, change the data accordingly and pop them from those arrays, don't compare is len of array is 0
# Parse Outside race ratings reports, add to profiles

# Algorithm for the SENATE data:
# Create 3d array to store data
# Parse 1st 2 tables, store date in 3 seperate arrays
# Parse Candiates list by state, add data to profile
# Parse Outside race ratings reports, add to profiles

# Algorithm for the GOVERNER data:
# Create 3d array to store data
# Parse the Gubernatorial elections, 2022 table
# Update based on the Gubernatorial elections, 2024 table
def scraper(file_name, soup, spread_soup):
    # Get the container:
    container = soup.find('div', attrs={'class':'mw-body'})
    tables = container.find_all('table', attrs={'class':'marqueetable'})
    if file_name == 'house_data.csv':   
        for table in tables:
            table_headers = table.find_all('th')
            for header in table_headers:
                if (RETIRINGHOUSE_HEADER in header.getText()):
                    rows = table.find_all('tr')
                    index = 0
                    for row in rows:
                        texts = row.find_all('a')
                        retiring_house.insert(index, [])
                        for text in texts:
                            if (text.getText() != '' and '[' not in text.getText()):
                                retiring_house[index].append(text.getText())
                        index+=1
                if (RUNNINGSENATE_HEADER in header.getText()):
                    rows = table.find_all('tr')
                    index = 0
                    for row in rows:
                        texts = row.find_all('a')
                        running_senate.insert(index, [])
                        for text in texts:
                            if (text.getText() != '' and '[' not in text.getText()):
                                running_senate[index].append(text.getText())
                        index+=1
                if (OTHEROFFICE_HEADER in header.getText()):
                    rows = table.find_all('tr')
                    index = 0
                    for row in rows:
                        texts = row.find_all('a')
                        other_office.insert(index, [])
                        for text in texts:
                            if (text.getText() != '' and '[' not in text.getText()):
                                other_office[index].append(text.getText())
                        index+=1

        # Process house member data
        candidates_window = soup.find('div', attrs={'class':'tab-content H800'})
        state_tabs = candidates_window.find_all('div', attrs={'class':'tab-pane'})
        for tab in state_tabs:
            body = tab.find('tbody')
            rows = body.find_all('tr')
            for row in rows:
                temp = []
                candidiate = row.find('td', attrs={'data-cell':'candidate'})
                candidiate_text = candidiate.find_all('a')
                for text in candidiate_text:
                    input = text.getText()
                    input = input.replace('\t', '').replace('\n', '')
                    temp.append(input)
                party = row.find('td', attrs={'data-cell':'party'})
                party_text = party.find_all('span')
                for text in party_text:
                    input = text.getText()
                    input = input.replace('\t', '').replace('\n', '')
                    temp.append(input)
                office = row.find('td', attrs={'data-cell':'office'})
                office_text = office.find_all('a')
                for text in office_text:
                    input = text.getText()
                    input = input.replace('\t', '').replace('\n', '')
                    temp.append(input)
                status = row.find('td', attrs={'data-cell':'status'})
                input = status.getText()
                input = input.replace('\t', '').replace('\n', '')
                temp.append(input)
                date = row.find('td', attrs={'data-cell':'date'})
                input = date.getText()
                input = input.replace('\t', '').replace('\n', '')
                temp.append(input)
                house_candidates.append(temp)

        # Process report data
        container = spread_soup.find('div', attrs={'id':'sheets-viewport'})
        table = container.find('div', attrs={'id':'4758905'})
        table_rows = table.find_all('tr')
        index = 0
        for row in table_rows:
            texts = row.find_all('td')
            spreadsheet_house.insert(index, [])
            for text in texts:
                if (text.getText() != ''):
                        spreadsheet_house[index].append(text.getText())
            index+=1

        

    if file_name == 'senate_data.csv':
        for table in tables:
            table_headers = table.find_all('th')
            for header in table_headers:
                if (RETIRINGSENATE_HEADER in header.getText()):
                    rows = table.find_all('tr')
                    index = 0
                    for row in rows:
                        texts = row.find_all('a')
                        retiring_senate.insert(index, [])
                        for text in texts:
                            if (text.getText() != '' and '[' not in text.getText()):
                                retiring_senate[index].append(text.getText())
                        index+=1
                if (RUNNINGGOVERNER_HEADER in header.getText()):
                    rows = table.find_all('tr')
                    index = 0
                    for row in rows:
                        texts = row.find_all('a')
                        running_governor.insert(index, [])
                        for text in texts:
                            if (text.getText() != '' and '[' not in text.getText()):
                                running_governor[index].append(text.getText())
                        index+=1
                if (CANDIDATESSENATE_HEADER in header.getText()):
                    rows = table.find_all('tr')
                    index = 0
                    for row in rows:
                        texts = row.find_all('a')
                        senate_candidates.insert(index, [])
                        for text in texts:
                            if (text.getText() != '' and '[' not in text.getText() and not re.search(r"\([A-Za-z\s]+\)", text.getText())):
                                word = text.getText()
                                words = word.split()
                                if len(words) >= 2:
                                    first_name = words[0]
                                    last_name = words[1]
                                    first_name = first_name.strip()
                                    last_name = last_name.strip()
                                    cleaned_full_name = f"{first_name} {last_name}"
                                    senate_candidates[index].append(cleaned_full_name)
                                else:
                                    senate_candidates[index].append(text.getText())
                        index+=1

        # Process report data
        container = spread_soup.find('div', attrs={'id':'sheets-viewport'})
        table = container.find('div', attrs={'id':'574950020'})
        table_rows = table.find_all('tr')
        index = 0
        for row in table_rows:
            texts = row.find_all('td')
            spreadsheet_senate.insert(index, [])
            for text in texts:
                if (text.getText() != ''):
                        spreadsheet_senate[index].append(text.getText())
            index+=1

        

    if file_name == 'governer_data.csv':
        key_counter = 0
        for table in tables:
            table_headers = table.find_all('th')
            for header in table_headers:
                if (GUBERNATORIALELECTIONS_HEADER in header.getText()):
                    rows = table.find_all('tr')
                    index = 0
                    for row in rows:
                        table_data = row.find_all('td')
                        if len(table_data) > 1:
                            state_find = table_data[0].find('a')
                            state = state_find.getText()
                            incumbent_find = table_data[1].find_all('a')
                            incumbent = incumbent_find[1].getText()
                            running = table_data[2].getText()
                            governor_candidates.insert(index, [key_counter,incumbent,state,running])
                            key_counter+=1
                        

        # Process report data
        container = spread_soup.find('div', attrs={'id':'sheets-viewport'})
        table = container.find('div', attrs={'id':'1284173647'})
        table_rows = table.find_all('tr')
        index = 0
        for row in table_rows:
            texts = row.find_all('td')
            spreadsheet_governor.insert(index, [])
            for text in texts:
                if (text.getText() != ''):
                        spreadsheet_governor[index].append(text.getText())
            index+=1

    
def dataframe_to_csv(data_frame, file_name):
    data_frame.to_csv(file_name, index=False)
    print("Data Frame Compiled")

# Run scraping algorithms:
scraper(HOUSE_FILE_NAME, HOUSE_SOUP, SPREADSHEET_SOUP)
scraper(SENATE_FILE_NAME, SENATE_SOUP, SPREADSHEET_SOUP)
scraper(GOVERNER_FILE_NAME, GOVERNER_SOUP, SPREADSHEET_SOUP)

def remove_empty_arrays(array):
    return [subarray for subarray in array if subarray]

def remove_first_entry_2d(array_2d):
    if len(array_2d) > 0:
        # Use slicing to remove the first entry (row) of the 2D array
        return array_2d[1:]
    else:
        # Handle cases where the 2D array is empty
        return array_2d

def extract_first_names(array):
    sub = []
    for subarray in array:
        if subarray:  # Check if the subarray is not empty
            first_entry = subarray[0]
            sub.append(first_entry)
    return sub

# Array Cleanup
retiring_house = remove_empty_arrays(retiring_house)
retiring_h = extract_first_names(retiring_house)

running_senate = remove_empty_arrays(running_senate)
running_s = extract_first_names(running_senate)

other_office = remove_empty_arrays(other_office)
other_o = extract_first_names(other_office)

retiring_senate = remove_empty_arrays(retiring_senate)
retiring_s = extract_first_names(retiring_senate)

running_governor = remove_empty_arrays(running_governor)
running_g = extract_first_names(running_governor)

spreadsheet_house = remove_empty_arrays(spreadsheet_house)
spreadsheet_house = remove_first_entry_2d(spreadsheet_house)

spreadsheet_senate = remove_empty_arrays(spreadsheet_senate)
spreadsheet_senate = remove_first_entry_2d(spreadsheet_senate)

spreadsheet_governor = remove_empty_arrays(spreadsheet_governor)
spreadsheet_governor = remove_first_entry_2d(spreadsheet_governor)

house_candidates = remove_empty_arrays(house_candidates)
senate_candidates = remove_empty_arrays(senate_candidates)
governor_candidates = remove_empty_arrays(governor_candidates)

key_counter = 0

def house_data_processing(target_2d_array, source_2d_array, normal_array, normal_array2, normal_array3, key_counter):
    for source_row in source_2d_array:
        # Extract the name from the source row
        name = source_row[0]
        source_row.insert(0, key_counter)
        key_counter+=1
        names_to_remove = []
        # Check if the name is in the normal array
        if name in normal_array:
            # Add the indicator to the source row
            source_row.append("Yes")
            names_to_remove.append(name)
        else:
            source_row.append("No")

        # Check if the name is in the normal array
        if name in normal_array2:
            # Add the indicator to the source row
            source_row.append("Yes")
            names_to_remove.append(name)
        else:
            source_row.append("No")

        # Check if the name is in the normal array
        if name in normal_array3:
            # Add the indicator to the source row
            source_row.append("Yes")
            names_to_remove.append(name)
        else:
            source_row.append("No")

        # Add the source row to the target 2D array
        target_2d_array.append(source_row)

    for name in names_to_remove:
        normal_array.remove(name)
        normal_array2.remove(name)
        normal_array3.remove(name)
    
    return key_counter

def process_and_add_data(array1, array2, array3, normal_array1, normal_array2, normal_array3, target_array, key_counter):
    for subarray1 in array1:
        name1 = subarray1[0]
        if name1 in normal_array1:
            target_array.append([key_counter, name1, subarray1[1], subarray1[2], 'N/A', 'N/A', 'Yes', 'No', 'No'])
            key_counter += 1

    for subarray2 in array2:
        name2 = subarray2[0]
        if name2 in normal_array2:
            target_array.append([key_counter, name2, subarray2[1], subarray2[2], 'N/A', 'N/A', 'No', 'Yes', 'No'])
            key_counter += 1

    for subarray3 in array3:
        name3 = subarray3[0]
        if name3 in normal_array3:
            target_array.append([key_counter, name3, subarray3[1], subarray3[2], 'N/A', 'N/A', 'No', 'No', 'Yes'])
            key_counter += 1

def process_data(target_array, input_array, normal_array1, normal_array2, key_counter):
    key_counter = 0
    # Iterate through the input 2D array
    for subarray in input_array:
        state = subarray[0]  # First entry is the state
        names = subarray[1:]  # Rest of the entries are names

        # Iterate through the names
        for name in names:
            # Check if the name is in normal_array1 or normal_array2
            if name in normal_array1 or name in normal_array2:
                # Remove the name from normal_array1 and normal_array2 if present
                if name in normal_array1:
                    normal_array1.remove(name)
                    # Add a subarray to the target array with the state and name
                    target_array.append([key_counter, name, state, "Yes", "No"])
                if name in normal_array2:
                    normal_array2.remove(name)
                    # Add a subarray to the target array with the state and name
                    target_array.append([key_counter, name, state, "No", "Yes"])
            else:
                # Add a subarray to the target array with the state and name
                target_array.append([key_counter, name, state, "No", "No"])
            key_counter+=1
    return key_counter

def process_and_add_data2(array1, array2, normal_array1, normal_array2, target_array, key_counter):
    for subarray1 in array1:
        name1 = subarray1[0]
        if name1 in normal_array1:
            target_array.append([key_counter, name1, subarray1[1], 'Yes', 'No'])
            key_counter += 1

    for subarray2 in array2:
        name2 = subarray2[0]
        if name2 in normal_array2:
            target_array.append([key_counter, name2, subarray2[1], 'No', 'Yes'])
            key_counter += 1

# Cooke and sabato processing:
def spreadsheet_process(house,spreadsheet,dicty):
    for line in spreadsheet:
        key = line[0]
        cook = line[1]
        inside = line[2]
        sabato = line[3]

        if key in dicty and dicty[key] is not None:
            district = dicty[key]
            for person in house:
                if district in person:
                    person.append(cook)
                    person.append(inside)
                    person.append(sabato)

def spreadsheet_process2(govorsen,spreadsheet):
    for line in spreadsheet:
        state = line[0]
        cook = line[1]
        inside = line[2]
        sabato = line[3]
        for person in govorsen:
            if state in person:
                person.append(cook)
                person.append(inside)
                person.append(sabato)
            
def pad_2d_arrays(arr1, arr2, arr3):
    # Define the expected lengths for each 2D array
    expected_lengths = [12, 8, 7]  # You can customize these values

    # Iterate through each subarray in the three arrays
    for subarray in arr1:
        current_length = len(subarray)

        # Calculate the number of blank spaces needed to pad the subarray
        spaces_to_add = expected_lengths[0] - current_length

        # Append the required number of blank spaces to the subarray
        subarray.extend(['N/A'] * spaces_to_add)

    # Iterate through each subarray in the three arrays
    for subarray in arr2:
        current_length = len(subarray)

        # Calculate the number of blank spaces needed to pad the subarray
        spaces_to_add = expected_lengths[1] - current_length

        # Append the required number of blank spaces to the subarray
        subarray.extend(['N/A'] * spaces_to_add)

    # Iterate through each subarray in the three arrays
    for subarray in arr3:
        current_length = len(subarray)

        # Calculate the number of blank spaces needed to pad the subarray
        spaces_to_add = expected_lengths[2] - current_length

        # Append the required number of blank spaces to the subarray
        subarray.extend(['N/A'] * spaces_to_add)

    return arr1, arr2, arr3

# House Data Processing - add house candidates data to house, but for each candidate check if the candidate is retiring, seeking other office or running for senate and fill boxes accorindly
key_counter = house_data_processing(house, house_candidates, retiring_h, other_o, running_s, key_counter)
process_and_add_data(retiring_house, other_office, running_senate, retiring_h, other_o, running_s, house, key_counter)

# Senate Data Processing
key_counter = process_data(senate, senate_candidates, retiring_s, running_g, key_counter)
process_and_add_data2(retiring_senate, running_governor, retiring_s, running_g, senate, key_counter)

# Governer Data Processing
governers = governor_candidates

spreadsheet_process(house,spreadsheet_house,us_house_dict)
spreadsheet_process2(senate,spreadsheet_senate)
spreadsheet_process2(governers,spreadsheet_governor)
pad_2d_arrays(house, senate, governers)

# Add array to data frame and convert to CSV
for item in house:
    dataframe_entry_point = len(HOUSE_DATA_FRAME) + 1
    HOUSE_DATA_FRAME.loc[dataframe_entry_point] = item
for item in senate:
    dataframe_entry_point = len(SENATE_DATA_FRAME) + 1
    SENATE_DATA_FRAME.loc[dataframe_entry_point] = item
for item in governers:
    dataframe_entry_point = len(GOVERNER_DATA_FRAME) + 1
    GOVERNER_DATA_FRAME.loc[dataframe_entry_point] = item

dataframe_to_csv(HOUSE_DATA_FRAME, HOUSE_FILE_NAME)
dataframe_to_csv(SENATE_DATA_FRAME, SENATE_FILE_NAME)
dataframe_to_csv(GOVERNER_DATA_FRAME, GOVERNER_FILE_NAME)