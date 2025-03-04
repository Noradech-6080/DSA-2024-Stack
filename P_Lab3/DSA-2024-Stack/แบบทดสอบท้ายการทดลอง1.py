class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def reverse_string_with_stack(input_string):
    stack = Stack()

    for char in input_string: #ใส่ตัวอักษรลงทีละตัว
        stack.push(char)
    reversed_string = "" #ตัวอักษรออกจาก stack ทีละตัวและสร้างข้อความที่กลับลำดับ
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

user_input = input("ป้อนข้อความที่ต้องการกลับลำดับตัวอักษร: ")
reversed_result = reverse_string_with_stack(user_input)
print(f"ข้อความที่กลับลำดับตัวอักษร: {reversed_result}")