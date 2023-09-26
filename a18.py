from glob import glob


for i in glob("*.py"):
    with open(i, "r") as f:
        if( "print" in f.read()):
            print(i, end=" ")