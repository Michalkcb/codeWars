'''
I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
'''
def array_plus_array(arr1,arr2):
    la = len(arr1)
    lb = len(arr2)
    result = 0
    for i in range (0, la, 1):
        result +=arr1[i]
    for j in range (0, lb, 1):
        result +=arr2[j]
    return result
