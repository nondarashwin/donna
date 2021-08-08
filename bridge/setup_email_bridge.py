import json
import sys
import re


class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidEmail(Error):
    """Invalid Email Error"""
    pass


regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'


def check(email):
    if re.search(regex, email):
        return True
    else:
        return False


try:
    print(sys.argv[1])
    data = sys.argv[1]
    print(data)
    data1 = json.loads(data)
    a = data1.keys()
    print(a)
    if "from" in a and "password" in a:
        if not check(data1["from"]):
            raise InvalidEmail
        with open("files/email.json", "w") as outfile:
            outfile.write(data)
    else:
        raise InvalidEmail
except InvalidEmail:
    print("email not found")
    sys.exit(1)
except:
    print("failed to execute")
    sys.exit(1)
