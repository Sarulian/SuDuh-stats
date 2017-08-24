import requests
import config
import time
import pandas as pd
import json


if __name__ == "__main__":

	summoner_name = "troze"

	matchlist = requests.get(config.api_base + "match/v3/matchlists/by-account/" + config.summoner_ids[summoner_name] + "?api_key=" + config.key).json()["matches"]

	prematch = requests.get(config.api_base + "match/v3/matches/" + str(matchlist[0]["gameId"]) + "?api_key=" + config.key).json()

	part_id = 0
	for player_info in prematch["participantIdentities"]:
		print("{0}: {1}".format(player_info["participantId"], player_info["player"]["summonerName"]))
		if player_info["player"]["summonerName"].lower() == summoner_name.lower():
			part_id = str(player_info["participantId"])

	match = requests.get(config.api_base + "match/v3/timelines/by-match/" + str(matchlist[1]["gameId"]) + "?api_key=" + config.key).json()

	# print(matchlist[0]["gameId"])

	frames = match["frames"]
	locations = []

	for frame in frames:
		try:
			print(frame["timestamp"])
			print(frame["participantFrames"][part_id]["position"])
			locations.append((frame["participantFrames"][part_id]["position"]["x"], frame["participantFrames"][part_id]["position"]["x"]))
		except KeyError:
			pass

	for frame in frames:
		for event in frame["events"]:
			try:
				if event["type"] == "WARD_PLACED":
					print(event)
			except KeyError:
				pass
			
