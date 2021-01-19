import random
import io
import functools

def maketask(points):
    t = io.StringIO()
    s = io.StringIO()

    printt = functools.partial(print, file=t)
    prints = functools.partial(print, file=s)

    printt("Multiple Choice Example (true/false)")

    mps = (
        (True, "the 1352 Siege of Guines reignited the Hundred Years' War after six years of uneasy truce."),
        (False, "Hundred Years' War: The Siege of Rouen ended with Italian troops capturing the city from Turkish forces.")
    )

    if points > len(mps):
        raise Exception("No shuffle possible - not enough entropy for points.")

    mpx = list(mps)
    random.shuffle(mpx)
    mpx = mpx[:points]

    for i, mp in enumerate(mpx):
        printt()
        printt(f"{i + 1}. True[ ] False[ ] {mp[1]}")

    for i, mp in enumerate(mpx):
        prints(f"{i + 1} {mp[0]}!")

    entropy = len(mps) - len(mpx)

    t.seek(0)
    s.seek(0)
    return t.read(), s.read(), entropy

if __name__ == "__main__":
    t, s, e = maketask(2)
    print("== TASK ==")
    print(t)
    print("== SOLUTION ==")
    print(s)
    print("== ENTROPY ==")
    print(e)
