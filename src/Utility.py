import json
import hashlib
import datetime


def get_now():
    return str(datetime.datetime.now())

def dump(code,msg):
    return json.dumps({"code":code,"msg":msg})

def hsh(obj):
    ans = hashlib.sha256(obj.encode()).hexdigest()
    return str(ans)