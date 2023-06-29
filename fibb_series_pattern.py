
a, b = 0, 1
fib_pattern = ""

for i in range(4):
    fib_line = ""
    for j in range(i + 1):
        fib_line += str(a) + " "
        a, b = b, a + b   
    fib_pattern += fib_line + "\n"
    # breakpoint()
print(fib_pattern)
