import shutil
import glob
import tempfile
import time
import calendar
import random

shutil.copy("src.txt", "dst.txt")

print(glob.glob("C:/python/q*"))

print(tempfile.mktemp())

f = tempfile.TemporaryFile()
f.close()

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime("%x", time.localtime(time.time())))
print(time.sleep(2))

print(calendar.prcal(2015))
print(calendar.prmonth(2015, 12))
print(calendar.weekday(2015, 12, 31))
print(calendar.monthrange(2015, 12))

print(random.random())
print(random.randint(1, 10))
print(random.choice([1,2,3]))
print(random.shuffle([1,2,3,4,5,6,7]))