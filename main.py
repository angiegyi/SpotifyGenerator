import requests
import json

endpoint_url = 'https://api.spotify.com/v1/recommendations?'
access_token = "BQCi4MzZb5qxUH3YzfOQWsFcF_sB1bSyTCrN7digZ7xRokqtTasljUxWQw0kUcpoWU-PGkyowrdEEDRItycTSY_CivLb17X72X2_Wf_of9PsVN6GTyrs84124io2NNXwqpJ8j1HKAnmvJJRmTNPC_FKQQrypO0Ve0KSB6IRp1NorPJ4dg3s"
uris = []

#FILTERS
limit = 10 #number of songs
market = "US" #country
seed_genres = "edm" #genres
target_danceability = 0.8
seed_artists = "7lZauDnRoAC3kmaYae2opv,45eNHdiiabvmbp4erw26rg"

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

user_id = "datdemaciakid"
endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "Beep Boop",
          "description": "I beep booped to make this",
          "public": False # let's keep it between us - for now
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", "Authorization":"Bearer " + access_token})
endpoint_url = f"https://api.spotify.com/v1/playlists/5XvFNff1cEKOUUrUMyWpWu/tracks"

request_body = json.dumps({
          "uris" : uris
        })

response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", "Authorization":f"Bearer {access_token}"})
print(response.status_code)



print(response.status_code)