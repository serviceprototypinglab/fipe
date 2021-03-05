import os
import sys
import shutil
#import random

if os.path.isdir("sep-onserver"):
    print("Big mistake! This exam is already generated. If you want to override, do what you have to do.", file=sys.stderr)
    exit(1)
os.mkdir("sep-onserver")

students = {}
fs = open("../final/students.out")
for line in fs:
    account, randaccount = line.strip().split(",")
    students[account] = randaccount

html = open("deploy-folder/index.html.template").read()

for account in students:
    randaccount = students[account]

    source = os.path.join("..", "final", "students", randaccount)
    target = os.path.join("sep-onserver", randaccount)

    print(account, "→", target)

    os.mkdir(target)

    shutil.copyfile(os.path.join(source, f"{account}-sep.pdf"), os.path.join(target, f"{account}-sep.pdf"))

    fhtml = open(os.path.join(target, "index.html"), "w")
    htmltext = html.replace("%ACCOUNT%", account)
    print(htmltext, file=fhtml)
    fhtml.close()
