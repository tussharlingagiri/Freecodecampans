def add_time(start, duration,starting_day=None):
  
  # a start time in the 12-hour clock format (ending in AM or PM)
  # a duration time that indicates the number of hours and minutes
  # the Function should add the duration time to the start time and return the result
  # If the result will be the next day, it should show (next day) after the time
  # If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.
  # If the function is given the optional starting day of the week parameter, then the output should display the day of the
  # minutes wil be a whole number less than 60

  days_of_week_array = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  days_of_week_index = {"monday":0,"tuesday":1,"wednesday":2,"thursday":3, "friday":4,"saturday":5,"sunday":6}
  days_later = 0
  start_hours,start_minutes = map(int,start.split()[0].split(":"))
  duration_hours , duration_minutes = map(int,duration.split(":"))
  period = start.split()[1]

  if period.upper() == 'PM':
    start_hours += 12

  end_hours = start_hours + duration_hours
  end_minutes = start_minutes + duration_minutes

  if end_minutes >= 60:
    end_hours  += end_minutes //60
    end_minutes = end_minutes % 60

  days_later = end_hours // 24
  end_hours = end_hours % 24

  new_period = 'AM' if end_hours < 12 else 'PM'
  end_hours = end_hours % 12
  end_hours = 12 if end_hours == 0 else end_hours
  new_time = f"{end_hours}:{end_minutes:02d} {new_period}"

  if starting_day:
    day_index = (days_of_week_index[starting_day.lower()] + days_later)      % 7
    new_day = days_of_week_array[day_index]
    new_time += f", {new_day}"

  if days_later == 1:
    new_time += " (next day)"
  elif days_later > 1:
    new_time += f" ({int(days_later)} days later)"
  return new_time
      
    

  
  





  