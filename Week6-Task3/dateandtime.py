##date and time
##
##
##import datetime
##from datetime import datetime,timedelta
##c_time=datetime.now()
##print(c_time.replace(microsecond=0))
##
##
##
##print(type(c_time))
##mod_time=c_time.replace(microsecond=0)
##print(mod_time)
##
##2023-06-28 15:15:15 - %y-%m-%d %H:%m:%s
##
##c_time = datetime.now()
##delta=c_time+timedelta(minutes=120)
##print(delta)
##
##
##
##c_time = datetime.now()
##dy = "%Y-%b-%d %H:%M:%S"
##mod_time = datetime.strftime(c_time,dy)
##print(mod_time)
##print(type(mod_time))



##from datetime import datetime
##
##current_datetime = datetime.now()  # Get the current date and time
##print("Current datetime:", current_datetime)




##from datetime import date
##
##today = date.today()  # Get the current date
##print("Today's date:", today)
##
##
##
##
##import time
##import datetime
##from datetime import datetime
##
##current_time = datetime.now().time() # Get the current time
##print("Current time:", current_time)

##
##
##
from datetime import datetime, timedelta
##
##future_datetime = datetime.now() + timedelta(days=7)  # Add 7 days to the current datetime
##print("Future datetime:", future_datetime)
##
##
##from datetime import datetime
##
##current_datetime = datetime.now()
##formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")  # Format as string
##print("Formatted datetime:", formatted_datetime)
##
##date_string = "2023-15-06"
##parsed_datetime = datetime.strptime(date_string, "%Y-%d-%m")  # Parse string into datetime
##print("Parsed datetime:", parsed_datetime)
##
##
from datetime import datetime, timezone

current_datetime = datetime.now()
utc_datetime = current_datetime.astimezone(timezone.utc)  # Convert to UTC timezone
print("UTC datetime:", utc_datetime)

##
##




