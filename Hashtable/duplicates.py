def find_duplicate(string):
    table = {}
    for i in string:
        if i in table:
            return True
        else:
            table[i] = True
    return None


string = "hhelo"
print(find_duplicate(string))
