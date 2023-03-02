def time_set(x, y, z):
    if y < 10:
        if z == "AM":
            return(str(x) + ":0" + str(y) + " AM")
        if z == "PM":
            return(str(x) + ":0" + str(y) + " PM")
    if y > 9:
        if z == "AM":
            return(str(x) + ":" + str(y) + " AM")
        if z == "PM":
            return(str(x) + ":" + str(y) + " PM")


def add_time(start, duration, day = "any"):
    colon_start = start.find(":")
    colon_duration = duration.find(":")

    h12_start = int(start[:colon_start])
    if start[-2:] == "PM":
        h_start = h12_start + 12
    if start[-2:] == "AM":
        h_start = h12_start
    h_duration = int(duration[:colon_duration])
    m_start = int(start[colon_start + 1 : colon_start + 3])
    m_duration = int(duration[colon_duration + 1:])

    if (m_start + m_duration)/60 < 1:
        right_m = m_start + m_duration
        raw_h = h_start + h_duration
    else:
        right_m = (m_start + m_duration)%60
        raw_h = h_start + h_duration + 1
    
    if day == "any":
        if raw_h < 12:
            right_h = raw_h
            return(time_set(right_h, right_m, "AM"))
        if raw_h == 12:
            return(time_set(12, right_m, "PM"))
        if 12 < raw_h < 24:
            right_h = raw_h - 12
            return(time_set(right_h, right_m, "PM"))
        if raw_h == 24:
            return(time_set(12, right_m, "AM"))
        if 24 < raw_h < 37:
            right_h = raw_h - 24 
            return(time_set(right_h, right_m, "AM") + " (next day)") 
        if 36 < raw_h < 48: 
            right_h = raw_h - 36
            return(time_set(right_h, right_m, "PM") + " (next day)")
        if raw_h > 47:
            raw2_h = raw_h%24
            n = raw_h//24
            if raw2_h == 0:
                return(time_set(12, right_m, "AM") + " (" + str(n) + " days later)") 
            if 0 < raw2_h < 12:
                right_h = raw2_h
                return(time_set(right_h, right_m, "AM") + " (" + str(n) + " days later)")
            if raw2_h == 12:
                return(time_set(12, right_m, "PM") + " (" + str(n) + " days later)")
            if 12 < raw2_h < 24:
                right_h = raw2_h - 12
                return(time_set(right_h, right_m, "PM") + " (" + str(n) + " days later)")
     
    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    week_wcase = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day != "any":
        case_day = day.lower()
        start_day = week.index(case_day)
        if raw_h < 12:
            right_h = raw_h
            return(time_set(right_h, right_m, "AM")+ ", " + week_wcase[start_day])
        if raw_h == 12:
            return(time_set(12, right_m, "PM"))            
        if 12 < raw_h < 24:
            right_h = raw_h - 12
            return(time_set(right_h, right_m, "PM") + ", " + week_wcase[start_day])
        if raw_h == 24:
            return(time_set(12, right_m, "AM"))
        if 24 < raw_h < 37:
            right_h = raw_h - 24 
            return(time_set(right_h, right_m, "AM")+ ", " + week_wcase[start_day + 1] + " (next day)") 
        if 36 < raw_h < 48: 
            right_h = raw_h - 36
            return(time_set(right_h, right_m, "PM") + ", " + week_wcase[start_day + 1] + " (next day)")
        if raw_h > 47:
            raw2_h = raw_h%24
            n = raw_h//24
            if raw2_h == 0:
                return(time_set(12, right_m, "AM")+ ", " + week_wcase[(start_day + n)%7] + " (" + str(n) + " days later)")  
            if 0 < raw2_h < 12:
                right_h = raw2_h
                return(time_set(right_h, right_m, "AM")+ ", " + week_wcase[(start_day + n)%7] + " (" + str(n) + " days later)")
            if raw2_h == 12:
                return(time_set(12, right_m, "PM") + ", " + week_wcase[(start_day + n)%7] + " (" + str(n) + " days later)")
            if 13 < raw2_h < 24:
                right_h = raw2_h - 12
                return(time_set(right_h, right_m, "PM") + ", "+ week_wcase[(start_day + n)%7] + " (" + str(n) + " days later)")
                  

print(add_time("11:59 PM", "24:05", "Monday"))