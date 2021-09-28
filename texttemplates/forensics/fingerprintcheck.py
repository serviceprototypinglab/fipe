keys = {}

f = open("fingerprint.keys")
for line in f:
    line = line[:-1]
    k, v = line.split(",")
    keys[k] = v

f = open("fingerprint.out")
s = f.read()
f.close()

for k, v in keys.items():
    if v in s:
        print("=> magic", k, "with length", len(v), "found")
