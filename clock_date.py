from datetime import date
from datetime import time
from datetime import datetime

def clock_date():
    #this will show you date of today
    today=date.today()
    #this will show you date and time of right now
    #dat_tim=datetime.now()

    #this will show you time of right now
    tim=datetime.time(datetime.now())
    #this will show you day number
    wd=date.weekday(today)
    days= ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    print('Date of today is',today,'and time is',tim,"today is day number",wd,"of week","which is", days[wd])

clock_date()