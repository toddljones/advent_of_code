from collections import Counter

def check_number(x):
    # at least 2 digits are the same
    if len(str(i)) == len(set(str(i))):
        return None

    # left to right, never decrease
    if list(str(i)) != sorted(str(i)):
        return None
    
    # check that at least 1 digit is repeated twice
    if 2 not in Counter(str(i)).values():
        return None
    
    return i

lbound = 134792
ubound = 675810
output = []
for i in range(lbound, ubound+1):
    if check_number(i):
        output.append(i)

print(len(output))