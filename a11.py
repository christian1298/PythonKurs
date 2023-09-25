data = [[10,5,5,5,"menu"], [0,0,200,20,"titlebar"],[50,30,15,5,"end button"]]
tx = 60
ty = 32

for i in data:
    dx = tx - i[0]
    dy = ty - i[1]
    #print(i)
    if((dx < 0) or (dx >= i[2])):
        continue
    if((dy < 0) or (dy >= i[3])):
        continue
    print("test point (%d , %d) inside rect %s\n" % (tx , ty, i[4]))