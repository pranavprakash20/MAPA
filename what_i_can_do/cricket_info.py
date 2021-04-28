from pycricbuzz import Cricbuzz

def get_match_score():
    c = Cricbuzz()
    print(c.matches())

get_match_score()