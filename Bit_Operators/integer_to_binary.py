def integer_t0_binary(number):
    out =[]
    while number > 0:
        out.append(number%2)
        number//=2
    out.reverse()
    return out


print(integer_t0_binary(4))

