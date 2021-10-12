#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):
    res=""
    for i in msg1:
        
        if i in msg2 and i!=" " and i not in res:
            res+=i
    if(not res):
        return -1
        
    return res
    #Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
