# 19. [IGA] Answer 4.6 Returning Values from Custom Functions
"""
Here we will use a different example  detecting an angle between the hours arm and the minutes arm in an analog watch .
 Happy Coding >>>>>>>>>
"""
hours = float(input("hour is : "))
minutes = float(input("minutes  are  : "))

def angle_anlaog(hours, minutes):
    if hours == 12 :
        hours = 0
    # 30 degree is correspond to each hour >>> (360 degree / 12 hours) = 30 degree
    angle_of_hours_arm = (30 * hours) + (0.5 * minutes)
    # 0.5 minutes : each minutes adds 0.5 degrees to the hour hand position
    angle_of_minutes_arm = 6 * minutes
    # the angle of minute hand is calculated as >> minutes hand angle = 6* minutes
    angle_between_hands = (angle_of_minutes_arm)-(angle_of_hours_arm)
    return (F"When tie is {hours} : {minutes}\n"
            F"Angle is : {angle_between_hands}")

print(angle_anlaog(hours, minutes))

# this code is working perfectly just for now but in the future we will add some enhancement to it