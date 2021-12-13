import json

with open("china_mainland_universities.json","r",encoding="utf-8") as f:
    dic=json.loads(f.read());

out={}

for i in dic:
    out[i]=dic[i]['all']

with open("university_list.json","w",encoding="utf-8") as f:
    f.write(json.dumps(out,ensure_ascii=False))

l={}
for i in out:
    for j in out[i]:
        l[j]=[]

with open("university_location.json","w",encoding="utf-8") as f:
    f.write(json.dumps(l,ensure_ascii=False))
