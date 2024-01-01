def freq(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] +=1
        else:
            dict[n] = 1

    return dict


str = input().strip()
print(freq(str))

