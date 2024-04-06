#Establish a String of "Hello World". 
#Create string which makes each other character an upper case.

String = "Hello World"


#For each letter, if the second letter is lowercase, convert to uppercase. 
Container_For_Outcome = ""

for letter_within_string in range(len(String)): #For each letter within the String, the loop should run.
    if letter_within_string % 2 == 0: #I can identify every other letter by using a Modulus Operator
        Container_For_Outcome += String[letter_within_string].upper() #For every second letter, create a string which is upper case

    else:
        Container_For_Outcome += String[letter_within_string].lower() #For every other letter, this will be lower case, however due to my variable, "H" will have an index of 1.

print(Container_For_Outcome)

