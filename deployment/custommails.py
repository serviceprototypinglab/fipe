import os
import sys

# Adjust domain to your student e-mail conventions
domain = "students.*.*"

if os.path.isdir("sep-mails"):
    print("Big mistake! The mail texts for this exam are already generated. If you want to override, do what you have to do.", file=sys.stderr)
    exit(1)
os.mkdir("sep-mails")

f = open("email.template")
template = f.read()

f = open("../final/students.out")

for line in f:
    line = line.strip()
    account, randaccount = line.split(",")

    text = template.replace("%RANDACCOUNT%", randaccount)

    fe = open(os.path.join("sep-mails", account + "@" + domain), "w")
    print(text, file=fe)
    fe.close()
