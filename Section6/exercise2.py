import json

readfile = open('csv_file.txt', 'r')
data = [line.strip() for line in readfile.readlines()]
readfile.close()

alldata = []

for d in data:
    # alldata.append(d.split(','))
    d1 = d.split(',')
    alldata.append({"club": d1[0], "country": d1[1], "city": d1[2]})

file = open("json_file.txt", "w")

json.dump(alldata, file)

file.close()
