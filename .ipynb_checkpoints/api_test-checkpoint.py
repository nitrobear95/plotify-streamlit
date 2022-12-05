
import requests

url = "https://marvelstefan-skliarovv1.p.rapidapi.com/getSeriesByCharacter"

payload = "privateKey=%3CREQUIRED%3E&titleStartsWith=avengers&characterId=%3CREQUIRED%3E&publicKey=%3CREQUIRED%3E"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "1688bcf98dmsh0dde3eda4f0374ap15d984jsnbb0c2deccb48",
	"X-RapidAPI-Host": "Marvelstefan-skliarovV1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
