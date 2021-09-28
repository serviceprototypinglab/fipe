import random
import os
import shutil

for path in ("generated", "autosolutions"):
    if os.path.isdir(path):
        exit(f"*MUST* delete '{path}' folder manually")

for path in ("generated", "autosolutions"):
    os.makedirs(path, exist_ok=True)

for genfile in ("templater.csv", "simulationfussball.keys", "testedmethods.csv"):
    if os.path.isfile(genfile):
        os.unlink(genfile)

mapping = {}

f = open("students.in")
for student in f:
    student = student.strip()
    while True:
        genstr = random.randrange(10 ** 8, 10 ** 9)
        if not genstr in mapping.values():
            break
    mapping[student] = str(genstr)
f.close()

f = open("students.out", "w")
for student, genstr in mapping.items():
    print(">", student)
    print(f"{student},{genstr}", file=f)
    targetpdir = os.path.join("generated", genstr)
    targetdir = os.path.join(targetpdir, "sep-dateien")
    soldir = os.path.join("autosolutions", student)
    os.makedirs(targetdir, exist_ok=True)
    os.makedirs(soldir, exist_ok=True)

    os.system(f"python3 templater.py '{student}'")
    shutil.copyfile("selectivediff.subst.py", os.path.join(targetdir, "aufgabe2.py"))

    os.system("python3 templater-mp.py")
    shutil.copyfile("warmup.subst.py", os.path.join(targetdir, "aufgabe1.py"))
    shutil.copyfile("warmup.subst.json", os.path.join(soldir, "aufgabe1.json"))

    os.system(f"python3 fingerprint.py 'simulationfussball.q.py' 'simulationfussball.subst.py' 'simulationfussball.keys' '{student}'")
    shutil.copyfile("simulationfussball.subst.py", os.path.join(targetdir, "aufgabe5.py"))

    os.system("python3 dividepandas.py")
    shutil.copyfile("pandastask.subst.py", os.path.join(targetdir, "aufgabe4.py"))
    shutil.copyfile("pandastask.subst.json", os.path.join(soldir, "aufgabe4.json"))

    os.system(f"python3 fingerprint.py 'testedmethods.q.py' 'testedmethods.subst.py' 'testedmethods.keys' '{student}'")
    os.system(f"python3 array.py '{student}'")
    os.system(f"python3 templater-naming.py '{student}'")
    shutil.copyfile("testedmethods.subst.3.py", os.path.join(targetdir, "aufgabe3.py"))

    shutil.copy("sneaker.json", targetdir)

    pwd = os.getcwd()
    os.chdir(targetpdir)
    os.system("zip -rq sep-dateien.zip sep-dateien")
    shutil.rmtree("sep-dateien")
    os.chdir(pwd)
f.close()

shutil.move("templater.csv", "autosolutions")
shutil.move("testedmethods.csv", "autosolutions")
shutil.move("naming.csv", "autosolutions")
shutil.move("simulationfussball.keys", "autosolutions")
shutil.move("testedmethods.keys", "autosolutions")
shutil.move("students.out", "autosolutions")
