#function that returns the sum of two numbers
def add_numbers(num1,num2):
    return sum((num1,num2))
    
#function that returns True/False if a number is even or not
def is_even(num):
    return num%2==0

#function that takes in a string and returns its reverse
def reverse_string(string):
    return string[::-1]

#functions that takes a string and returns the count of vowels in the string,ignoring case sensitivity
def count_vowels(string):
    return len([vowel for vowel in string if vowel.lower() in("a","e","i","o","u")])

#function that takes in a non-negative integer and returns the factorial of the integer
def calculate_factorial(num):
    if(num>0):
        result=1
        for i in range(1,num+1):
            result=result*i
        return result

#function that takes in a function and applies a decorator
def apply_decorator(func):
    def decorator_func(*args,**kwargs):
        print("Decorator Applied")
        return func(*args,**kwargs)
    return decorator_func
#application example
@apply_decorator
def funct1(val):
    print(f"{val} after Decorator")
funct1("Hello")
#when called, the output of funct1() is:
    #Decorator Applied
    #Hello after Decorator

#function that sorts a list of tuples by values of a key age
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda item:item[1])


#function that takes two dictionaries and merges them into a single diction,summing up any common values
def merge_dicts(dict1,dict2):
    dict5={} #create an empty dict where merged keys and values will be passed
    #loop through the dicts
    for item in [dict1,dict2]: #use a list containing the dicts so looping is possible
        for key, value in item.items(): #loop through each dict(item) from a combination of the dicts
            dict5[key]=dict5.get(key,0)+value #assign a value of 0 to each key initially and increase it by value of the keys to add values of common keys
    return dict5


#define a class named car that takes in data and prints the car's info
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def display_info(self):
            print(f"Make:{self.make}")
            print(f"Model:{self.model}")
            print(f"Year:{self.year}")