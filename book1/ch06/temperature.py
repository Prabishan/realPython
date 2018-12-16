def celsius_to_fahrenheit(C):
    F = C*9/5+32
    return F
def fahrenheit_to_celsius(F):
    C=(F-32)*(5/9)
    return C
temp1 = 72;
print("{} degrees F = {} degrees C".format(temp1,fahrenheit_to_celsius(temp1)));
temp2 = 37;
print("{} degrees C = {} degrees F".format(temp2,celsius_to_fahrenheit(temp2)));
