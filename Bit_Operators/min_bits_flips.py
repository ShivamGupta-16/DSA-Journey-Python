# Q. Calculate the minimum number of bit flip to convert from one number to another.


def count_set_bits(num):
    count =0
    while num >0:
        count += num&1
        num >>= 1
    return count

def find_different_bits(n1,n2):
    xor_res = n1^n2
    return count_set_bits(xor_res)


print(find_different_bits(5,11))
    