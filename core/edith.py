# Even Dead I'm The Hero :)
import sys
import json

sys.path.append("../")
from what_i_can_do.joke import tell_me_a_joke


def get_skill(cmd):
    f = open('commands/command_mapping.json', )
    commad_list = json.load(f)

    for command in commad_list:
        print(command)
    if " " in cmd:
        return cmd.replace(" ", "_")
    else:
        return cmd

def show_welcome_message():
    print("Hey there, MAPA here!!! ['My Automated Personal Assistant] "
          "Just ask `hey mapa` to see the skills I have :)\n\n")