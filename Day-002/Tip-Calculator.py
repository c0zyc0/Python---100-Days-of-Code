"""
Tip Calculcator

Final Output :
Welcome to the tip calculator!
What was the total bill? $ - accept input
How much tip would you like to give? 10, 12, or 15? - accept input (12/100 = 0.12)
How many people to split the bill? - accept input
Each person should pay: - display amount each person should pay to 2nd decimal place

"""
print("Welcome to the Tip Calculator!")

#capturing total bill and type casting as float
total_bill = float(input("What was the total bill? $"))

#capturing tip percentage and type casting as int
tip_percentage = int(input("How much tip would you like to give? 10, 12, 15?"))

#making tip percentage into tip decimal and adding 1 to account for total calculation later
deci_tip_percent = (tip_percentage / 100) + 1

#capturing total people and type casting as int
people = int(input("How many people to split the bill?"))

#total bill divided by total people
tot_div_person = (total_bill / people)

#print(tot_div_person) #debug - testing for correct math

#calculating total for each person to pay (not in correct format yet) 
total = tot_div_person * deci_tip_percent

#round total to get requested print format - round to 2 decimal places
rTotal = round(total, 2)

#print total per person including tip
print(f"Each person should pay: ${rTotal}")
