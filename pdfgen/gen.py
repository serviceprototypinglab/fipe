import os
import sys
import random

def render(tasks, tasksdir, outputdir):
    pages = []

    for taskidx, task in enumerate(tasks):
        tasknum, tasktitle, points = task
        indir = None
        for searchpath in (tasksdir, outputdir):
            if os.path.isfile(os.path.join(searchpath, f"{tasknum}.txt")):
                taskfile = f"{tasknum}.txt"
                indir = searchpath
            elif os.path.isfile(os.path.join(searchpath, f"{tasknum}.tex")):
                taskfile = f"{tasknum}.tex"
                indir = searchpath
        taskpath = os.path.join(indir, taskfile)
        if taskfile.endswith(".txt"):
            print("Text-process", taskfile)
            f = open("template.tex")
            t = f.read()
            f = open(taskpath)
            text = f.read()

            #print("TEXT", text)
            if "!INCLUDE" in text:
                lines = text.split("\n")
                for i in range(len(lines)):
                    line = lines[i]
                    if line.startswith("!INCLUDE"):
                        includepath = line.split(" ")[1]
                        print("**", includepath)
                        fullincludepath = os.path.join(indir, includepath)
                        # scale=0.32\columnwidth - not "fair" as widths + heights of rendered graphs differ but we want all nodes to have constant size
                        lines[i] = "\\end{Verbatim}\n\\includegraphics[scale=0.5]{" + fullincludepath + "}\n\\begin{Verbatim}[breaklines=true]"
                text = "\n".join(lines)

            t = t.replace("%TASK%", text)
            t = t.replace("%TASKNUM%", str(taskidx))
            t = t.replace("%TASKTITLE%", tasktitle)
            gentex = os.path.join(outputdir, taskfile.replace(".txt", ".gentex"))
            f = open(gentex, "w")
            print(t, file=f)
            f.close()
            #pdflatex -interaction=nonstopmode template.tex >/dev/null
            ret = os.system(f"pdflatex -output-directory={outputdir} -interaction=nonstopmode {gentex} >/dev/null")
            if ret:
                print("Error! LaTeX failed", file=sys.stderr)
                break
            else:
                pages.append(taskfile.replace(".txt", ".pdf"))
            #os.unlink(gentex)
        elif taskfile.endswith(".tex"):
            print("LaTeX-process", taskfile)
            ret = os.system(f"pdflatex -output-directory={outputdir} -interaction=nonstopmode {taskpath} >/dev/null")
            if ret:
                print("Error! LaTeX failed", file=sys.stderr)
                break
            else:
                pages.append(taskfile.replace(".tex", ".pdf"))
        else:
            print("Error! Unknown suffix", task, file=sys.stderr)
            exit(-1)

    pagelist = " ".join(pages)
    olddir = os.getcwd()
    os.chdir(outputdir)
    os.system(f"pdftk {pagelist} cat output EXAM.pdf")
    os.chdir(olddir)

roottasksdir = "../generator/tasksgen"

tasksdirs = os.listdir(roottasksdir)

sout = os.path.join(roottasksdir, "admin", "students.out")
students = {}
f = open(sout)
for line in f:
    account, tasksdir = line.strip().split(",")
    students[tasksdir] = account

for tasksdir in tasksdirs:
    if tasksdir == "admin":
        continue

    outputdir = os.path.join("tasks-out", tasksdir)
    tasksdir = os.path.join(roottasksdir, tasksdir)
    student = students[os.path.basename(tasksdir)]
    print("**", tasksdir, student)
    #tasksdir = "tasks"
    #tasksdir = "../generator/tasksgen/314436814/"
    shuffletasks = True

    os.makedirs(outputdir, exist_ok=True)

    #tasks = sorted(os.listdir(tasksdir))

    tasks = []
    f = open(f"{tasksdir}/toc")
    for line in f:
        tasknum, tasktitle, points = line.strip().split(",")
        tasks.append((tasknum, tasktitle, points))

    if shuffletasks:
        random.shuffle(tasks)

    f = open("templatetitle.tex")
    t = f.read()

    fs = open("templatesolution.tex")
    ts = fs.read()

    s = ""
    totalpoints = 0
    for taskidx, task in enumerate(tasks):
        tasknum, tasktitle, points = task
        totalpoints += int(points)
        s += "\n"
        s += f"{taskidx + 1}. {tasktitle} ({points} points)\n"
    s += "\n"
    s += f"Total: {totalpoints} points\n"

    t = t.replace("%TOC%", s)
    ts = ts.replace("%TOC%", s)
    ts = ts.replace("%ACCOUNT%", student)

    admindir = os.path.join("admin-out", student)
    f = os.makedirs(admindir, exist_ok=True)
    for taskidx, task in enumerate(tasks):
        sol = os.path.join(roottasksdir, "admin", f"{student}.{task[0]}.solution")
        #print("SOL", sol)
        os.system(f"cp {sol} {admindir}/{task[0]}.txt")

    f = open(f"{outputdir}/0.tex", "w")
    print(t, file=f)
    f.close()

    f = open(f"{admindir}/0.tex", "w")
    print(ts, file=f)
    f.close()

    tasks = [(0, None, None)] + tasks

    render(tasks, tasksdir, outputdir)
    render(tasks, admindir, admindir)

    soutputdir = os.path.join("students-out", os.path.basename(tasksdir))
    os.makedirs(soutputdir, exist_ok=True)
    os.system(f"cp {outputdir}/EXAM.pdf {soutputdir}/{student}-sep.pdf")

    soutputdir = os.path.join("solutions-out", student)
    os.makedirs(soutputdir, exist_ok=True)
    os.system(f"cp {admindir}/EXAM.pdf {soutputdir}/{student}-solution.pdf")
