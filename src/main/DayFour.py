def matches_code(num):
    res = list(map(int, str(num)))
    match_code = False;
    for i in range(0, res.__len__() - 1):
        if res[i] > res[i + 1]:
            return False
        if res[i] == res[i + 1]:
            if i == 0 or (res[i] != res[i - 1]):
                if (i + 2 > (res.__len__() - 1)) or (res[i + 1] != res[i + 2]):
                    match_code = True
    if match_code:
        return True
    return False

k = 0
for i in range(382345, 843167):
    if matches_code(i):
        k += 1
print(k)
