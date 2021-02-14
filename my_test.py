from assign_1pyth import *
from assign_2pyth import *
from assign_3pyth import *
import pytest

def test_func():
    assert reverse_num(3456) == 6543
    assert reverse_num(122310) == 13221
    assert reverse_num("439832") == None

def test2_func():
    assert root_quad(1,-5,6) == (3,2)
    assert root_quad(1,-2,1) == (1,1)

def test3_func():
    assert prime_all(2, 25) == ([2, 3, 5, 7, 11, 13, 17, 19, 23], 9)
    assert prime_all(1, 100) == ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 25)

def test4_func():
    assert isprime(2) == True
    assert isprime(1) == False
    assert isprime(-2) == False

def test5_func():
    assert leap_year(2016) == True
    assert leap_year(1900) == False
    assert leap_year(1600) == True
    assert leap_year(1922) == False

def test6_func():
    assert fact(4) == 24
    assert fact(8) == 40320
    assert fact(10.1) == None
    assert fact(0) == 1
    assert fact(-1) == None

def test7_func():
    assert fact_sum(30) == 72
    assert fact_sum(20) == 42

def test8_func():
    assert largest([1,2,3,4,5]) == 5
    assert largest([3,-3,6,0,1]) == 6
    assert largest(["0",1,2,9]) == None

def test9_func():
    assert sum_of([1,3,4,7]) == 15
    assert sum_of([0,-1,3,9,11]) == 22

def test10_func():
    assert armstrong_num(1729) == False
    assert armstrong_num(153) == True
    assert armstrong_num(-11) == False

def test11_func():
    assert lcm(9,8) == 72
    assert lcm(1,9) == 9
    assert lcm(5,25) == 25

def test12_func():
    assert hcf(5,7) == 1
    assert hcf(2,8) == 2

def test13_func():
    assert vow_cons("a") == True
    assert vow_cons("b") == False

def test14_func():
    assert type_triangle(3,4,5) == 3
    assert type_triangle(1,2,4) == 4
    assert type_triangle(2,2,3) == 2

def test15_func():
    assert quadrant(1,1) == 1
    assert quadrant(2,-1) == 4
    assert quadrant(1,0) == None

def test16_func():
    assert triang_num(5) == 35
    assert triang_num(8) == 120 
    assert triang_num(-12) == 0

def test18_func():
    assert digi_root(3821516) == 8
    assert digi_root(-23132) == None

def test19_func():
    assert ncr(5,2) == 10
    assert ncr(3,1) == 3
    assert ncr(8,0) == 1
    assert ncr(0,0) == 1

def test20_func():
    assert fibonacci(7) == (13, [1, 1, 2, 3, 5, 8, 13])
    assert fibonacci(10) == (55, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])      


def test21_func():
    assert tribonacci(8) == 44
    assert tribonacci(10) == 149

def tes22_func():
    assert super_prime(20) == [3,5,11,17]
    assert super_prime(50) == [3,5,11,17,31,41]

def test23_func():
    assert max_del(7319) == 739
    assert max_del(57129) == 7129

def test24_func():
    assert max_del_4(9010) == 900
    assert max_del_4(7811) == 811

def test25_func():
    assert ch_arith(1,2,'+') == 3
    assert ch_arith(8,3,'-') == 5
    assert ch_arith(5,2,'/') == 2.5

# Printed pattern (Triangle and Pyramid to be observed manually)


def test26_func():
    assert close_mean([1,2,3,4,5]) == 3
    assert close_mean([1,0,2,9,11]) == 2

def test27_func():
    assert missing_list([1,2,3], [2,3]) == 1
    assert missing_list([1,2,1,0,1], [1,2,0,1]) == 1

def test28_func():
    assert ele_small_mean([1,2,3,4,5]) == [1,2,3]
    assert ele_small_mean([1,2,0,1,9]) == [1,2,0,1]

def test29_func():
    assert diff_lst([1,2,3,4,5]) == 1
    assert diff_lst([2,4,0,1,1]) == 1

def test30_func():
    assert no_small_mean([1,2,3,5]) == 2
    assert no_small_mean([1,2,3,4,1,1,2,-1]) == 4

def test31_func():
    assert no_bus(25,{1:(2,5), 2:(9,6), 3:(8,4)}) == 29
    assert no_bus(11,{1:(0,2), 2:(10,11)}) == 8

def test32_func():
    assert odd_one([1,2,1,1,1,1]) == 2
    assert odd_one([3,1,1,1,1]) == 3

def test33_func():
    assert avg_speed([1, 2, 1.1, 1.6, 0.9], 6) == 10.8
    assert avg_speed([0.1, 0.9, 2.1, 3.2, 0.9, 1.1], 4) == 11.0

def test34_func():
    assert isogram("mithun") == True
    assert isogram("chinmai") == False
    assert isogram("python") == True

def test35_func():
    assert iptoint("192.168.1.251") == 1921681251
    assert iptoint(192112134251) == "192.112.134.251."

def test36_func():
    assert word_frequency("a cat a bat and a rat") == {'a': 3, 'cat': 1, 'bat': 1, 'and': 1, 'rat': 1}
    assert word_frequency("can i come in i am tired ?") == {'can': 1, 'i': 2, 'come': 1, 'in': 1, 'am': 1, 'tired': 1, '?': 1}

def test37_func():
    assert lar_shuff

def test38_func():
    assert malf_time

def test39_func():
    assert mal_date

def test40_func():
    assert rgb_to_hex

def test41_func():
    assert accum_str("abcd") == "A-Bb-Ccc-Dddd"
    assert accum_str("mithun") == "M-Ii-Ttt-Hhhh-Uuuuu-Nnnnnn"

def tes42_func():
    assert mexican("hello") == ['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']
    assert mexican("Messi") == ['Messi', 'mEssi', 'meSsi', 'mesSi', 'messI']