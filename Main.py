#Nicole Tambone
#A program that combines all my programming exercises
intro= "Hello!" * 3
print(intro)
print("My name is Nicole!")
print("My email is: nmtambone2597", end = '@')
print("eagle.fgcu.edu")
print("The date is," '09','23','2021', sep='-')
age = input("How old are you? ")
#enter 21
print("I am", age)
major= input("Enter major:")
#enter Mathematics
year= input("Enter year:")
#enter Senior
university= input("Enter university name:")
#enter Florida Gulf Coast University
print( "I am majoring in " + major + " , and I am a " + year + " at " + university)
num1= 12
num2= 3
difference= num1 - num2
print("Difference = ", difference)
#This subtracts the 2 numbers in the equation
num3= 12
num4= 6
addition= num3 + num4
print("Sum = ", addition)
#This adds the 2 numbers in the equation
num5= 5
num6= 3
product= num5 * num6
print("Product = ", product)
#This multiplys the 2 numbers in the equation
num7= 18
num8= 9
quotient= num7 / num8
print("Quotiet = ", quotient)
#This divides the 2 numbers in the equation
num9= 6
num10= 4
mod= num9 % num10
print("Mod = ", mod)
#This shows the mod of the equation. It gives the number minus the remainder
remainder= num9 // num10
print("Remainder = ", remainder)
#This gives just the remainder of the equation
num11=4
num12=2
exponent= num11 ** num12
print("Exponent = ", exponent)
#This gives the answer to the exponent
#For all the math equations i used POGIL04
original_test_score= float(input("Enter the original test score: "))
#input a grade such as 74.3
original_test_score= float(input("Enter the original test score: "))
#input a grade such as 74
class_curve= float(input("Enter the class curve: "))
#input a class curve such as 10 pts
new_test_score= float(int(original_test_score + class_curve))
print("Original test score: ", original_test_score)
print("Class curve: ", class_curve)
print("New test score: ", new_test_score)
if (new_test_score >= 85):
    print("You got a great test score!")
books_read = 40
if (books_read > 5) and (books_read < 100):
    print("True")
steps_walked = 8000
if (steps_walked > 5000) or (steps_walked < 10000):
    print("True")
calories_consumed = 2700
if not(calories_consumed <= 2500):
    print("True")
credit_hours = int(input("Enter credit hours: "))
#enter the number of credit hours you have to see if you can graduate
if (credit_hours >= 120):
    print("Congrats, your can graduate!")
else:
    print("Unfortunately, you cannot gradutate.")
cop_1500_grade = int(input("Enter your grade in COP 1500: "))
if cop_1500_grade >= 90:
    print("Very Good! You have an A")
elif cop_1500_grade < 90 and cop_1500_grade >= 80:
    print("Good! You have a B")
elif cop_1500_grade < 80 and cop_1500_grade >= 70:
    print("Satisfactory, you have a C")
elif cop_1500_grade < 70 and cop_1500_grade >= 60:
    print("Fair, you have a D")
elif cop_1500_grade < 60:
    print("Poor, you have an F")
average_quiz_grade = int(input("Enter your average quiz score in COP 1500: "))
if average_quiz_grade >= 90:
    print("Very good! You have an A")
elif average_quiz_grade >= 70:
    print("Great, you are passing.")
else:
    print("Poor")
favorite_color = input("Enter your favorit color: ")
x = 0
while (x < 10):
    print(favorite_color)
    x = x + 1
greeting = input("Enter a greeting: ")
for name in range(5):
    for name in range(3):
        print(greeting + " ", end= " ")
    print()
def add_numbers(num1, num2):
    print(num1, "+", num2, "=", num1+num2)

def subtract_numbers(num1, num2):
    print(num1, "-", num2, "=", num1-num2)

def main():
    first_number = int(input("Enter a number between 1 and 20: "))
    second_number = int(input("Enter a number between 1 and 20: "))
    operator = input("Enter a '+' to add or a '-' to subtract: ")

    if operator == '+':
        add_numbers(first_number, second_number)
    elif operator == '-':
        subtract_numbers(first_number, second_number)
    else:
        print("Invalid operator!")

main()
total = 0
for integer in range(5):
    number = int(input("Enter a number: "))
    total += number
print("The total is:", total)
total = 0
for integer in range(5):
    number = int(input("Enter a number: "))
    total -= number
print("The total is:", total)
do_again = True
while do_again:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))
    number4 = int(input("Enter the fourth number: "))
    maximum_of_numbers = max(number1, number2, number3, number4)
    print("The largest of the four numbers is: ", maximum_of_numbers)
    another = input("Type 'y' to find another max number " + "or any other key to quit.")
    if another != 'y':
        do_again = False
print("Done!")



      
