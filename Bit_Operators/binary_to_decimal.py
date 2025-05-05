def binary_to_decimal(number):
    out =0
    power = 0
    for i in range(len(number)-1,-1,-1):
        if number[i] ==1:
            out += 2**power
        power+=1
    return out

number= [1,0]
print(binary_to_decimal(number))