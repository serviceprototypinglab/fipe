import random
import sys

fingerprint = ""
for i in range(12):
    f = random.choice(" \t")
    fingerprint += f

infile = "fingerprint.template"
outfile = "fingerprint.out"
magicfile = "fingerprint.keys"
student = "*"
if len(sys.argv) == 5:
    infile = sys.argv[1]
    outfile = sys.argv[2]
    magicfile = sys.argv[3]
    student = sys.argv[4]

f = open(infile)
s = f.read()
s = s.replace("%MAGIC%", fingerprint)
f.close()

f = open(outfile, "w")
print(s, file=f)
f.close()

f = open(magicfile, "a")
print(f"{student},{fingerprint}", file=f)
f.close()
