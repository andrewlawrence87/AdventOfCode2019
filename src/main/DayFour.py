def matches_code(num):
    res = list(map(int, str(num)))
    for i in range(0, res.__len__() - 1):
        print(res[i])
        if res[i] > res[i + 1]:
            return False
        if res[i] == res[i + 1]:
            if i == 0 | res[i] != res[i - 1]:
                if i + 2 > (res.__len__() - 1) | res[i + 1] != res[i + 2]:
                    return True
    return False


print('Test 1 ' + str(matches_code(112233)))
print('Test 2 ' + str(matches_code(123444)))
print('Test 3 ' + str(matches_code(111122)))

# k = 0
# for i in range(382345, 843167):
#     if matches_code(i):
#         k += 1
# print(k)
