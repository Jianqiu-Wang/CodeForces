#!/usr/bin/python3
# https://codeforces.com/problemset/problem/1154/A
input_str = input().split(" ")
num_list = [int(x) for x in input_str]
abc = max(num_list)
pop_flag = False
for x in num_list:
    if x == abc and not pop_flag:
        pop_flag = True
        pass
    else:
         print(abc-x, end=" ") 