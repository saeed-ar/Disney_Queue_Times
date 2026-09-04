"""
Pyhton Script to see all the queue times at disney 
"""
import requests
from datetime import datetime, UTC
import pandas as pd 
import pathlib
import os

response = requests.get("https://queue-times.com/parks.json")
data = response.json()

#print(data)
#print("\n")
#print("\n")

filtered_data = [
    park 
    for company in data
    for park in company["parks"]
    if "Disney" in company["name"]
]

#print(filtered_data)


collect_disney_ids = [
   park["id"]
   for park in filtered_data
]

print(collect_disney_ids)


filtered_data1 = [
    park
    for company in data
    for park in company["parks"]
    if "Japan" in park["country"] 
]



def get_park_data_times(park_id):


    park_response = requests.get(f"https://queue-times.com/parks/{park_id}/queue_times.json")
    wait_times_data = park_response.json()
    return wait_times_data

#print(get_park_data_times(6))

def flatten_park_data(wait_times_data, park_id, park_name):

    result = []
    fetched_at_utc = datetime.now(UTC).isoformat()

    for land in wait_times_data["lands"]:
        for ride in land["rides"]:
            row = {
                "fetched_at_utc": fetched_at_utc,
                "park_id": park_id,
                "park_name": park_name,
                "land": land["name"], 
                "ride_id": ride["id"],
                "ride_name": ride["name"],
                "wait_time": ride["wait_time"],
                "is_open": ride["is_open"],
                "last_updated": ride["last_updated"]
            }
            result.append(row)
    return result

#magic_kingdom = (flatten_park_data(get_park_data_times(6), 6, "Magic Kingdom"))

##df = pd.DataFrame(magic_kingdom)
#file_exists = os.path.exists("MagicKingdom.csv")

#df.to_csv(
 #   "MagicKingdom.csv",
  #  mode="a" if file_exists else "w",
   # header = not file_exists,
    #index= False
#)
#print()

def main():


    DISNEY_PARKS = [
        {"id": 6, "name": "Magic Kingdom"},
        {"id": 5, "name": "EPCOT"},
        {"id": 7, "name": "Hollywood Studios"},
        {"id": 8, "name": "Animal Kingdom"},
        {"id": 16, "name": "Disneyland"},
        {"id": 17, "name": "California Adventure"}
    ]

    park_data = []

    for park in DISNEY_PARKS:
        try:
            park_data.extend(flatten_park_data(get_park_data_times(park["id"]), park["id"], park["name"]))
        except:
            print(f"Failed to retrieve data for {park['name']}")

    df = pd.DataFrame(park_data)
    file_exists = os.path.exists("all_park_data.csv")

    df.to_csv(
        "all_park_data.csv",
        mode="a" if file_exists else "w",
        header = not file_exists,
        index= False
    )

if __name__ == "__main__":
    main()
    
    





 