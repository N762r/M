z = int(input())

def f(n):
    bin_n = bin(n)
    bin_n = bin_n[2:]
    s_bin_n = '1' + bin_n + '11' if n % 2 == 0 else '1' + bin_n + '1'
    s_bin_n = s_bin_n + bin_n[-1] if bin_n.count('1') % 2 == 0 else s_bin_n + bin_n[-2]
    print(int(s_bin_n, base = 2))

f(z)