# 2. Variable Names

# now it's an interesting part about Variable Names
student_count  = 120
student_count001 = int(120)
student_count01 = float(120)
student_count1 = "120"
# you may think they all the same but let us  see what is behind each one .
print(student_count, student_count1, student_count01, student_count001)
# the output should all the sme because we are only printing them nothing more
# output like >> 120 120 120.0 120
# but if we need to run some king of math operation what we are going to do here  ?
print(student_count001 + student_count01+ student_count)
# this wil give me output as 120 +120 +120.0 = 360.0

# print(student_count1 + student_count)
#  print(student_count1 + student_count)
#           ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~
# TypeError: can only concatenate str (not "int") to str
# to get answer correct we have to do convert the str to int value of float
# like that
print(int(student_count1) + student_count)
# answer be like = 240

# happy coding

