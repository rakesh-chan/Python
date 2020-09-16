def math_op(a,b):
    classic_division = 3/2
    floor_division = a//b
    modulus = a%b
    power=a**b
    return [classic_division,floor_division,modulus,power]

[classic_division,floor_division,modulus,power] = math_op(3,2)
print(classic_division)
print(floor_division)
print(modulus)
print(power)

