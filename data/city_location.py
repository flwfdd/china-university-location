#根据高校列表生成城市地址列表
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

with open("china_mainland_universities.json","r",encoding="utf-8") as f:
    dic=json.loads(f.read())

out={}
for (ind,i) in enumerate(dic):
    out[i]=get_location(i)
    print(ind,i)
    time.sleep(1)

with open("city_location.json","w",encoding="utf-8") as f:
    f.write(json.dumps(out,ensure_ascii=False))
