from a23_p import Rect
with open("Dateien/Uebung/rects.txt", "r") as f:
    l = f.readlines()

r = []
d = {}
for i in l:
    i = i.split(":")
    try:
        i[4] = i[4].replace("\n", "")
    except IndexError:
        exit()  
    r.append(Rect(int(i[0]), int(i[1]), int(i[2]), int(i[3]), i[4]))
    d[i[4]] = Rect(int(i[0]), int(i[1]), int(i[2]), int(i[3]), i[4])

tx = 60
ty = 32
for i in r:
    i.contains(tx, ty)

desc = input("Eingabe: ")
try:
    val = d.get(desc)
    print(val.x,val.y,val.w,val.h)
except:
    print("Not in dataset")
    
# for i in r:
#     if(i.name == desc):
#         print(i.x,i.y,i.w,i.h)
#         break
# else:
#     print("Not in dataset")
