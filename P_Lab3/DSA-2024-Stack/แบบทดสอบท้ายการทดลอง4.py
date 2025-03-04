class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def is_valid_json(json_string):
    stack = Stack()
    inside_string = False

    for char in json_string:
        if char == '"':
            if not inside_string:
                stack.push(char) #เปิดstring
                inside_string = True
            elif stack.peek() == '"':
                stack.pop() #ปิดstring
                inside_string = False
        elif not inside_string:
            #จัดการวงเล็บที่อยู่นอกstring
            if char in "{[":
                stack.push(char)
            elif char == "}":
                if stack.is_empty() or stack.pop() != "{":
                    return False
            elif char == "]":
                if stack.is_empty() or stack.pop() != "[":
                    return False

    return stack.is_empty() and not inside_string #ตรวจสอบวstackว่าง และไม่มีstring ที่เปิดอยู่

user_input = input("ป้อน JSON string: ")

if is_valid_json(user_input):
    print("JSON string ถูกต้อง")
else:
    print("JSON string ไม่ถูกต้อง")