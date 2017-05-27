# Imports arguments entered on command line as variables for the program.
#from sys import argv

#Assigns variable names to the arguments fed from the system
#script, filename = argv #script is the name of the program, filename is the file you want to open
filename=input("What is the name of the file?(Include the extenstion) >")
# Opens the file fed from the command line.
txt = open(filename)

#Prints a line to thecommand window introducing your file.
print(f"Here's your file {filename}:")

#Reads and prints your file.
print(txt.read())

#Asks for input from the user in the form of the filename. 
print("Type the filename again:")

#Assigns the input from the user to varible named "file_again"
file_again = input("> ")

#opens the file with the name the user entered
txt_again = open(file_again)

#prints the contens of the file. 
print(txt_again.read())