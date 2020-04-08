#this program calculates the return on investment. User is required to input initial amount, interest rate, length of investment and investment type (simple/compound)
import math #imports advanced math functions to file
amount = float(input("Enter amount deposited: ")) #declare variable, cast to float
rate = float(input("Enter the interest rate: "))  #declare variable, cast to float
years = int(input("Enter number of years: ")) #declare variable, cast to integer
interest = input("interest type, simple or compound: ") #declare variable, cast to integer
 
ratePercent = rate /100 #converts interest rate to a percentage
 
if interest == "simple":  #if simple investment type chosen by user
    A =amount*(1 + ratePercent * years) #calculates simple return
    print ("R" + str(round((A), 2))) #output result, float cast to string and rounded to 2 decimal places
else: #if compound investment type chosen by user
    A =amount* math.pow((1 + ratePercent),years) #calculates compound return
    print ("R" + str(round((A), 2)))  #output result, float cast to string and rounded to 2 decimal places
