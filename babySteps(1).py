
# Online Python - IDE, Editor, Compiler, Interpreter

print("Hi there")


#age = 20
#price = 19.95

first_name = "Marco"
is_online = True

print("Exercise")
patient_name = 'John Smith'
patient_age = 20
is_new_patient = True

''' 
Exercise to calculate your birthday 

name = input("What is your name? ")

print("Hello " + name)

birth_year = input("Enter your birth year: ")

age = 2023 - int(birth_year)

print(age)


'''

'''
Exercise to sum 2 numbers 


first_num = float(input("Enter first number: "))
sec_num = float(input("Enter second number: "))

sum = first_num + sec_num

print("Sum : "+ str(sum))

'''

'''
alternative Ex. sum 

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')

'''

course = 'Python for Beginners'
print(course.upper())
print(course)

print (course.find('y'))

print (course.replace('for','4'))

print ('Python' in course) # check if there is the word "Python" in the variable string course

'''
Arithmetic Operator
'''
print (10 //  3 )
print (10 / 3)

print (10%3)

print (10**3)

'''
Comparison Operator
'''

print()

x = 3>2
print(x)

#   >  
#   <
#   >=
#   <=
#   ==
#   !=

'''
Logical Operator
'''
print ("------------------------------------------------------")

price = 5
print (not price > 10)

print ( price > 2 and price < 30 )

print ( price > 10 or price < 30 )


'''
IF statement 
'''
print ("------------------------------------------------------")

temperature = 35

if temperature > 30 : 
    print("It's a hot day")
    print("Drink")
elif temperature > 20 :
    print("It's a nice day")
    
print("Done")


'''
Exercise Weight converter 
'''
print ("----------------Exercise-------------------------")

weight = float(input("Weight: "))
unit = input("(K)g or (L)bs :")

if unit == 'k' or unit == 'K' :
    weight = weight * 2.20462
    print("Weight in lbs: " + str(weight))
    
if unit == 'l' or unit == 'L': 
        weight = weight * 0.453592
        print("Weight in Kg: " + str(weight))
        
        
        














































































































































































