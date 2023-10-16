# Define imports
import pandas as pd
import requests
from bs4 import BeautifulSoup

## Create Data Frame and Collection Structure
house_column_name = ['key','Name']
house_data_frame = pd.DataFrame(columns=house_column_name)
house_file_name = 'house_data.csv'

senate_column_name = ['key','Name']
senate_data_frame = pd.DataFrame(columns=senate_column_name)
senate_file_name = 'senate_data.csv'

governer_column_name = ['key','Name']
governer_data_frame = pd.DataFrame(columns=governer_column_name)
governer_file_name = 'governer_data.csv'

house_data = 'https://ballotpedia.org/United_States_House_of_Representatives_elections/'
senate_data = 'https://ballotpedia.org/United_States_Senate_elections/'
governer_data = 'https://ballotpedia.org/Gubernatorial_elections/'

house_page_content = requests.get(house_data)
senate_page_content = requests.get(senate_data)
governer_page_content = requests.get(governer_data)

