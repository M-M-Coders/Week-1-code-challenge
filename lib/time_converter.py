def convert_it(hour, minute, period):
   
   if period.lower() =='am':
      if hour ==12:
         hour=0

   else:
      if hour !=12:
         hour+=12

   return f'{hour}{minute}'