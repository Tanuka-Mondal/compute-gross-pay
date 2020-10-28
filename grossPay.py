#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
print("Hello user!")
hours = input("Enter Hours:")
rate = input("Rate per hour: ")

h=float(hours)
r=float(rate)

rate=h*r

print("Pay: "+str(rate))
