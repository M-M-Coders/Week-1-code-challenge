def solve (word):
    word = word.lower()
    alphabet="abcdefghijklmnopqrstuvwxyz"
    vowels="aeiou"
    
    current_sum = 0
    max_value=0
    current_string=''
    max_value_string=''

    print(f"Solve word {word}")
    
    for char in word:
        if not char in vowels:
            current_sum += alphabet.index(char)+1
            current_string +=char
            
        else:
            max_value = max(max_value, current_sum)
            max_value_string = current_string if max_value == current_sum else max_value_string
            current_sum = 0
            current_string = ''
            
    max_value = max(max_value, current_sum)
    max_value_string = current_string if max_value == current_sum else max_value_string

    return print (f'The max value is {max_value} for string {max_value_string}')
            
    
