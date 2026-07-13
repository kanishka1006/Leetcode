def roman_to_integer(n):
    roman = {
        'I' : 1,
        'v' : 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    for i in range(len(n)):
        # if the current value is smaller than next value
        if i < len(n) -1 and roman[n[i]] < roman[n[i+1]]:
            total -= roman[n[i]]
        else:
            total -= roman[n[i]]
                    

            
    return total
 