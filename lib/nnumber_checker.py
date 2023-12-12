def two_positives(a,b,c):
    

    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        print(f"a, b, or c is not int")
        return False

    print(f"Two or more positives in \n{a ,b, c}", end=" = ")
    
    count_positive_number = 0
    
    if a > 0:
        count_positive_number += 1
    if b > 0:
        count_positive_number += 1
    if c > 0:
        count_positive_number += 1
        
    if count_positive_number >= 2:
        print("True")
        return True
    else:
        print("False")
        return False
    
    
    
