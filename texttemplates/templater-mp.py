import re
import random
import json

limit = 10

f = open("warmup.q.py")
s = f.read()
f.close()

ctr = 0
answers = {}
questions = {}

lines = s.split("\n")

numctr = 0
for idx, line in enumerate(lines):
    r = "Aussage X"
    m = re.findall(r, line)
    if m:
        numctr += 1

indices = list(range(1, numctr + 1))
random.shuffle(indices)
indices = [0] + indices
#!print("#### IDX", indices)

for idx, line in enumerate(lines):
    r = "Aussage X"
    m = re.findall(r, line)
    if m:
        ctr += 1
        repl = "Aussage " + str(indices[ctr])
        line = re.sub(r, repl, line)
    r = "bewertungX = (True|False)"
    m = re.findall(r, line)
    if m:
        answer = m[0]
        assess = "bewertung" + str(indices[ctr])
        #!print("#### =>", assess, "@", ctr)
        answers[assess] = eval(answer)
        repl = assess + " ="
        line = re.sub(r, repl, line)
    #lines[idx] = line
    questions[indices[ctr]] = questions.get(indices[ctr], []) + [line]

lines = []
selanswers = {}
for i in range(limit + 1):
    if i > 0:
        #j = "bewertung" + str(indices[i])
        k = "bewertung" + str(i)
        #!print("#### <= ", k)
        selanswers[k] = answers[k]
    rel = i
    #if i == 0:
    #    rel = indices[-1]
    for line in questions[rel]:
        lines.append(line)

s = "\n".join(lines)

f = open("warmup.subst.py", "w")
f.write(s)
f.close()

f = open("warmup.subst.json", "w")
json.dump(selanswers, f)
f.close()
