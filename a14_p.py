def get_ones(n: int):
    c = 0
    while n != 0:
        if(n & 1):
            c += 1
        n = n >> 1
    return c

print(get_ones(1))
print(get_ones(5))

def get_bits_as_list(n: int):
    return [int(n) for n in [*bin(n)[2::]]]

print(get_bits_as_list(10))

def sort_by_ones(n: list):
     return sorted(n, key=get_ones)

print(sort_by_ones([3, 9, 7, 5, 3]))