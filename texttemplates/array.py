import random
import sys

student = None
if len(sys.argv) == 2:
    student = sys.argv[1]

x = [9, 12, 18]

for i in range(random.randrange(5, 12)):
    z = random.randrange(25)
    if z % 3 == 0:
        continue
    x.append(z)

x = list(set(x))
x = sorted(x)

if student:
    f = open("testedmethods.subst.py")
    s = f.read()
    f.close()

    array = str(x)
    s = s.replace("%ARRAY%", array)

    f = open("testedmethods.subst.2.py", "w")
    print(s, file=f)
    f.close()

    f = open("testedmethods.csv", "a")
    print(f"{student},{array}", file=f)
    f.close()
else:
    print(x)
