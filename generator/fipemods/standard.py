import random
import io
import functools

def maketask(points):
    t = io.StringIO()
    s = io.StringIO()

    printt = functools.partial(print, file=t)
    prints = functools.partial(print, file=s)

    if points != 2:
        raise Exception("This task only works for a fixed allocation of 2 points.")

    printt("This is a standard task. Give an answer A to question Q.")
    printt()

    printt("Q: Explain how when Riot Games approached investors to fund the development of League of Legends, publishers were baffled by the game's free-to-play business model?")
    printt()

    prints("As they refined League of Legends' initial creation, they pitched investors a video game company rooted in e-commerce. Merill said that they approached publishers who were baffled by the game's lack of a single-player mode and free-to-play business model.")

    entropy = 0

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
