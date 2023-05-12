# write a function with *args
# write a function that takes variable number of arguments and returns their sum

def sum_all(*chai):
    return sum(chai)


print(sum_all(1,2))
print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,5))