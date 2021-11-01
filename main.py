import math
import csv

a = [1, "hello world", 3.5] # list

# 打印a
# 求a 元素个数
# 取 第一个元素
# 将第一个元素拆分
# 求拆分的第一个元素的个数

print(a)
print(len(a))
print(a[1])
print(a[1].split())
print(len(a[1].split()))

b = a
print(b)
# 给b加一个元素t
# 给b加一个元素["a", "t,d", "1"]
# 把b最后一位print
b.append("t")
print(b)

b.append(["a", "t,d", "1"])
print(b)
print(b[-1])

d = (1, "hello world", 3.5) #tuple
# 打印d
# 打印d的第一位
# 将tuple转成list

print(d)
print(d[1])
print(list(d))

sets1 = set([1, 2, 3]) #set 元素不能重复
print("set1", sets1)

sets2 = {1, 2, 3}
print("set2", sets2)

dic = {"a": 1, "b": 2, "c": 3} #dict, key: value
#打印dic
# 查询b 的数值
# 计算dic的长度
# 把dic转成list
# 给dic添加元素d=4
# 把b元素改成5

print(dic)
print(dic["b"])
print(len(dic))
print(list(dic.items()))
dic["d"] = 4
print(dic)
dic["a"] = 3
print(dic)

e = [1, 2, 2, 3, 4, 5, 1]
print(set(e))
print(len(set(e)))

a = [1]

def f(x):
    if len(x) >= 2:
        return 10
    elif len(x) ==0 :
        return 100
    else:
        return 9

y = f(a)
x = y** 2 +1
print(x)

arr = [1, 2, 1, 3, 2, 4, 2, 1]
print((sum(list(set(arr)))-len(arr)) *2 )




dic1 = {"abd":1, "abc": 2, "abb":3 }
print("#".join(sorted(dic1.keys())))
g = list(dic1.values())[::-1]
g[1] = math.log(g[1])**3
print(g)


def score(arr):
    if arr >= 90:
        return "A"
    elif arr >= 80:
        return "B"
    else:
        return "C"

f = score(88)
print(f)

#依次平方数相加

def total_score1(arr):
    val = 0
    for i in range(len(arr)):
        val += arr[i]**2
    return val

l = [3, 2, 4, 1]
print("final", total_score1(l))

def total_score(arr):
    val1, val2 = 0, 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            val1 += arr[i]**2
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            continue
        val2 += arr[i]**2
    return val1, val2
l = [3, 2, 4, 1]
print("val1, val2 ", total_score(l))

def square_sum1(arr):
    val1, val2 = 0, 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            val1 += arr[i]**2
    for num in arr:
        if num % 2 == 1:
            continue
        val2 += num
    return val1, val2


s1, s2 = square_sum1(l)
print("s1:", s1, ", s2:", s2)

def swapChar(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] == s[r]:
            break
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s

h = [1, 2, 3, 4]
print(swapChar(h))

def exchange(s):
    l, r = 0, len(s) -1
    while 1 < r:
        if s[l] == s[r]:
            break
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s

j = [3, 3, 4, 6, 6, 9]

print(exchange(j))

d = {"a": [1, 2, 3], "b": [3, 4, 5]}

def sumMid(dic):
    sumVal = 0
    for k, v in dic.items():
        print("k:", k, ", v:", v)
        sumVal += v[1]
    return sumVal

print(sumMid(d))


d1 = {"a": [8, 2, 3], "b": [3, 4, 5]}

def sum1(dic):
    sumval = 0
    for k, v in dic.items():
        sumval += v[0]
    return sumval

print(sum1(d1))

p= ["name, class, score",
    "Peixiu, A, 90",
    "Peixiu, A, 88",
    "Ben, B, 70"]

def dic(arr):
    dic = {}
    for i in range(1, len(arr)):
        _, label, score = arr[i].strip().split(",")
        if label not in dic:
            dic[label] = []
        dic[label].append(float(score))

    score_dic =[]
    for k, v in dic.items():
        score_dic.append([k, str(sum(v)/len(v))])
    return score_dic

print(dic(p))



