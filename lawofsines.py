import math

print("This is a solver for law of sines created by Simon Socolow and ouputs angles in degrees")
a1 = float(input("Enter angle 1 (You should know this angle and the corresponding side): "))
a1rad = math.radians(a1)
s1 = float(input("Enter side 1 (that corresponds with angle 1): "))

a2 = input("Enter angle 2 (if unknown enter 'u' )(without the quotation marks): ")
s2 = input("Enter side 2 (that corresponds with angle 2) (if unknown enter 'u') (without the quotation marks): ")

if a2 == "u":
    s2 = float(s2)
    a2 = math.degrees(math.asin((math.sin(a1rad)*s2)/s1))
    q = input("Is the unknown angle obtuse? Answer 'y' for yes or 'n' for no (without the quotation marks):  ")
    if q == "y":
        a2 = 180 - a2
        print("Angle 2 equals " + str(a2) +" degrees")
    else:
        print("Angle 2 equals " + str(a2) +" degrees")

if s2 == "u":
    a2 = math.radians(float(a2))
    s2 = (s1*math.sin(a2))/math.sin(a1rad)
    print("Side 2 equals " + str(s2))
