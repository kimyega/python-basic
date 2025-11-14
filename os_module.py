import os
print(os.environ)
print(os.environ['PATH'])
os.chdir("C:/WINDOWS")
print(os.getcwd())
print(os.system("dir"))
f = os.popen("dir")
print(f.read())