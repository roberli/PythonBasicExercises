roberli = ""
f = open("sourcezbx", "r")
for i in f:
    roberli += "ZBX_" + i.upper()
print(roberli)