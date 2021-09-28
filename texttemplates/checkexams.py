import glob
import importlib
import sys
import os
#import ast
import json
import pandas
import unittest

origsyspath = sys.path

def checkaufgabe4(m, student):
    f = open(os.path.join("autosolutions", student, "aufgabe4.json"))
    symbols = json.load(f)
    f.close()

    df = pandas.read_json(os.path.join("abgabe-lösungen", student, "sneaker.json"))

    score = 0
    for sym in symbols:
        if sym == "-":
            continue
        if sym in ("plot_plot", "plot_boxplot"):
            if os.path.isfile(os.path.join("abgabe-lösungen", student, sym + ".png")):
                score += 0 # Plots müssen manuell ausgewertet werden - aber Überprüfung auf 'falschen' Plot
                if os.path.isfile(sym + ".png"):
                    os.unlink(sym + ".png")
            else:
                print("! UNKLARHEIT bei", student, "Plot", sym)
            continue
        if sym in dir(m):
            score += 1
            if sym == "df":
                if m.df.equals(df):
                    score += 1
            elif sym == "df_black":
                df_black = df[df["color"] == "Black"]
                if m.df_black.equals(df_black):
                    score += 2
            elif sym == "df_blue":
                df_blue = df[df["color"] == "Blue"]
                if m.df_blue.equals(df_blue):
                    score += 2
            elif sym == "df_preis180":
                df_preis180 = df[df["price"] == 180]
                if m.df_preis180.equals(df_preis180):
                    score += 2
            elif sym == "df_preis110":
                df_preis110 = df[df["price"] == 110]
                if m.df_preis110.equals(df_preis110):
                    score += 2
            elif sym == "df_wander":
                df_wander = df[df["displayName"].str.endswith("Wanderschuh")]
                if m.df_wander.equals(df_wander):
                    score += 2
            elif sym == "df_lauf":
                df_lauf = df[df["displayName"].str.endswith("Laufschuh")]
                if m.df_lauf.equals(df_lauf):
                    score += 2

    return score

def checkaufgabe3(m, student):
    globals()["Testklasse"] = m.Testklasse
    res = unittest.main(testRunner=unittest.TextTestRunner(stream = open(os.devnull, "w")), exit=False).result
    score = res.testsRun - len(res.failures) - len(res.errors)
    return score * 3

def checkaufgabe2(m, student):
    print(m.fixpoint_array[5])

    c = m.ConvergenceCalculation()
    c.precalculate()
    c.calculate()
    c.validate()
    c.output()
    #print(round(c.result))

    return "läuft"

def checkaufgabe1(m, student):
    f = open(os.path.join("autosolutions", student, "aufgabe1.json"))
    answers = json.load(f)
    f.close()

    score = 0
    for i in range(10):
        assess = "bewertung" + str(i + 1)
        if assess in dir(m):
            expr = f"m.{assess}"
            try:
                #val = ast.literal_eval(expr)
                val = eval(expr)
            except:
                pass
            else:
                #print("ASSESS", assess, val)
                if assess in answers and val == answers[assess]:
                    score += 1
    return score

def cleanupmodule(m):
    for name in [n for n in m.__dict__ if not n.startswith("__")]:
        m.__dict__.__delitem__(name)

def runchecks(title, filename, checkfunc, df, quiet=False):
    if quiet:
        print(f"{title} (Ausgaben unterdrückt)")
    else:
        print(title)
    m = None

    pyfiles = glob.glob(f"abgabe-lösungen/*/{filename}.py")

    for pyfile in pyfiles:
        modpath = os.path.dirname(pyfile)
        student = os.path.basename(modpath)
        print(">", student)
        sys.path = origsyspath + [modpath]
        devnull = None
        origstdout = None
        if quiet:
            devnull = open(os.devnull, "w")
            origstdout = sys.stdout
            sys.stdout = devnull
        try:
            #importlib.invalidate_caches()
            if m:
                cleanupmodule(m)
                m = importlib.reload(m)
            else:
                m = importlib.import_module(filename)
        except:
            score = "Fehler"
        else:
            try:
                score = checkfunc(m, student)
            except Exception as e:
                print("!", e, file=sys.stderr)
                score = "Fehler"
        if quiet:
            devnull.close()
            sys.stdout = origstdout
        if type(score) == int:
            print(" =", score, "Punkte")
        else:
            print(" =>", score)

        df.loc[student, title] = score

def fillempty(df):
    students = glob.glob(f"abgabe-lösungen/*")
    for student in students:
        student = os.path.basename(student)
        if student.startswith("_") or student.startswith("."):
            continue
        for col in df.columns:
            fill = False
            try:
                df.loc[student, col]
            except:
                fill = True
            else:
                if pandas.isnull(df.loc[student, col]):
                    fill = True
            if fill:
                df.loc[student, col] = 0

df = pandas.DataFrame()
runchecks("Aufgabe 1", "aufgabe1", checkaufgabe1, df)
runchecks("Aufgabe 2", "aufgabe2", checkaufgabe2, df)
runchecks("Aufgabe 3", "aufgabe3", checkaufgabe3, df)
runchecks("Aufgabe 4 OHNE Plots", "aufgabe4", checkaufgabe4, df, quiet=True)
fillempty(df)
df.sort_index(inplace=True)
df.to_excel("results.xls")
print("Teilautomatisiertes Assessment in Datei results.xls abgelegt.")
