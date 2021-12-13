#整合地点信息
import json
import requests
import time

out={}
with open("country_location.json","r",encoding="utf-8") as f:
    out.update(json.loads(f.read()))

with open("city_location.json","r",encoding="utf-8") as f:
    out.update(json.loads(f.read()))

with open("university_location.json","r",encoding="utf-8") as f:
    out.update(json.loads(f.read()))

print(len(out))
with open("location.json","w",encoding="utf-8") as f:
    f.write(json.dumps(out,ensure_ascii=False))
