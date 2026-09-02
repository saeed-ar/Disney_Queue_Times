"""
Pyhton Script to see all the queue times at disney 
"""
import requests

response = requests.get("https://queue-times.com/parks.json")
data = response.json()

print(data)
print("\n")
print("\n")

filtered_data = [
    park 
    for company in data
    for park in company["parks"]
    if "Disney" in company["name"]
]

print(filtered_data)

filtered_data1 = [
    park
    for company in data
    for park in company["parks"]
    if "Japan" in park["country"] 
]

print(f"\n{filtered_data1}")