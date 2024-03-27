from datetime import date

today= date.today()
print("Today's Date:",today)

import time
t=time.localtime()
current_time= time.strftime("%H:%M")
print("Current Time",current_time)