import statistics
import math
import random
#import time

ids = []
size = []   # size[i]: size of tree rooted at i

def root(i):
    while i != ids[i]: i = ids[i]
    return i

def connected(p, q):
    return root(p) == root(q)

def union(p, q):    
    id1, id2 = root(p), root(q)
    if id1 == id2: return
    if size[id1] <= size[id2]: 
        ids[id1] = id2
        size[id2] += size[id1]
    else:
        ids[id2] = id1
        size[id1] += size[id2]

def connentObj(N, n, x):   # x의 인접한 열린 객체 확인 및 연결
    isSpecialLine = 0
    if x//n == 0 :   # 첫번째 라인
        union(x, N)
        if ids[x + n] >= 0: union(x, x + n)
    elif x//n == n-1 : # 마지막 라인
        union(x, N + 1)
        isSpecialLine = 1
        if ids[x - n] >= 0 :
            union(x - n, x)
    else:
        if ids[x + n] >= 0: union(x, x + n)
        if ids[x - n] >= 0: union(x - n, x)

    if x%n == n-1 : # 맨 오른쪽 라인
        isSpecialLine = 1
        if ids[x - 1] >= 0: union(x - 1, x)
    elif x%n == 0 :   # 맨 왼쪽 라인
        isSpecialLine = 1
        if ids[x + 1] >= 0: union(x, x + 1)
    else:
        if ids[x - 1] >= 0: union(x - 1, x)
        if ids[x + 1] >= 0: union(x, x + 1)

def calOpenRate(rands, N, n):
    openObj = 0
    
    random.shuffle(rands)

    for idx in range(N):    # ids, size 초기화. close 상태: -1
        ids.append(-1)
        size.append(0)

    ids.append(N)   # 가상 객체 추가
    size.append(1)
    ids.append(N+1)
    size.append(1)

    while (not connected(N, N + 1)):    # percolate할 때까지 반복 
        rand = rands[openObj]
        openObj += 1
        ids[rand] = rand
        size[rand] += 1

        connentObj(N, n, rand)

    openRate = openObj / N
    return openRate

def simulate(n, t):
    rands = []
    rates = []
    N = n * n

    for i in range(N):  # 0 ~ N-1까지의 random num list 생성
        rands.append(i)

    for i in range(t):
        rate = calOpenRate(rands, N, n)
        rates.append(rate)
        ids.clear()
        size.clear()
    
    mean = statistics.mean(rates)
    stdev = statistics.stdev(rates)
    confidenceIntervalLower = mean - 1.96 * stdev / math.sqrt(t)
    confidenceIntervalUpper = mean + 1.96 * stdev / math.sqrt(t)

    print('mean                     = {:0.10f}'.format(mean))
    print('stdev                    = {:0.10f}'.format(stdev))
    print('95% confidence interval = [{:0.10f}, {:0.10f}]'.format(confidenceIntervalLower, confidenceIntervalUpper))
    return mean, stdev

'''
Unit Test
'''
if __name__ == "__main__":
    #start = time.time()
    print(simulate(200,100))
    #print("time :", time.time() - start) 
    #start = time.time()
    simulate(200,100)
    #print("time :", time.time() - start)
    #start = time.time()
    simulate(2,10000)
    #print("time :", time.time() - start)
    #start = time.time()
    simulate(2,100000)
    #print("time :", time.time() - start)