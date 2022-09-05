import os

for path, sub, files in os.walk(os.getcwd()):
    if os.getcwd != path:
        os.chdir(path)
    for j in files:
        if j[len(j) - 3 : len(j)] == ".py":
            if j != "uafile.py":
                print(j)
                os.system('python3 ' + j)
