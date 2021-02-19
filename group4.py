#Write a program that will accept and compute the sum of odd numbers 
#between 1 and 100 inclusive

#Solution

#........................................................................
#Psuedo Code 
#........................................................................


#1# Input a number between 1 and 100 inclusive from a user and save as maximunNumb
#2# Declare a varible oddSum to store the total sum and initialize it to 0
#3# If maximumNumb is not a valid number. then restart program .............
#4# While maximumNumb is less than 1 or greater than 100 ask user to input a number

#5# Iterate through the maximumNumb by checking for the difference with 1
#6# Use control structure to check whether the difference is an odd numbers
#7# Add the oddSum with the odd numbers from the control structure
#8# Output the oddSum



def callFunction():
    try:
        maximumNumb = int(input("Enter a maximum number : "))
        oddSum = 0

        while maximumNumb > 100 or maximumNumb < 1:
            maximumNumb = int(input("Enter a number between 1 and 100 inclusive :"))


        for numbers in range(1, maximumNumb + 1):
            if(numbers % 2 == 1):
                oddSum = oddSum + numbers
                
        print("The sum of the odd numbers : " + str(oddSum) )
    except ValueError as _:
        print("Value entered is not a number. Try again...")
        callFunction()


callFunction()


#===================================================================================
#Flow chart
#===================================================================================

        