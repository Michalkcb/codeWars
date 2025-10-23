'''
Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

Some cases:
[22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]

[68, -1, 1, -7, 10, 10] => [-1, 10]

[-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]
'''

def multiple_of_index(arr):
    results = []
    # osobna obsługa indeksu 0
    if arr and arr[0] == 0:
        results.append(arr[0])

    # osobna pętla dla pozostałych indeksów 1..n-1
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            results.append(arr[i])

    return results
