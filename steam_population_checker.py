#!/usr/bin/env python3

import requests
import notify2
import sys
import datetime
from time import sleep

notify2.init("Game Notifier")
# create Notification object 
n = notify2.Notification(None) 
  
# set urgency level 
n.set_urgency(notify2.URGENCY_NORMAL) 
  
# set timeout for a notification 
n.set_timeout(10000) 

def check_player_count(appId, threshold, api_key):

    header = {"Client-ID": api_key}
    
    
    game_name_url=f"https://store.steampowered.com/api/appdetails?appids={appId}"
    game_name = requests.get(game_name_url, headers=header)
    name = game_name.json()["608800"]["data"]["name"]    
    print(name)
    
    while True:
        if datetime.datetime.now().weekday() < 5:
            # if it's a weekday, only look between 5 and 9 pm
            if datetime.datetime.now().hour < 17 or datetime.datetime.now().hour > 21:
                sleep(600)
                continue
        else:
            # if it's a weekend, only look between 8am and 11pm
            if datetime.datetime.now().hour < 8 or datetime.datetime.now().hour > 23:
                sleep(600)
                continue
        
        
            
        sleep(300) #during the correct hours, check pop every 5 minutes
        game_players_url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?format=json&appid=' + appId
        game_players = requests.get(game_players_url, headers=header)
        count = game_players.json()['response']['player_count']
        print(f"Game name: {name}" + ", Player count: " + str(count))
        if count > threshold:
            
            n.update(name, f"{name} is active with {count} players")
            n.show()
            sleep(3600) # only send one positive notification per hour


if __name__ == '__main__':
    
    if len(sys.argv) < 4:
        print("Usage: python3 steam_population_checker.py [Steam Appid] [threshold] [api_key]")
        sys.exit(1)
    
    appId = sys.argv[1]
    threshold = int(sys.argv[2])
    api_key = sys.argv[3]
    
    
    check_player_count(appId, threshold, api_key)
