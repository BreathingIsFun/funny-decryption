import re

#set tuples
CHARTUPLE = ("⽂","A")#To determine key of uper case letters
chartuple = ("⽜","a")#To determine key of lower case letters

#helps set character limits to differentiate between upper case encoded characters and lower case encoded characters
def deflimits (encrypted, decrypted, caseA):
    upperbound = (ord(decrypted)-ord(caseA)-25)
    lowerbound = (ord(decrypted)-ord(caseA))
    return (ord(encrypted)-lowerbound,ord(encrypted)-upperbound)



#get the character shift/encryption key
def getkey(encrypted, decrypted):
    return ord(encrypted)-ord(decrypted)

#decode the encryption
def decoder(encrypted, key):
    return chr(ord(encrypted)-key)
    
#just more shitty design
def removejunk (input):
    helper = input.replace("cls", "`").replace("711","´")
    helper = re.sub(r'`.+?´', "", helper)
    return helper

limitBIG = deflimits(*CHARTUPLE, "A")
limitsmall = deflimits(*chartuple, "a")

keyBIG = getkey(*CHARTUPLE)
keysmall = getkey(*chartuple)
   
#checks if the output is sane... if it isn't it returns the original input to prevent conversion of unincrypted characters like numbers, etc.
def sanity (char):
    value = ord(char)
    try: 
        if  limitBIG[0]<= value <=limitBIG[1]:
            testdecode = decoder(char,keyBIG)
            return testdecode
        elif limitsmall[0]<= value <=limitsmall[1]:
            testdecode = decoder(char,keysmall)
            return testdecode
        else:
            return char
    except:
        return char

input = """" """
result = ""
input2 = removejunk(input)
for c in input2:
    result = result+sanity(c)
print(result)