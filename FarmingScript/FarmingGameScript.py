## ==========================================
## Project: Farming Game
## Author: Meakz
## Purpose: Farm and stuff
## ------------------------------------------
## Version: 1.0
## Created: 23/10/2026
## ==========================================

# Imports

import time
import os
import random
import pygame

# Variables For Pygame Sound

pygame.mixer.init()
Start_game_Sound = pygame.mixer.Sound("FarmStartUp.wav")

# Variables

Level = 0
total_harvests = 0
farm_count = 1
Cash_Money = 1
money_earned = 1
Farm_Per_Second = 0.10
harvest = 0
sell_multiplier = 1

# Definitions


def farm_crops():
    global harvest, total_harvests
    time.sleep(1)
    os.system("cls")
    time.sleep(2)
    print("=========================================")
    print("===========| Farming Crops! |============")
    print("===========||||||||||||||||||============")
    print("=========================================")
    print(f"           |      {harvest}        |            ")
    print("=========================================")
    time.sleep(2)
    harvest += Farm_Per_Second
    os.system("cls")
    time.sleep(2)
    print("=========================================")
    print("===========| Farming Crops! |============")
    print("===========||||||||||||||||||============")
    print("=========================================")
    print(f"           |      {harvest}        |            ")
    print("=========================================")
    time.sleep(2)
    harvest += Farm_Per_Second
    os.system("cls")
    time.sleep(2)
    print("=========================================")
    print("===========| Farming Crops! |============")
    print("===========||||||||||||||||||============")
    print("=========================================")
    print(f"           |      {harvest}        |            ")
    print("=========================================")
    time.sleep(2)
    harvest += Farm_Per_Second
    os.system("cls")
    time.sleep(2)
    print("=========================================")
    print("===========| Farming Crops! |============")
    print("===========||||||||||||||||||============")
    print("=========================================")
    print(f"           |      {harvest}        |            ")
    print("=========================================")
    time.sleep(2)
    harvest += Farm_Per_Second
    os.system("cls")
    time.sleep(2)
    print("=========================================")
    print("===========| Farming Crops! |============")
    print("===========||||||||||||||||||============")
    print("=========================================")
    print(f"           |      {harvest}        |            ")
    print("=========================================")
    time.sleep(3)
    os.system("cls")
    print("Done Harvesting!")
    time.sleep(1)
    total_harvests += Farm_Per_Second
    os.system("cls")
    game_screen()


def start_game_question_mark():
    global choice_of_GQM
    print("Hey, Ready to Start Farming? Click Enter to Play!")
    choice_of_GQM = input("")
    if choice_of_GQM == "":
        os.system("cls")
        time.sleep(2)
        Start_game_Sound.play()
        print("Welcome! Starting Game.")
        time.sleep(3)
        os.system("cls")
        time.sleep(0.5)
        print("Starting game..")
        time.sleep(1)
        os.system("cls")
        time.sleep(0.5)
        print("Starting game...")
        time.sleep(1)
        os.system("cls")
        time.sleep(0.5)
        game_screen()
        
    elif choice_of_GQM == "n":
        os.system("cls")
        print("Restarting Question!")
        time.sleep(1)
        start_game_question_mark()
        
    else:
        os.system("cls")
        time.sleep(1)
        start_game_question_mark()
        
def game_screen():
    global choice_game_screen,Farm_Per_Second, harvest, are_you_sure_sell, Cash_Money
    print("1. Farm My Crops.")
    print("2. Check Some Values.")
    print("3. Sell Harvest")
    print("4. Exit.")
    choice_game_screen = input(">> ")
    
    if choice_game_screen == "1":
        print("starting farm gui!")
        time.sleep(2)
        os.system("cls")
        farm_crops()
        
    elif choice_game_screen == "2":
        time.sleep(1)
        os.system("cls")
        time.sleep(2)
        print(f"Farm Per Second: {Farm_Per_Second}")
        print(f"Harvest: {harvest}")
        print(f"Cash: {Cash_Money}")
        input("Click Enter to go Back!")
        time.sleep(2)
        os.system("cls")
        game_screen()
        
    elif choice_game_screen == "3":
        print("Checking Harvest Price")

        money_earned = harvest * sell_multiplier

        print(f"Are you sure you want to sell {harvest} Harvests for ${money_earned}? (y/n)")
        are_you_sure_sell = input(">> ").lower()

        if are_you_sure_sell == "y":
            Cash_Money += money_earned
            harvest = 0

            print(f"Successfully sold harvests for ${money_earned}!")
            time.sleep(2)
            os.system("cls")
            time.sleep(2)
            game_screen()
            
        else:
            time.sleep(2)
            os.system("cls")
            time.sleep(2)
            game_screen()
        
                
        
    elif choice_game_screen == "4":
        print("Are You Sure? This Will Fully Exit The Script! 'y/n'")
        are_you_sure = input(">> ")
        
        if are_you_sure == "y":
            os.system("cls")
            exit()
            
        elif are_you_sure == "n":
            os.system("cls")
            time.sleep(1)
            start_game_question_mark() 
            
        else:
            print("Invalid Input")
            time.sleep(2)
            os.system("cls")
            game_screen()
            
            
# Game Code 

os.system("cls")
time.sleep(1)
start_game_question_mark()