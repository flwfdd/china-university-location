# country with location from csv to json
import csv,json

loc={}
with open('countries.csv', 'r',encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row[0])==2:
            if row[1]=="":continue
            loc[row[0]]=[float(row[1]),float(row[2])]

out={}
with open('country_list.csv', 'r',encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] in loc:
            out[row[0]]=loc[row[1]]
        else:
            print("Can't find: ",row[0],row[1])


with open("country_list.json","w",encoding="utf-8") as f:
    f.write(json.dumps([i for i in out],ensure_ascii=False))

with open("country_location.json","w",encoding="utf-8") as f:
    f.write(json.dumps(out,ensure_ascii=False))
