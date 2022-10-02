N = 8

ids = []
for idx in range(N):    
    ids.append(idx)

def connected(p, q):
    return ids[p] == ids[q]

def minMax(a, b):
    if a<b: return a,b
    else: return b,a

def union(p, q):
    id1, id2 = minMax(ids[p], ids[q]) # id1 < id2
    for idx, _ in enumerate(ids): # enumerate : 배열의 인덱스, 값을 동시에 반환
        if ids[idx] == id2: ids[idx] = id1 # ids 값이 id2와 같으면 id1으로 바꾸기

'''
Unit Test
'''
if __name__ == "__main__":
    union(4,1)
    print(ids)
    union(4,5)
    print(ids)
    union(2,3)
    print(ids)
    union(6,2)
    print(ids)
    union(3,6)
    print(ids)
    union(3,7)
    print(ids)
    print(connected(1,7))
    union(5,2)
    print(ids)
    print(connected(1,7))
    print(connected(0,6))
    union(0,3)
    print(ids)
    print(connected(0,6))
