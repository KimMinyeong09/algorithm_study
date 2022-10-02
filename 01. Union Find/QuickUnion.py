N = 10

ids = []
for idx in range(N):    # ids 초기화
    ids.append(idx)

def root(i):    # root에 도달할 때까지 parent 따라 올라가기
    while i != ids[i]: i = ids[i]
    return i

def connected(p, q):     # root 같은지 확인
    return root(p) == root(q)

def union(p, q):    # p의 root를 q의 root로 바꾸기
    id1, id2 = root(p), root(q)
    ids[id1] = id2    

'''
Unit Test
'''
if __name__ == "__main__":
    union(6,5)
    print(ids)
    union(5,0)
    print(ids)
    union(2,1)
    print(ids)
    union(7,1)
    print(ids)
    union(4,3)
    print(ids)
    union(4,8)
    print(ids)
    union(6,7)
    print(ids)
    union(9,8)
    print(ids)
    union(7,3)
    print(ids)
    print(connected(5,4))
    print(connected(7,9))
