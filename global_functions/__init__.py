def makeStr(array, separator=' '):
    # makes an array into a string
    final = ''
    for item in array:
        # don't add the separator onto the end of the string!
        if array[array.index(item)] != array[len(array)-1]:
            final += item + separator
        else:
            final += item
    return final

def getID(word):
    # gets the ID of a user like <@7856198364>
    word = list(word)
    user_id = ''
    for char in word:
        try:
            user_id += str(int(char))
        except:
            user_id += ''
    return int(user_id)

users_who_can_get_ip = [262637906865291264, 179741296464887808]

owner = 262637906865291264
minh_id = 285546753057619978 
