# You can run this using jupyter notebook if you already pip you can just pip install it pip install jupyter-lab
# or you can use this https://www.programiz.com/python-programming/online-compiler/
# Hoping to hear some feedback and thank you for consideration
#
#Level 1
"""
So first I am using built-in function isspace() to check if the variable have a value of whitespace and at the same time checking if its not empty
There are many ways to solve this problem, loops, built-in function etc, in the v1 of my answer, I use only slice function and conditions
which gives us ability to run through the index of a string, list etc. So this function have a syntax of string[start:end:step]. Step can be positive
or negative, making it negative means that we will start from the end of the string to the begining. After getting the reverse of text, we can just go 
and compare it to the original one using a comparison operator (string equal) to compare character per character and return a True or False

Second approach is by the use of list comprehension, this time I wrote a single line code that will run the exact algorithm as what v1 will do, only
in fewer text. In the v2 of the code we use the expression x to loop in per letter of the string, making all letters in lowercase, split the list, combined it ['something'] and add 
a condition that if the reverse of x is the same as x return a value of true or false.

In this 2 version we can see that even though they provide same output, there is a huge difference in speed, this is all because how we process it . The time complexity for  
v1 is 0(1) and have a space complexity of 0(n) for the slice function that we did for the string or a constant, for v2 we implemented a list comprehension and we know that "for x in var" is equal to 0(n) since we are looping in the string by its letters giving us a 0(n) complexity

Reference below using Jupyter Notebook (%timeit)
v1 = 312 ns ± 12.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
v2 = 661 ns ± 21.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

so in this scenario Ill go with v1 as a final algorithm that I will use as an answer
"""
def palindromes_valid_v1(string):
    if string and not string.isspace():
        reverse = string[::-1] 
        if string == reverse:  
            return True 
        return False 
    return "Check variable value chief" 

def palindromes_valid_v2(string):
    if string and not string.isspace():
        return bool([x for x in string.lower().split() if x == x[::-1]])
    return "Check variable value chief"
#key = 'abcdcba'
#print(palindromes_valid_v2(key))

#level 2
"""
For level 2 I have the same approach, as above first checking if the conditions are met, after that declaring a variable string_length which
have a value of whatever the string length is, so we can avoid calling the function len again and again since we are using nested loop in this approach. Also declaring the palindrome variable that will
store the palindrome inside the string.  Used 2 loops, first, a in range of length of string then b ranging from 0 - a value, and then from there we will do a slice function of the string using b as start and 
a + 1 as stop point and store it in a variable called "part" now next thing to do is to compare if the reverse version of it is equal to itself then return it. Time complexity of this is 0(n^2) as where n is the length
of the string, where in every loop, part value is changing based on b to a + 1, stored/added letters and being evaluated if its the same as the reverse counterpart of it. And by also the Space complexity of this is
0(n) cause the increase of characters will use more memory in constructing a "part" word in proportion to the string value


"""
def is_there_palindrome(string):
    if string and not string.isspace():
        string_length = len(string)
        palindrome = ''
        for a in range(string_length): # a to N
            for b in range(0, a):  # b to (0 to N)
                part = string[b:a + 1] #0(n)
                #check if the part current value is equal to the reverse version of it 
                if part == part[::-1]:
                    #print(str(part) + " " + str(part[::-1]))
                    palindrome = part 
        return palindrome
        
#abc = 'jabccba'
#print(is_there_palindrome(abc))

#Level 3
"""
in level 3 i will use 2 version as well. For the Space complexity this is a 0(n^2) since increase in string characters will also increase
memory allocation needed in arr and min_val. for the Time Complexity this is 0(n^3) we can see that in the runtime. The process for this is
we will declare the string length to a variable to avoid repetition, create a list name arr based on string length and run thru the loop, indicate value of min_val as
i and continue on another loop with range of i+1. From there it will be matching game from characters to characters of the string, if it is match get the min from iterable
and insert it in arr in index i. In the second version I use the level 2 function to check first if the string is palindrome increasing both time and space complexity :)

"""
def how_many_cuts_v1(string):
    if string and not string.isspace():
        string_length = len(string)
        arr = [0 for i in range(string_length)] #0(n)
        for i in range(string_length): #0(n)
            min_val = i #1
            for j in range(i + 1): #0(n)
                #matching string[x] to string[x+1]
                if (string[i] == string[j]):      
                    min_val = min(min_val, 0 if  j == 0 else (arr[j - 1] + 1))
            arr[i] = min_val;   
        return arr[string_length - 1]

def how_many_cuts_v2(string):
    palindrome = is_there_palindrome(string)
    if palindrome:
        string_length = len(string)
        arr = [0 for i in range(string_length)]
        for i in range(string_length):
            min_val = i
            for j in range(i + 1):
                if (string[i] == string[j]):      
                    min_val = min(min_val,0 if  j == 0 else (arr[j - 1] + 1))
            arr[i] = min_val;   
        return arr[string_length - 1]

#var = "noonabbad"
#print(how_many_cuts_v1(var))


#thank you for making me do the exam

