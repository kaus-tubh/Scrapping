import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from csv import reader
import time

response= requests.get("https://www.youtube.com/feed/trending")
soup=BeautifulSoup(response.text, "lxml")
print(soup)