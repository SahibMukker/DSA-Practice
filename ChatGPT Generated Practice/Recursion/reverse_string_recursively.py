'''
Write a recursive function reverse_string(s) that takes a string s and returns it reversed.

Ex.
reverse_string("hello") → "olleh"
reverse_string("racecar") → "racecar"
reverse_string("") → ""

Completed in 12 mins 35 secs
'''

def reverse_string(s):
    
    # if the string is empty, return the empty string
    if s == "":
        return ""
    
    # s[1:] takes current string or list or whatever and makes copy of the entire thing starting at index 1 (so index 0 is not included)
    # so this return statement reverses the rest of the string and adds the current first letter to the end of that result
    # ex.
    # reverse_string("cat")
    # → reverse_string("at") + "c"
    # → (reverse_string("t") + "a") + "c"
    # → (("t" + "") + "a") + "c"
    # → "t" + "a" + "c"
    # → "tac"
    return reverse_string(s[1:]) + s[0]

print(reverse_string('hello'))