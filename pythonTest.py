from itertools import combinations
import time
import os
start_time = time.time()

arr = []
with open('D:/test/test.txt') as f:
    for line in f:
        if line.strip()!='':
           arr.append("".join(line.split()))
to = 12;
if len(arr)>2:
    numbers_num = arr[0].split(',')
    sums_num = arr[1].split(',')
    to = int(arr[2])
else:
    print('数据获取失败')
    exit()
nums = []
sums = []
numbers = []
for i in range(len(numbers_num)):
    nums.append(float(numbers_num[i]))


for i in range(len(nums)):
    numbers.append(str(nums[i]))

for i in range(len(sums_num)):
    sums.append(float(sums_num[i]))

def groups():
    text_arr = ['','','']
    for i in range(2,to):
        for a in combinations(nums, i):
            b = round(sum(a),2)
            if b == sums[0]:
                text = ''
                for j in a:
                  text += str(j)+' '
                text_arr[0]+= text+"\n"
            elif b == sums[1]:
                text = ''
                for j in a:
                  text += str(j)+' '
                text_arr[1]+= text+"\n"
            elif b == sums[2]:
                text = ''
                for j in a:
                  text += str(j)+' '
                text_arr[2]+= text+"\n"

    paths =  ['D:/test/1.txt','D:/test/2.txt','D:/test/3.txt']

    for k in range(0,3):
        file = open(paths[k],mode='a+')
        file.write(text_arr[k])
        file.close()

def parseFile(path):
    arr = []
    with open(path) as f:
       k=0
       for line in f:
           line_arr = line.split()
           arr.append([])
           for i in range(len(line_arr)):
               arr[k].append(line_arr[i])
           k+=1
    return arr

def the_three():
    path1 = 'D:/test/1.txt'
    path2 = 'D:/test/2.txt'
    path3 = 'D:/test/3.txt'
    arr1 = parseFile(path1)
    arr2 = parseFile(path2)
    arr3 = parseFile(path3)

    a = []
    for item in arr1:
        for item2 in arr2:
            tmp = [val for val in item if val in item2]
            if(len(tmp)==0):
                merge = item+item2
                for item3 in arr3:
                    tmp1 = [value for value in merge if value in item3]
                    if(len(tmp1)==0):
                        a.append(item)
                        a.append(item2)
                        a.append(item3)
    return a


def the_four(data):
    for i in range(len(data)):
        if i%3==0 & i!=len(data):
            merge = data[i]+data[i+1]+data[i+2]
            diff = list(set(numbers).difference(set(merge))) #计算数组差集
            res = open('D:/test/result.txt',mode='a+')
            res.write((','.join(data[i]))+"\n")
            res.write((','.join(data[i+1]))+"\n")
            res.write((','.join(data[i+2]))+"\n")
            res.write((','.join(diff))+"\n\n\n\n")
    res.close()

def delete_file():
    paths= ['D:/test/1.txt','D:/test/2.txt','D:/test/3.txt','D:/test/result.txt']
    for file in paths:
        if os.path.exists(file):
            os.remove(file)

if __name__=='__main__':
    delete_file()
    groups()
    data = the_three()
    the_four(data)
    long_time = int(time.time())-int(start_time)
    print('success for times:',long_time,' s')