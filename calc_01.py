from colorama import init
from colorama import Fore
print( Fore.GREEN)
value0 = float(input("Enter first number --> "))
value1 = float(input("Enter second number --> "))
action =  input("Choose an action: ( +  -  /  * ) --> ")

if action == "+":
	x = value0 + value1
	print("Result --> "+ str(x))

elif action == "-":
	x = value0 - value1
	print("Result --> "+ str(x))
	
elif action == "/":
	x = value0 / value1
	print("Result --> "+ str(x))
	
elif action == "*":
	x = value0 * value1
	print("Result --> "+ str(x))	

else:				
	print("Choosed incorrect action")
	