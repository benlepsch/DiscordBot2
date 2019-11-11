banned_channels = ['general']

sohn = { 's':'<:sohn1:625139707453505561>', 'o':'<:sohn2:625139706950189088>','h':'<:sohn3:625139707432402974>','n':'<:sohn4:625139707533328414>' }

sohn_letters = ['s','o','h','n']

def sohn_top():
    return sohn['s'] + sohn['o']

def is_sohn_in_word(word):
    word = list(word)
    for i in range(len(word) - 3):
        if word[i] in sohn_letters:
            issohn = True
            for j in range(4):
                if word[i + j] not in sohn_letters:
                    issohn = False
            if issohn:
                return sohn[word[i]] + sohn[word[i + 1]] + '\n' + sohn[word[i + 2]] + sohn[word[i + 3]]
    return 'not sohn'



def is_sohn_in_word_deprecated(word):
    if 's' in word and 'o' in word and 'h' in word and 'n' in word and len(word) == 4:
        return True
    return False

def get_sohn_config(word):
    # returns false if word isn't a sohn permutation
    # returns the string of the sohn emojis to make his face if it is
    word = list(word)
    if 's' in word and 'o' in word and 'h' in word and 'n' in word and len(word) == 4:
        return sohn[word[0]] + sohn[word[1]] + '\n' + sohn[word[2]] + sohn[word[3]]

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
