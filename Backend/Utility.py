import json
import hashlib
import datetime


def get_now():
    return str(datetime.datetime.now())


def dump(code, msg):
    return json.dumps({"code": code, "msg": msg})


def hsh(obj):
    ans = hashlib.sha256(obj.encode()).hexdigest()
    return str(ans)


def obj_dumps(obj):
    return json.dumps(
        obj, default=lambda o: o.__dict__, sort_keys=True)


def confirm_data(ar):
    for i in ar.keys():
        if ar[i] == "" and i != "message":
            return False
    return True
