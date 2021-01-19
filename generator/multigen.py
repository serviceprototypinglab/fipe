import importlib
import random
import os
import sys

path = "tasksgen"

rans = []
ranom = 100000000

adminpath = os.path.join(path, "admin")
os.makedirs(adminpath, exist_ok=True)
fo = open(os.path.join(adminpath, "students.out"), "w")

mods = []
fm = open("multigen.conf")
for line in fm:
    modname, title, points = line.strip().split(",")
    points = int(points)
    mods.append((modname, title, points))

sys.path.append("fipemods")

f = open("students.in")
for student in f:
    identicalpoints = 0
    opoints = 0

    student = student.strip()
    print(student)

    while True:
        ran = str(random.randrange(ranom, 10 * ranom))
        if not ran in rans:
            rans.append(ran)
            break

    print(f"{student},{ran}", file=fo)

    xpath = os.path.join(path, ran)
    os.makedirs(xpath, exist_ok=True)

    smods = list(mods)
    random.shuffle(smods)

    for i, mod in enumerate(mods):
        modname, title, points = mod
        mod = importlib.import_module(modname)

        origdir = os.getcwd()
        os.chdir(xpath)
        t, s, e = mod.maketask(points)
        os.chdir(origdir)

        ft = open(os.path.join(xpath, f"{i+1}.txt"), "w")
        print(t, file=ft)
        ft.close()

        fs = open(os.path.join(adminpath, f"{student}.{i+1}.solution"), "w")
        print(s, file=fs)
        fs.close()

        opoints += points
        spoints = e * 2
        if spoints > points:
            spoints = points
        identicalpoints += points - spoints

    ft = open(os.path.join(xpath, "toc"), "w")
    for i, mod in enumerate(mods):
        modname, title, points = mod
        print(f"{i+1},{title},{points}", file=ft)
    ft.close()

fo.close()

pct = round(100 * identicalpoints / opoints, 1)
print("Statistics:")
print(f"{opoints} points total of which {identicalpoints} are identical ({pct}%)")
