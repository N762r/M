def convert_base(num_str, from_base=10, to_base=10):
    decimal_number = int(num_str.split('.')[0], from_base) + int(num_str.split('.')[1], from_base) / (from_base ** len(num_str.split('.')[1]))
    
    integer_part = int(decimal_number)
    fractional_part = decimal_number - integer_part
    
    res = ''
    while integer_part:
        res = str(integer_part % to_base) + res
        integer_part //= to_base
    
    res += '.'
    
    while fractional_part:
        fractional_part *= to_base
        fractional_digit = int(fractional_part)
        res += str(fractional_digit)
        fractional_part -= fractional_digit
        if len(res.split('.')[1]) >= 5:
            break
    
    return res
num = input()
from_base = int(input())
to_base = int(input())
print(convert_base(num, from_base, to_base))
