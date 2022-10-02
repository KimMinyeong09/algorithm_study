import math

# convex인지 확인
def ccw(i, j, k):
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area2 > 0: return True
    else: return False

# points 중에서 점 p 반환
# p는 y값이 가장 작은 점 중 x값이 가장 큰 점
def findP(points):
    li = sorted(points, key = lambda p: (p[1], -p[0]))
    return li[0]

# angWithP: ((x, y), ang) 리스트
# ang로 sort
# pPoint의 성질로 인해 ang>=0
def sortByAngle(pPoint, points):
    angWithP = []

    for a in points:
        ang = math.atan2(a[1] - pPoint[1], a[0] - pPoint[0])
        angWithP.append((a, ang))
    sortLi = sorted(angWithP, key = lambda p: (p[1], p[0][0], -p[0][1]))
    return sortLi

def grahamScan(points):
    convexHull = []
    p = findP(points)
    sortPoints = sortByAngle(p, points)
    sortPoints.append(sortPoints[0])
    kIndex = 2

    convexHull.append(sortPoints[0][0])

    i= convexHull[0]
    j = sortPoints[1][0]
    
    while (kIndex < len(sortPoints)):
        k = sortPoints[kIndex][0]
        if j != convexHull[-1]:
            convexHull.append(j)
        if ccw(i, j, k):
            i, j = j, k
            kIndex += 1
        else:
            convexHull.pop()
            i, j= convexHull[-2], i
    return convexHull

if __name__ == '__main__':
    # ccw turns
    print(ccw((0, 0), (-1, 1), (-2, -1)))

    # non-ccw turns
    print(ccw((0, 0), (-2, 1), (-1, 1)))
    print(ccw((0, 0), (-1, 1), (-2, 2)))    # Straight Line

    print()

    # test gramhamHull
    print(grahamScan([(0 ,0), (-2, -1), (-1, 1), (1, -1), (3, -1), (-3, -1)]))
    print()
    print(grahamScan([(0 ,0), (-2, -1), (-1, 1), (1, -1), (3, -1), (-3, -1), (5, 2), (-2, 2), (0, -3), (6, -2), (4, 1), (3, 0), (-6, 1)]))
    print()
    print(grahamScan([(4,2),(3,-1),(2,-2),(1,0),(0,2),(0,-2),(-1,1),(-2,-1),(-2,-3),(-3,3),(-4,0),(-4,-2),(-4,-4)]))