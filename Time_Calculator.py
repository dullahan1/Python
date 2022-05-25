
def add_time(start, duration, day=False):
	

	daysdic = { "sunday": 0,
    	     "monday": 1,
        	 "tuesday": 2,
         	"wednesday": 3,
         	"thursday": 4,
         	"friday": 5,
         	"saturday": 6,
         	}
            
	values = { 0: "Sunday",
    	       1: "Monday",
        	   2: "Tuesday",
         	   3: "Wednesday",
         	   4: "Thursday",
         	   5: "Friday",
         	   6: "Saturday",
         	}

	first_time = start.split(" ")
	value1 = start[:-2].split(':')
	hourv1 = value1[0]
	minutesv1 = value1[1]
	value_minutes = int(minutesv1)
	time_interval = first_time[1]
	h = int(hourv1) % 12
	
	if time_interval == "PM" : 
		h = h + 12
    
	total_time = (h*60)+value_minutes
    
       
	duration = duration.split(":")
	
	hourv2 = duration[0]
	minutesv2 = duration[1]
	minutes_total = int(hourv2)*60 + int(minutesv2)
	hours_duration = minutes_total/60
    
    #sum of all time in minutes divided by 60
	sum_of_time = (total_time + minutes_total)/60
    #decimals of sum of all time
	decimals = sum_of_time - int(sum_of_time)
    #minutes for result <-------------------------------------------------------
	decimal_minutes = round(decimals*60) 
	if decimal_minutes < 10:
		decimal_minutes = "0"+str(decimal_minutes)
    #days ahead
	days_ahead = (sum_of_time/24)
	#newday = (days_ahead + days[day]) % 7
    #time format
	time_format = int(sum_of_time%12)
	if time_format == 0:
		time_format = 12
	if sum_of_time % 24 > 12:
		suffix = "PM"
	else:
		suffix = "AM"
	
	if day == False:
		if days_ahead < 1:
			return str(time_format) +":" +str(decimal_minutes) + " " + suffix  
		elif days_ahead > 1 and days_ahead <2 :
			return str(time_format) +":" +str(decimal_minutes) + " " + suffix + " (next day)"
		else:
			return str(time_format) +":" +str(decimal_minutes) + " " + suffix + " " + "(" + str(round(days_ahead)) + " days later)"
    
	else:
		days = day.casefold()
		newday = (round(days_ahead) + daysdic[days]) % 7
		if days_ahead < 1:
			return str(time_format) +":" +str(decimal_minutes) + " " + suffix + ", " + day
		elif days_ahead > 1 and days_ahead <2 :
			return str(time_format) +":" +str(decimal_minutes) + " " + suffix + ", " + values[newday] + " (next day)"
		
		return str(time_format) +":" +str(decimal_minutes) + " " + suffix + ", " + values[newday] + " " + "(" + str(round(days_ahead)) + " days later)"

print(add_time("2:59 AM", "24:00", "saturDay"))