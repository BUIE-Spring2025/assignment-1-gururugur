def int_to_roman(num):
    roman_values = {
        1: "I", 4: "IV", 5: "V", 9: "IX",
        10: "X", 40: "XL", 50: "L", 90: "XC",
        100: "C", 400: "CD", 500: "D", 900: "CM",
        1000: "M"
    }
    
    # Sorting keys by descending order
    sorted_keys = sorted(roman_values.keys(), reverse=True)
    
    roman_numeral = ""  # Our result string

    # Here I convert the number from maximum to minimum
    for value in sorted_keys:
        while num >= value:
            roman_numeral += roman_values[value]  # Add the Roman symbol
            num -= value  # Substract the number
    
    return roman_numeral
