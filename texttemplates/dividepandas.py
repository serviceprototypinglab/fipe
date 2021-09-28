import random
import json

f = open("pandastask.q.py")
lines = f.read().splitlines()
f.close()

sect = None
numsect = None
sections = {}
sectoptions = {}
for line in lines:
    if line.startswith("%%"):
        sect = line.split(" ")[1]
        numsect = 0
        if sect in sections:
            numsect = len(sections[sect])
        sectoption = line.split(" ")[2]
        if not sect in sectoptions:
            sectoptions[sect] = []
        sectoptions[sect].append(sectoption)
    else:
        if not sect in sections:
            sections[sect] = []
            numsect = 0
        if len(sections[sect]) < numsect + 1:
            sections[sect].append([])
        #print(">", sect, numsect)
        sections[sect][numsect].append(line)

alloptions = []
f = open("pandastask.subst.py", "w")

for sect in sections:
    indices = list(range(len(sections[sect])))
    if sect != "ALL":
        letter = sect[0]
        num = int(sect[1])
        random.shuffle(indices)
        indices = indices[:num]

    for idx in indices:
        lines = sections[sect][idx]
        for line in lines:
            print(line, file=f)

        sectoption = sectoptions[sect][idx]
        alloptions.append(sectoption)

f.close()

f = open("pandastask.subst.json", "w")
json.dump(alloptions, f)
f.close()
