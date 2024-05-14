z = int(input())

def f(n):
    bin_n = bin(n)
    bin_n = bin_n[2:]
    s_bin_n = bin_n + '01' if n % 2 == 0 else '10'
    print(int(s_bin_n, base = 2))

f(z)