import requests
import config


while 1:
	summoner_name = input("Enter a summoner name: ")
	print("Requesting...")
	summoner_json = requests.get(config.api_base + "summoner/v3/summoners/by-name/" + summoner_name + "?api_key=" + config.key).json()
	acc_id = summoner_json["accountId"]
	print("accountId = " + str(acc_id))