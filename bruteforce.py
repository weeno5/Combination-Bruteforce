# This Python code experiments whether it is more optimal to bruteforce a four-digit combination in chronological order or in a random order.
# Results are appended into the result.txt file

import random

# Function for bruteforcing in a chronological order
def chronological(combination):
    
	num = 0
 
	while num != combination:
		print (num)
		num+=1
  
	print ("Combination is found :", combination)
 
	with open ("result.txt","a") as f:
		strnum = str(combination)
		f.write("Chr : ")
		f.write(strnum)
		f.write("\n")

# Function for bruteforcing in a random order
def rando(combination):
    
	num = random.randint(0,9999)
	count = 1
 
	while num!= combination:
		print(num)
		num = random.randint(0,9999)
		count += 1
  
	print ("Combination is found :", combination)
	print("Total amount of iterations :", count)
 
	with open ("result.txt","a") as f:
		strnum = str(count)
		f.write("Ran : ")
		f.write(strnum)
		f.write("\n")

# While loop for interacting with the code indefinitely
while True:
    
	combination = random.randint(0,9999)
 
	input("Press ENTER to bruteforce the combination CHRONOLOGICALLY")
	chronological(combination)
	input("Press ENTER to bruteforce the combination RANDOMLY")
	rando(combination)
	with open ("result.txt","a") as f:
		f.write("\n")