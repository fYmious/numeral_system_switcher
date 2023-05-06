def convert_number(number, from_base, to_base):
    if from_base == 10:
        return int(str(number), to_base)
    else:
        decimal_number = 0
        for i, digit in enumerate(str(number)[::-1]):
            decimal_number += int(digit) * (from_base ** i)

        if to_base == 10:
            return decimal_number
        else:
            result = []
            while decimal_number > 0:
                remainder = decimal_number % to_base
                result.append(str(remainder))
                decimal_number //= to_base

            return int(''.join(result[::-1]))


print(convert_number(22222, 3, 10))
