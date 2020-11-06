import requests

people = requests.get("http://api.open-notify.org/astros.json")

#print(people.text)

people_json  = people.json()
#print(people_json)

#To print the number of people in space
print("Number of people in space right now:",people_json['number'])
#To print the names of people in space using a for loop
for p in people_json['people']:
    print(p['name'])
