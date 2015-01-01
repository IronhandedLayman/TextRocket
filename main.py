#!/usr/bin/python

import random

# Constants
version = "0.2.0"

# functions
def init():
  print "Welcome to TextRocket version " + version
  print "---------------------"
  state = dict()
  state["ended"] = False
  state["ending"] = ""
  state["direction"] = "North"
  state["elevation"] = 0
  state["evolution"] = "Hatched"
  state["location"] = "Starting room"
  return state

def describe(state):
  print "You are facing " + state["direction"] + ". You are at elevation " + str(state["elevation"]) + " feet and are in the " + state["location"] + "."
  print "You are currently " + state["evolution"]

def read():
  return raw_input("> ")

def train(state):
  evolve_state = state["evolution"]
  if evolve_state == "Hatched":
    l = random.randint(0,20)
    r = random.randint(0,20)
    ans = raw_input("What is "+str(l)+" times "+str(r)+"?")
    try:
      if l*r == int(ans):
        print "YOU SUCCESSFULLY EVOLVED!"
        state["evolution"]="Adolescent"
      else:
        print "You are terrible at math! Try again."
    except:
      print "That's not a number! You're an IDIOT."
  else:
    print "You cannot evolve further."

def myEval(state, command):
  print "You wanted to " + command
  if command == "TRAIN":
    train(state)
    state["ended"] = False
  elif state["evolution"] == "Adolescent" and (command == "WIN" or command == "SUCCEED"):
    state["ended"] = True
    state["ending"] = "WIN"
  elif command == "CORRECT" or command == "sorta":
    state["ended"] = True
    state["ending"] = "DRAW"
  elif command == "DIE":
    print "Why did you want to KILL ME? LOSER."
    state["ended"] = True
    state["ending"] = "LOSE"
  elif command == "QUIT":
    state["ended"] = True
    state["ending"] = "LOSE"
  else:
    print "NOT FINISHED YET"
    state["ended"] = False

def ending(state):
  if state["ending"] == "WIN":
    print "You completed TextRocket!"
  elif state["ending"] == "DRAW":
    print "You kind of completed TextRocket."
  elif state["ending"] == "LOSE":
    print "YOU LOST"

# main
def loop():
  state = init()
  while not state["ended"]:
    describe(state)
    myEval(state,read())
  ending(state)

loop()
