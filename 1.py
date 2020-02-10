"""
 Write a function called decision that takes a string as input, and then checks the number of characters. If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.
"""
def decision(string):
    if len(string.replace(" ",""))>=17:
        return("This is a long string")
    elif len(string.replace(" ",""))<17:
        return("This is a short string")
if __name__=="__main__":
    string=input()
    print(decision(string))
