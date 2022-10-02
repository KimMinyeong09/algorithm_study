def slope(p1, p2):
    si = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return si

def slopeSorting(points, pi):
    slopeList = []  # slopeList = list of ((x, y), slope) that sorted by slop
    
    for point in points:
        if point != pi:
            if point[0] == pi[0]:
                slopeList.append((point, float('inf')))
            else:
                slopeList.append((point, slope(point, pi)))

    slopeList = sorted(slopeList, key = lambda p: (p[1]))

    return slopeList

def make4tup(p, q): # p < q
    return (p[0], p[1], q[0], q[1])

def maxColl(col, slopelist, p):    # 점 p를 기준으로 한 slopelist에서 maximal 직선 구하기
    count = 2
    si = 1
    slopeVal = slopelist[0][1]
    temp = [p, slopelist[0][0]]

    while (si < len(slopelist)):
        if slopeVal == slopelist[si][1]:
            temp.append(slopelist[si][0])  
            count += 1
        else:
            if count >= 4:
                temp = sorted(temp, key = lambda p: (p[0], p[1]))
                col.add(make4tup(temp[0], temp[-1]))
            temp = [p, slopelist[si][0]]
            slopeVal = slopelist[si][1]
            count = 2
        si += 1
    
    if count >= 4:
        temp = sorted(temp, key = lambda p: (p[0], p[1]))
        col.add(make4tup(temp[0], temp[-1]))

def collinearPoints(points):
    col = set([])

    for p in points:
        slist = slopeSorting(points, p)
        maxColl(col, slist, p)

    resultLine = sorted(list(col), key = lambda p: (p[0], p[1], p[2], p[3]))

    return resultLine

if __name__ == '__main__':
    # test sample
    li1 = [(19000,10000), (18000,10000), (32000,10000), (21000,10000), (1234,5678), (14000,10000)]
    li2 = [(10000,0), (0,10000), (3000,7000), (7000,3000), (20000,21000), (3000,4000), (14000,15000), (6000,7000)]
    li3 = [(0,0), (1,1), (3,3), (4,4), (6,6), (7,7), (9,9)]
    li4 = [(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (8,0)]
    li5 = [(7,0), (14,0), (22,0), (27,0), (31,0), (42,0)]
    li6 = [(12446,18993), (12798,19345), (12834,19381), (12870,19417), (12906,19453), (12942,19489)]
    li7 = [(1,1), (2,2), (3,3), (4,4), (2,0), (3,-1), (4,-2), (0,1), (-1,1), (-2,1), (-3,1), (2,1), (3,1), (4,1), (5,1)]

    li_my = [(0,0), (1,1), (3,3), (4,4), (6,6), (7,7), (9,9), (1, 2), (-11, 20), (2, 4), (3, 6), (7, 3), (-1, -2)]

    print(collinearPoints(li1))
    print(collinearPoints(li2))
    print(collinearPoints(li3))
    print(collinearPoints(li4))
    print(collinearPoints(li5))
    print(collinearPoints(li6))
    print(collinearPoints(li7))
    print(collinearPoints(li_my))