try:
    1 / 0
except: ZeroDivisionError

d = {}
try:
    d["d"]
except: KeyError

d = []
try:
    d["d"]
except: TypeError