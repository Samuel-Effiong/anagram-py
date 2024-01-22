# write the function is_anagram
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()

    
    # assuming test is an anagram of original
    flag = True

    if len(test) == len(original):
        new_string = list(test)
        for i in new_string:

            if i in original:
                flag = True
            else:
                flag = False
                break
        
        if flag:
            return True
        else:
            return False
        
    else:
        return False


    
