print("输出为：[值,映射加和,[b1,b2,b3,b4,n1,n2,n3,n4]]")
blist = [19,23,26,29]
dictionary = {23 : 5, 19 : 4, 26 : 6, 29 : 7}
s1 = int(input("输入s1: "))
s2 = int(input("输入s2: "))
tar = int(input("输入目标: "))
def calc(b1,b2,b3,b4,n1,n3):
    sum = 0
    sum += dictionary[b1] + dictionary[b2] + dictionary[b3]
    ans = s1 * (b1 * n1 + b2 * (10 - n1)) + 3 * s2 * (n3 * b3 + b4* (3 - n3))
    answer = []
    answer.append(ans)
    answer.append(sum)
    answer.append([b1,b2,b3,b4,n1,10-n1,n3,3-n3])
    return answer
listtarget = []
for b1 in blist:
    for b2 in blist:
        for b3 in blist:
            for b4 in blist:
                for n1 in range(11):
                    for n3 in range(4):
                        listtarget.append(calc(b1,b2,b3,b4,n1,n3))
out = sorted(listtarget,key=lambda x: x[0],reverse=True)
i,end = 0,len(out)
flag = True
while i < end:
    if (out[i][0] <= tar and flag):
        print("------------Your Target is Here------------")
        flag = False
    print(out[i])
    i += 1