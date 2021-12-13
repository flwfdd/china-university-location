#爬大学
import json
import requests
import time

ak=""
url="http://api.map.baidu.com/place/v2/search?query={}&region=全国&output=json&ak="+ak

#传入名称 返回[纬度,经度]
def get_location(name):
    try:
        r=requests.get(url.format(name))
        loc=json.loads(r.text)['results'][0]['location']
        return [loc['lat'],loc['lng']]
    except:
        print("ERR: ",name)
        return []

with open("university_location.json","r",encoding="utf-8") as f:
    dic=json.loads(f.read())

for (ind,i) in enumerate(dic):
    #if ind<1700: continue
    #if ind>1800: break
    if len(dic[i])>0: continue
    dic[i]=get_location(i)
    print(ind,i)
    time.sleep(1)

with open("university_location.json","w",encoding="utf-8") as f:
    f.write(json.dumps(dic,ensure_ascii=False))
