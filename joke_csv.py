import requests
import random
from csv import writer
url="https://icanhazdadjoke.com/search"
x=input("Which joke you want to read :? ")
response= requests.get(url,headers={"Accept": "application/json"},params={"term":x})
data=response.json()
# print(data)
if data['total_jokes']==0:
    print(f"No joke available for {x}")
# else:
#     print(f"We have {data['total_jokes']} jokes with {x} .")
#     # y=random.choice(data['results'])
#     for x in data['results']:
#         print(x)
else:
    with open('joke.csv',"w") as file:
        csv_writer=writer(file)
        csv_writer.writerow(["JOKES"])
        for x in data['results']:
            csv_writer.writerow([x['joke']])
    

