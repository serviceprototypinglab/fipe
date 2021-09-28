import re
import random
import sys

student = None
if len(sys.argv) == 2:
    student = sys.argv[1]

f = open("selectivediff.q.py")
s = f.read()
f.close()

vary = None

lines = s.split("\n")
for idx, line in enumerate(lines):
    r = "\{(\w+):(\w+)\}"
    m = re.findall(r, line)
    if m:
        #print("###", line, m)
        instr = m[0][0]
        repl = m[0][1]
        newrepl = []
        if instr == "VARY":
            for n in repl:
                newrepl.append(str(random.randrange(10)))
            repl = "".join(newrepl)
            vary = repl
            line = re.sub(r, repl, line)
        else:
            exit("Unknown substitution type!", instr)
        #print("->", line)
        lines[idx] = line
s = "\n".join(lines)

f = open("selectivediff.subst.py", "w")
f.write(s)
f.close()

if student:
    f = open("templater.csv", "a")
    print(f"{student},{vary}", file=f)
    f.close()
