#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.

hrs = input("Enter Hours:")
rph = input("Rate per hour: ")

h=float(hrs)
r=float(rph)

rate=h*r

print("Pay: "+str(rate))
