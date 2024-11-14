import platform
import subprocess
import requests
import ctypes
import json
import asyncio
import discord
import os
import time
from threading import *

def menu():
    os.chdir(os.path.dirname(__file__))
    try:
        # Define the list of ASCII art files
        ascii_files = ["docAscii.txt", "docAscii2.txt", "docAscii3.txt", "docAscii4.txt"]

        # Set the console color to green on black
        os.system('color 02')

        # Animate the ASCII art
        for file in ascii_files:
            # Clear the console
            os.system('cls')
            # Open the current ASCII art file
            with open(file, encoding="utf-8") as f:
                # Print the current frame
                print("\033[92m" + f.read() + "\033[0m")
            # Print the menu options
            print("\033[93m" + "By ☠ Defender Of Christ ☦" + "\033[0m")
            
            print("Select an option:")
            print("[1] auto disconnect")
            print("[2] auto server mute")
            print("[3] auto server deafen")
            print("[4] auto moderation activate")
            print("[5] forced nickname")
            print("[0] Exit the Program")
            # Wait for a short time
            time.sleep(0.4)

        # Reset the console color to default
        os.system('color')

    except FileNotFoundError:
        print("Error: One or more ASCII art files not found.")
        print(os.listdir())




menu()
option = int(input("Enter your option: "))
def clearWindows():
    os.system('cls')
def clearLinux():
    os.system('clear')

def get_token():
    script_dir = os.path.dirname(__file__)
    config_file = os.path.join(script_dir, 'config.json')
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        token = config.get('token')
        if token:
            return token
        else:
            print("No token found in config.json file")
            exit()
    except FileNotFoundError:
        print("config.json file not found")
        exit()
    except json.JSONDecodeError:
        print("config.json file is not valid JSON")
        exit()

client = discord.Client()
token = get_token()


while option != 0: 
    if option == 1:
        #run the auto disconnecter
        userid = int(input("User ID: "))

        @client.event
        async def on_ready():
            os.system("cls")
            print(f"hey {client.user.name}, auto disconnected is ready")

        @client.event
        async def on_guild_available(guild):
            member = guild.get_member(userid)
            if member:
                voice_state = member.voice
                if voice_state and voice_state.channel:
                    print(f"{member.display_name} is already connected to voice channel {voice_state.channel.name}")
                    # You can move them to None if needed
                    await member.move_to(None)
                    print(f"{member.display_name} was automatically disconnected from voice chat. HAIL CHRIST CHRIST IS KING")

        @client.event
        async def on_voice_state_update(member, before, after):
            
            if member.id == userid and after.channel:
                await member.move_to(None)
                print(f'{member.display_name} was automatically disconnected from voice chat. HAIL CHRIST CHRIST IS KING')

        client.run(token, bot=False)
    elif option == 2:
        #run the auto server muter
        userid = int(input("User ID: "))

        @client.event
        async def on_ready():
            os.system("cls")
            print(f"hey {client.user.name}, auto muter is ready")

        @client.event
        async def on_voice_state_update(member, before, after):
            if member.id == userid and before.mute and not after.mute:
                await member.edit(mute=True)
                print(f'{member.display_name} was automatically muted in voice chat. HAIL CHRIST CHRIST IS KING')

        client.run(token, bot=False)
    elif option == 3:
        #run the auto server deafener
        userid = int(input("User ID: "))

        @client.event
        async def on_ready():
            os.system("cls")
            print(f"hey {client.user.name}, auto deafener is ready")

        @client.event
        async def on_voice_state_update(member, before, after):
            if member.id == userid and before.deafen and not after.deafen:
                await member.edit(deafen=True)
                print(f'{member.display_name} was automatically deafened in voice chat. HAIL CHRIST CHRIST IS KING')

        client.run(token, bot=False)
    elif option == 4:
        #run the auto moderator
        userid = int(input("User ID: "))

        @client.event
        async def on_ready():
            os.system("cls")
            print(f"hey {client.user.name}, auto mods are ready")

        @client.event
        async def on_guild_available(guild):
            member = guild.get_member(userid)
            if member:
                voice_state = member.voice
                if voice_state and voice_state.channel:
                    print(f"{member.display_name} is already connected to voice channel {voice_state.channel.name}")
                    # You can move them to None if needed
                    await member.move_to(None)
                    print(f"{member.display_name} was automatically disconnected from voice chat. HAIL CHRIST CHRIST IS KING")

        @client.event
        async def on_voice_state_update(member, before, after):
            if member.id == userid:
                if after.channel:
                    await member.move_to(None)
                    print(f'{member.display_name} was automatically disconnected from voice chat. HAIL CHRIST CHRIST IS KING')
                if before.mute and not after.mute:
                    await member.edit(mute=True)
                    print(f'{member.display_name} was automatically muted in voice chat. HAIL CHRIST CHRIST IS KING')
                if before.deafen and not after.deafen:
                    await member.edit(deafen=True)
                    print(f'{member.display_name} was automatically deafened in voice chat. HAIL CHRIST CHRIST IS KING')

        client.run(token, bot=False)
    elif option == 5:
        #run the forced nicknamme
        userid = int(input("User ID: "))
        customName = input("Custom nickname: ")
        serverid = int(input("Server ID: "))
        @client.event
        async def on_ready():
            os.system("cls")  # Clear console (Windows)
            print(f"Hey {client.user.name}, auto nicknamer is ready")
            
            guild = client.get_guild(serverid)
            if guild is None:
                print(f"Guild with ID {serverid} not found.")
                return
            
            try:
                member = await guild.fetch_member(userid)
            except discord.NotFound:
                print(f"Member with ID {userid} not found in server {serverid}.")
                return
            except discord.HTTPException as e:
                print(f"Error fetching member: {e}")
                return
            await change_nickname(member, customName)
        async def change_nickname(member, customName):
            try:
                await member.edit(nick=customName)
                print(f"Nickname for {member} has been forcefully updated to '{customName}'.")
            except discord.Forbidden:
                print(f"Failed to change nickname for {member}, insufficient permissions.")
            except discord.HTTPException as e:
                print(f"Error while updating nickname for {member}: {e}")
            while True:
                await client.wait_until_ready()
                guild = client.get_guild(serverid)
                try:
                    member = await guild.fetch_member(userid)  
                    if member.nick != customName:
                        await change_nickname(member, customName)
                except discord.NotFound:
                    print(f"Member with ID {userid} not found in server {serverid}.")
                    return
                await asyncio.sleep(1)  
        client.run(token, bot=False)
    else:
        print("Invalid option")




    print()
    menu()
    option = int(input("Enter your option: "))


print("Thanks for using Network Fixer, Christ is King!")