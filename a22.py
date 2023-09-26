idx = 0 # Index Error if out of bounds
val = 2 # Divide by Zero error if zero
seq=[1, 2]
try:
    neuwert = seq[idx]
except: IndexError
try:
    schwelle = 42 / val
except: ZeroDivisionError
print("Schwelle =", schwelle)