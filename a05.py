a = 12
b = 4
str = "a/dez={}, b/dez={}, a/hex=0x{:X}".format(a,b,a)
print(str)
txt2 = f"a/dez={a:d}, b/dez={b:d}, a/hex=0x{a:X}"
print(txt2)
txt3 = "a/dez=%d, b/dez=%d, a/hex=%#8x" % (a,b,a)
print(txt3)
