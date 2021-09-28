import re
import random
import string
import sys

student = sys.argv[1]

f = open("testedmethods.subst.2.py")
s = f.read()
f.close()

naming = {}

lines = s.split("\n")
for idx, line in enumerate(lines):
    r = "\{%(\w+)%(?::(\w+))?\}"
    ms = re.findall(r, line)
    if ms:
        for m in ms:
            #print("###", line, m, naming)
            instr = m[0]
            dt = m[1]
            if dt:
                val = ""
                if dt == "DIGIT":
                    val = str(random.choice([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, "\"Error\"", "\"Fehler\"", "\"Invalid\"", "\"Falsch\"", "\"Fail\""]))
                elif dt == "LETTER":
                    val = random.choice([l for l in string.ascii_lowercase if l != "k"])
                naming[instr] = val
            else:
                val = naming[instr]
            line = re.sub(r, val, line, count=1)
            lines[idx] = line
s = "\n".join(lines)

f = open("testedmethods.subst.3.py", "w")
f.write(s)
f.close()

f = open("naming.csv", "a")
print(f"{student},{naming}", file=f)
f.close()
