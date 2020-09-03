def vogal (v):
    if v in "aeiouAEIOU":
        return True
    else:
        return False


print(vogal("a"))
print(vogal("b"))
print(vogal("E"))
print(vogal("x"))