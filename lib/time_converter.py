def convert_to_24_hour(hour, minute, period):
    
    print(f"convert {hour}:{minute if minute >= 10 else '0'+str(minute)} {period} to 24 hrs")
    
    if not (1 <= hour <= 12) or not (0 <= minute <= 59) or (period != 'am' and period != 'pm'):
        print("Invalid input")
        
    if period == 'am':
        
        if hour == 12:
            hour = 0
    else:
        
        if hour == 12:
            pass
        else:
            hour += 12
    
    
    if hour < 10:
        hour_str = '0' + str(hour)
    else:
        hour_str = str(hour)
    if minute < 10:
        minute_str = '0' + str(minute)
    else:
        minute_str = str(minute)

    
    
    print(hour_str + minute_str + "H")

