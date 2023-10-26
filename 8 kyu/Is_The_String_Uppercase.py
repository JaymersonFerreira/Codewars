# DESCRIPTION:
# Is the string uppercase?
# Task
# Create a method to see whether the string is ALL CAPS.

# Examples (input -> output)
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True
# In this Kata, a string is said to be in ALL CAPS whenever it does not contain any 
# lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.


from time import sleep

def is_uppercase(inp):
    for char in inp:
        if char.isalpha() and not char.isupper():
            sleep(0.5)
            return False
    return True

    



print(is_uppercase("c"))
print(is_uppercase("C"))
print(is_uppercase("hello I AM DONALD"))
print(is_uppercase("HELLO I AM DONALD"))
print(is_uppercase("$%&"))

# False
# True
# False
# True
# True
