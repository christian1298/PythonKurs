def get_ones(val):
    return bin(val).count("1")

def sort_by_ones(seq):
    ret = seq.copy()
    ret.sort(key=get_ones)
    print(ret)
    return ret

def get_bits_as_list(val):
    return [int(x) for x in [*bin(val)[2::]]]

print(get_ones(7))
print(sort_by_ones([1,0x21,7,0x80,0,0b1111]))
print(get_bits_as_list(27))