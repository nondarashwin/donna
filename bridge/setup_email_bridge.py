import json
import sys


data = json.loads(sys.argv[1])
with open("email.json", "w") as outfile:
    outfile.write(data)
