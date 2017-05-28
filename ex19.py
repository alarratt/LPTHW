#This line defines the function as "cheese_and_crackers," but should really have
#a better name.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#Each o the following lines prints a string with one of the variables defined for
#the function in the line.
    print (f"You have {cheese_count} cheeses!")
    print (f"You have {boxes_of_crackers} boxes of crackers!")
    print ("Man, that's enough for a party!")
    print ("Get a blanket.\n")

#The next two lines demonstrate how the function will assign 
#numbers to the variables to give into the function
print ("We can just give the functions numbers directly:")
cheese_and_crackers(20, 30)

#Now we show how we can define variables, and use them in the function.
print ("OR, we can use variables from our script")

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#This iteration shows how one could perform math operations within the call to a function.
print ("We can do math inside too:")
cheese_and_crackers(10+20, 5+6)

#We can even combine math and variables, assuming that the variables are mumerical in nature.
print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
