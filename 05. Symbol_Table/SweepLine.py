from queue import PriorityQueue
from RedBlackBST import LLRB

class Segment:
    def __init__(self, x1, y1, x2, y2): # (x1, y1), (x2, y2)를 연결하는 직선
        assert(x1==x2 or y1==y2) # Accept either a horizontal or vertical segment  
        assert(not (x1==x2 and y1==y2)) # Two end points cannot be equal              

        # Put smaller values in (x1,y1) and larger values in (x2,y2)
        # x1 < x2 이거나 y1 < y2 임
        if x1==x2: # 수직선
            if y1<y2: self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
            else: self.x1, self.y1, self.x2, self.y2 = x1, y2, x2, y1
        elif y1==y2: # 수평선
            if x1<x2: self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
            else: self.x1, self.y1, self.x2, self.y2 = x2, y1, x1, y2
    
    def isHorizontal(self): # 수평선인지 확인
        return self.y1 == self.y2

    def isVertical(self): # 수직선인지 확인
        return self.x1 == self.x2

    # Create a human-readable string representation
    def __str__(self):
        return f"({self.x1},{self.y1})--({self.x2},{self.y2})"

    def __repr__(self): # Called when a Segment is printed as an element of a list
        return self.__str__()

    # Defines behavior for the equality operator, ==
    # This operator is required for grading
    def __eq__(self, other):
        if other == None: return False
        if not isinstance(other, Segment): return False        
        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2

'''
segments: list of Segment objects
return value: list of Segment pairs that intersect
'''
def sweepLine(segments):
    pq = PriorityQueue() # minPQ 생성
    bst = LLRB() 
    result = []

    for i in segments:
        #print(i)
        if i.isHorizontal():
            pq.put((i.x1, i))
            pq.put((i.x2, i))
        else:
            pq.put((i.x1, i))
    
    while pq.qsize():
        e = pq.get()
        if e[1].isHorizontal():
            if e[0] == e[1].x1: # 수평선에서 왼쪽 점
                bst.put(e[1].y1, e[1]) # table에 y좌표 추가
            elif e[0] == e[1].x2: # 수평선에서 오른쪽 점
                bst.delete(e[1].y1) # table에서 y좌표 제거
        else: # 수직선
            temp = bst.rangeSearch(e[1].y1, e[1].y2) # 수직선의 y 범위에 대해 교차점 확인
            for i in temp:
                x  = bst.get(i)
                result.append((x, e[1]))
    
    return result

if __name__ == "__main__":
    '''
    3 intersections found
    (1,4)--(8,4) (6,3)--(6,7)
    (9,6)--(16,6) (13,5.5)--(13,9.5)
    (0,1)--(15,1) (14,0)--(14,2)
    '''    
    intersections = sweepLine([Segment(0,1,15,1), Segment(14,0,14,2), Segment(1,4,8,4), Segment(6,3,6,7),\
        Segment(2,5,4,5), Segment(3,8,11,8), Segment(9,6,16,6), Segment(13,5.5,13,9.5)])
    print(intersections)    
    print()
    
    # Grading example utilizing __eq__() operator
    if intersections == [(Segment(1,4,8,4),Segment(6,3,6,7)),(Segment(9,6,16,6),Segment(13,5.5,13,9.5)),\
        (Segment(0,1,15,1),Segment(14,0,14,2))]:
        print("True")
    print()

    '''
    6 intersections found
    (1,3)--(6,3) (5,0)--(5,9)
    (4,7)--(9,7) (5,0)--(5,9)
    (4,7)--(9,7) (8,6)--(8,10)
    (11,2)--(17,2) (12,1)--(12,5)
    (10,4)--(13,4) (12,1)--(12,5)
    (14,6.5)--(16,6.5) (15,5.5)--(15,7.5)
    '''
    intersections = sweepLine([Segment(1,3,6,3), Segment(5,0,5,9), Segment(4,7,9,7), Segment(8,6,8,10),\
        Segment(10,4,13,4), Segment(11,2,17,2), Segment(12,1,12,5), Segment(15,5.5,15,7.5), Segment(14,6.5,16,6.5)])    
    print(intersections)
    