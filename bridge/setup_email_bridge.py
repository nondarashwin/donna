import json
import sys

print(sys.argv[1])
data = sys.argv[1]
print(data)
with open("files/email.json", "w") as outfile:
    outfile.write(data)
