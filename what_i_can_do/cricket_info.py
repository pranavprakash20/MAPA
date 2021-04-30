from pycricbuzz import Cricbuzz
import json
c = Cricbuzz()
lscore = c.livescore("30330")
print(json.dumps(lscore, indent=4, sort_keys=True))