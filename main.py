import requests
import json

endpoint_url = 'https://api.spotify.com/v1/recommendations?'
access_token = "BQADQCgERW8pc5ITf8LMkoOstv4MO1o3KWFgc5CSaSW_eNondw0ce-tLI7Y-gF2r92rfe6l4UK33N5AbUdWHRtXji3rx2_c0Iu6-P0t4JznfW7svWbIdCRDaJ8cY0zdxGv9TubbvTx35nQukFQlztyLDQeZOQsH48Zt_O4cVzg9XrM_dSa4"
uris = []

#FILTERS
limit = 10 #number of songs
market = "US" #country
seed_genres = "edm" #genres
target_danceability = 0.8
seed_artists = "45eNHdiiabvmbp4erw26rg"

#QUERY FOR SONGS
query = f'{endpoint_url}limit={limit}&market={market}&seed_artists={seed_artists}&target_danceability={target_danceability}'

response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

json_response = response.json()
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

print(response)
