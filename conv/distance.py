"""
Modul zum Umwandeln von Längen zwischen Meter und
Zoll

"""
def meter2inch(val):
    """Rechne Meter in Zoll um"""
    return val * 39.37

def inch2meter(val):
    """Rechne Zoll in Meter um"""
    return val / 39.37


# if __name__ == "__main__":
#     m = 11
#     inch=meter2inch(m)
#     m_p = inch2meter(inch)

#     inch=celsius2fahrenheit(theta)
#     F_p = fahrenheit2celsius(F)
#     print(theta, T, theta_p)
#     print(theta, F, F_p)
#     if theta != theta_p: print("=> Differenz gefunden")

    