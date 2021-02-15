#element close to mean //
def close_mean(lst):
    sum = 0
    for i in lst:
        sum += i
    mean = sum / len(lst)
    cmp = abs(mean - lst[0])
    for i in lst:
        if abs(mean-i) < abs(cmp):
            cmp = mean - i
            res = i
    return res


#missing number from a list //
def missing_list(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            continue
        else:
            res = lst1[i]
            break
    return res


#elements smaller than mean //
def ele_small_mean(lst):
    sum = 0
    lst2 = []
    for i in lst:
        sum += i
    mean = sum / len(lst)
    for i in lst:
        if mean >= i:
            lst2.append(i)
    return lst2


#difference between 2 lowest numbers in the list //
def diff_lst(lst):
    small = lst[0]
    for i in lst:
        if i < small:
            small = i
    lst.remove(small)
    small2 = lst[0]
    for i in lst:
        if i < small2:
            small2 = i
    
    return small2 - small


#no of elements smaller than mean //
def no_small_mean(lst):
    sum = 0
    res = 0
    for i in lst:
        sum += i
    mean = sum / len(lst)
    for i in lst:
        if mean >= i:
            res += 1
    return res


# no of people in a bus //
def no_bus(n,d1):
    for i in d1.values():
        n += i[0] - i[1]
    return n


# odd one out //
def odd_one(lst):
    for i in range(1,len(lst)):
        if lst[i] != lst[i-1]:
            if lst[i] != lst[i+1]:
                return lst[i]
            else:
                return lst[i-1]


#Average speed of a vehicle (distance in km, time in minutes, speed is in kmph) //
def avg_speed(lst, t): 
    k = len(lst)
    total = lst[0]
    for i in range(k-1):
        total += lst[i+1] - lst[i]
    return round(total/(k*t) * 60, 3)

