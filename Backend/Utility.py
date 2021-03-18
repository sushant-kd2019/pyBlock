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
    dic = obj.__dict__
    return json.dumps(dic, sort_keys=True)

def confirm_data(ar):
    for i in ar.keys():
        if ar[i] == "" and i != "message":
            return False
    return True

def hash_removed_obj(obj):
    dic = obj.__dict__
    dic.pop('block_hash')
    return hsh(json.dumps(dic,sort_keys=True))

def object_to_jsonstring_list(obj_list):
    tmp_list = []
    for i in obj_list:
        tmp_list.append(obj_dumps(i))
    return tmp_list



# class New:
#     def __init__(self):
#         self.a=12
#         self.b=45
#         self.block_hash=hsh(obj_dumps(self))
# ads= New()
# print(ads.block_hash==hash_removed_obj(ads))