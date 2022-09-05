#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
def reverseStr(string):
    return string[::-1]

#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
def containsWord(containingStr, containedStr):
    report = ""
    if containedStr in containingStr:
        #print("Yes")
        report = "Yes"
    else:
        #print("No")
        report = "No"
    return report

#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
def isPalindrome(string):
    hold = ""
    report = ""
    for i in string:
        hold = i + hold

    if (string == hold):
        #print("Yes")
        report = "Yes"    
    else:
        #print("No")
        report = "No"
    return report

#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
def upperCaseStr(string):
    return string.upper()

