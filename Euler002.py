def fib(n):
    fib_list = [1, 1]
    while fib_list[-1] <= n:
        fib_list.append(fib_list[-2]+fib_list[-1])
    print(fib_list)
    return fib_list

returned_fib_list = fib(4000000)

total = 0
for i in returned_fib_list:
    if i%2 == 0:
        total += i

print(total)
