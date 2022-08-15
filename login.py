import json
import os
import random
import time

path = 'players' #player data in this folder
if not os.path.exists(path):
  os.makedirs(path)

def login():
  question = input("Do you have an account y/n ")
  if question.lower() == 'n':
    signup()
  elif question.lower() == 'y':
    print("Please Enter you account information:\n")
    username = input("Username: ")
    password = input("Password: ")

    try:
      with open(os.path.join(path,username + ".json"), "r") as game:
        info = json.load(game)
      if info["username"] == username and info["password"] == password:
        print("Welcome to your game account", username.title() + "!\n")
        

        #saves current file
        with open("current_player.json","w") as file:
          json.dump(info, file)
          
      else:
        print("Incorrect username or password")
        login()
    except FileNotFoundError:
      print("We cannot find that account\nPlease try again")
      login()
      
    
  else:
    print("invalid choice")
    login()


def signup():
  print("Welcome to the game! Sign up for an account!")
  username = input("Please select a username ")
  password = input("Please choose a password ")

  data = {}
  data["username"] = username
  data["password"] = password
  data["progress"] = 0
  data["health"] = 100
  data["items"] = []
  data["credit"] = 0
  data["start_time"] = time.time()
  data["last_login"] = time.time()

  with open(os.path.join(path, username + ".json"),"w") as infile:
    data = json.dump(data,infile)

  print('Thanks for signing up, now you can login')

  login()
  
  
  