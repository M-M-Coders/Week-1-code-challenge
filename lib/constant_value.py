def constant_value_assignment(s):
    
    vowels = 'aeiou'
    max_value = 0
    current_value = 0

    for char in s:
        if char not in vowels:
            current_value += ord(char) - ord('a') + 1
            if current_value > max_value:
                max_value = current_value
        else:
            current_value = 0

    return max_value
