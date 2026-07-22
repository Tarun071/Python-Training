def multiplier(n):
    def multiply(x):
        return x * n
    return multiply
double = multiplier(2)
triple = multiplier(3)
quadruple = multiplier(4)
quintuple = multiplier(5)
print("Double the number of 15 =", double(15))
print("Triple the number of 15 =", triple(15))
print("Quadruple the number of 15 =", quadruple(15))
print("Quintuple the number of 15 =", quintuple(15))