class Stack:
    def __init__(self): 
        # Stack 클래스 생성자
        self.list = []
    
    def push(self, x):
        # list 마지막에 추가
        self.list.append(x)

    def pop(self):
        # Stack에 가장 마지막으로 추가된 원소를 삭제하며 반환
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop()
    
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())