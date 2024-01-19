print("输出为：[值,映射加和,[b1,b2,b3,b4,n1,n2,n3,n4],ans/sum]")
blist = [19,23,26,29]
dictionary = {23 : 5, 19 : 4, 26 : 6, 29 : 7}
s1 = int(input("输入s1: "))
s2 = int(input("输入s2: "))
TargetNum = int(input("输入目标: "))
def calc(b1,b2,b3,b4,n1,n3):
    sum = 0
    sum += n1 * dictionary[b1] + (10 - n1) * dictionary[b2] + n3 * dictionary[b3] + (3 - n3) * dictionary[b4]
    ans = s1 * (b1 * n1 + b2 * (10 - n1)) + s2 * (n3 * b3 + b4* (3 - n3))
    answer = []
    answer.append(ans)
    answer.append(sum)
    answer.append([b1,b2,b3,b4,n1,10-n1,n3,3-n3])
    return answer

def FilterAnswer(out):
    i,end = 0,len(out)
    tmp_sum = 0
    FilteredAns = []
    while i < end:
        if (out[i][0] - TargetNum <= 1000 and TargetNum - out[i][0] <= 1000):
            if(out[i][1] != tmp_sum):
                tmp_line = out[i]
                tmp_line.append(tmp_line[0] / tmp_line[1])
                FilteredAns.append(out[i])
                tmp_sum = out[i][1]
        i += 1
    return FilteredAns

listtarget = []
for b1 in blist:
    for b2 in blist:
        for b3 in blist:
            for b4 in blist:
                for n1 in range(11):
                    for n3 in range(4):
                        listtarget.append(calc(b1,b2,b3,b4,n1,n3))
RawData = sorted(listtarget, key = lambda x: x[0], reverse=True)
Filtered = FilterAnswer(RawData)
Output = sorted(Filtered, key = lambda x: x[3], reverse= True)
for i in Output:
    if(i[0] >= TargetNum):
        print(i)
