# สร้างคลาส Stack
class Stack:
    def __init__(self):
        self.items = []

    # ฟังก์ชันสำหรับการ push ข้อมูล
    def push(self, item):
        self.items.append(item)

    # ฟังก์ชันสำหรับการ pop ข้อมูล
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    # ฟังก์ชันสำหรับการดูข้อมูลบนสุดของ Stack (peek)
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    # ฟังก์ชันเช็คว่า Stack ว่างหรือไม่
    def is_empty(self):
        return len(self.items) == 0

    # ฟังก์ชันสำหรับแสดงข้อมูลใน Stack
    def display(self):
        return self.items

# สร้าง Stack ใหม่
stack = Stack()

# 1. ทดสอบการ push ข้อมูล 5 ตัว
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# 2. แสดงข้อมูลบนสุดของ Stack โดยใช้ peek
print("ข้อมูลบนสุดของ Stack:", stack.peek())

# 3. ทดสอบการ pop ข้อมูลออก 3 ตัว
print("Pop ข้อมูล:", stack.pop())
print("Pop ข้อมูล:", stack.pop())
print("Pop ข้อมูล:", stack.pop())

# 4. แสดงข้อมูลที่เหลือใน Stack
print("ข้อมูลที่เหลือใน Stack:", stack.display())
