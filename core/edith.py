# Even Dead I'm The Hero :)
import sys
import json
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import time
import subprocess
import json
import requests
sys.path.append("../")
from what_i_can_do.joke import *
from what_i_can_do.search_wiki import *

class Edith:
    """ Yes, the name says it all, I do the background work :P"""

    def __init__(self):
        """ Some pre-reqs taken care here!! """

        # Initialise pyttsx3 engine for text to speech conversion
        self.speech_engine = pyttsx3.init()
        self.speech_engine.setProperty('voice', 'voices[0].id')
        self.speech_engine.setProperty('rate', 150)
        self.speech_engine.setProperty('volume', 1.0)

    def show_welcome_message(self):
        """ Welcome message for the user """
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            wish = "Good Morning"
        elif 12 <= hour < 18:
            wish = "Good Afternoon"
        else:
            wish = "Good Evening"
        command = "Hello {}, How may I help you?".format(wish)
        # self.speak(command)
        print(command)

    def get_skill(self, given_cmd):
        """ Checks whether the command specified by the user is already
            defined, if not notify the same to the user
        """
        f = open('../commands/command_mapping.json', )
        command_list = json.load(f)
        for key, val in command_list['commands'][0].items():
            if given_cmd in val:
                return (key if " " not in key
                        else key.replace(" ", "_"))

    def get_command_via_speech(self):
        """ Listens for user input from user"""

        # TODO: Fix `Cannot connect to server request channel` for linux
        #       platforms
        r = sr.Recognizer()
        sr.Microphone.list_microphone_names()

    def speak(self, text):
        """ Speaks the given text input"""
        self.speech_engine.say(text)
        self.speech_engine.runAndWait()
