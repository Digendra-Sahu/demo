# reversing a number //
def reverse_num(n):
    res = 0
    i = 0
    k = n
    while k > 0:
        i += 1
        k //= 10
    while n > 0:
        rem = n%10
        n //= 10
        i -= 1
        res += rem*pow(10,i)
    return res

# roots of quad equation //
def root_quad(a,b,c):
    det = b**2 - 4*a*c
    if det == 0:
        return -b/(2*a), -b/(2*a)
    else:
        return (-b+det**0.5)/(2*a), (-b-det**0.5)/(2*a)


#list and count of a prime nos //
def prime_all(a,b):
    lst1 = []
    def isprime(n):
        if n > 2:
            for i in range(2, n//2+1):
                if n%i == 0:
                    return False
            return True
        elif n == 2:
            return True

    for i in range(a, b+1):
        if isprime(i):
            lst1.append(i)
    return lst1, len(lst1)

#PRIME NOS //
def isprime(n):
    if n == 0 or n == 1:
        return False
        
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

#leap year //
def leap_year(n):
    if n%100 == 0:
        if n%400 == 0:
            return True
        else:
            return False
    else:
        if n%4 == 0:
            return True
        else:
            return False

#factorial of a number //
def fact(n):
    res = 1
    if n >= 1:
        for i in range(1, n+1):
            res *= i
    return res

#sum of the factors //
def fact_sum(n):
    res = 0
    for i in range(1, n+1):
        if n % i == 0:
            res += i
    return res

#Largest of numbers //
def largest(lst1):

    large = lst1[0]
    for i in range(len(lst1)):
        if lst1[i] > large:
            large = lst1[i]
    
    return large

#Sum of Digits //
def sum_of(lst1):
    n = 0
    for i in range(lst1):
        n += i
    return n


#armstrong number //
def armstrong_num(n):
    res = 0
    k = n
    d = 0
    while k>0:
        k //= 10
        d += 1
    k = n
    while k>0:
        rem = k%10
        k //= 10
        res += pow(rem, d)

    return res == n

#LCM of 2 numbers //
def lcm(a, b):
    if a >= b:
        larger = a
    else:
        larger = b
    
    while True:
        if larger%a == 0 and larger%b == 0:
            break
        else:
            larger += 1
    return larger
                

#HCF of 2 numbers //
def hcf(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
    
    while smaller > 0:
        if a%smaller == 0 and b%smaller == 0:
            break
        else:
            smaller -= 1
    return smaller

#vowel or consonant //
def vow_cons(n):
    if n == "a" or "e" or "i" or "o" or "u":
        return True
    else:
        return False

#Triangle condition //
def type_triangle(a,b,c):
    i = lambda a,b,c: a+b > c and b+c > a and c+a > b
    if i:
        if a == b and a == c: #EQUILATERAL
            return 1
        elif a == b or b == c or a == c: #ISOSCELES
            return 2
        elif a**2 == b**2 + c**2 or a**2 + b**2 == c**2 or c**2 + a**2 == b**2: #RIGHT ANGLED
            return 3
        else: #SCALENE
            return 4
    else:
        return 0

#quadrant of a point on plane //
def quadrant(x,y):
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3

#trianglular sum of a nunber //
def triang_num(n):
    res = 0
    while n > 0:
        i = 1
        while i <= n:
            res += i
            i += 1
        n -= 1
    return res
    
#pascal triangle //
def pascal(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print(int(ncr(i,j)), end=' ')
        print("\n")

#digital root //
def digi_root(n):
    k = n
    res = 0
    while k > 0:
        rem = k%10
        k //= 10
        res += rem
    while res // 10 != 0:
        res = digi_root(res)
    return res

#ncr //
def ncr(n,r):
    return fact(n)/(fact(n-r)*fact(r))


#fibonacci //
def fibonacci(n):
    lst = []
    a,b = 0,1
    while n>0:
        c = a+b
        a = b
        b = c
        n -= 1
        lst.append(a)
    return a, lst

# using recursion
def recur_fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n > 1:
        return recur_fibo(n-1) + recur_fibo(n-2)

#tribonacci //
def tribonacci(n):
    a,b,c = 0,0,1
    while n > 0:
        d = a + b + c
        a = b
        b = c
        c = d
        n -= 1
    return b


#generate super prime nos 
def super_prime(n):
    lst = prime_all(2, n)[0]
    lst2 = []
    for i in range(len(lst)):
        if isprime(i+1):
            lst2.append(lst[i])
    return lst2

print(super_prime(20))




#maximum nos by deleting a single digit //
def max_del_4(num):
    lst = []
    k = str(num)
    for c in k:
        lst.append(int(k.replace(c, '')))

    return max(lst)


#choice based arithmetic //
def ch_arith(a,b,c):
    if c == "+":
        return a+b
    elif c == "-":
        return a-b
    elif c == "*":
        return a*b
    elif c == "/":
        return a/b
    elif c == "%":
        return a%b
    else:
        return None

#number triangle //
def number_tri(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print("\n")

#number pyramid //
def number_pyr(n):

    s = n - 1

    for i in range(1, n+1):
        for j in range(0, s):
            print(end=" ")
        s -= 1
        for j in range(1, i+1):
            print(j, end=".")
        
        print("\n")

