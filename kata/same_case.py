def same_case(a, b):
    if not (a.isalpha() and b.isalpha()):
        return -1
    if a.islower() == b.islower():
        return 1
    return 0
