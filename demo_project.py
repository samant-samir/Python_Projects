import requests
import csv
import json

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = json.loads(response.text)

def flattenjson(b, delim):
    val = {}
    for i in b.keys():
        if isinstance( b[i], dict ):
            get = flattenjson( b[i], delim )
            for j in get.keys():
                val[ i + delim + j ] = get[j]
        else:
            val[i] = b[i]
    return val


users = list(map( lambda x: flattenjson( x, "_" ), users ))
columns = [ x for row in users for x in row.keys() ]
columns = list(columns)

print(json.dumps(users, indent=2))

filename = "demo.csv"

with open(filename, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(users)