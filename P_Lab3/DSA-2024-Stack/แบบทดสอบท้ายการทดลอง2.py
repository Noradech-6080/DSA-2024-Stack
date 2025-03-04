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


def decimal_to_binary_stack(decimal_number):
    stack = Stack()
    binary_result = ""
    
    while decimal_number > 0: #เลขฐาน 10 เป็นฐาน 2
        remainder = decimal_number % 2
        stack.push(remainder)
        decimal_number //= 2

    while not stack.is_empty(): #ข้อมูลจากstack มาสร้างเลขฐาน 2
        binary_result += str(stack.pop())

    return binary_result


def decimal_to_hexadecimal_stack(decimal_number):
    stack = Stack()
    hex_result = ""
    hex_map = "0123456789ABCDEF"  #แปลงเลขฐานเป็น 16

    while decimal_number > 0: #เลขฐาน 10 เป็นฐาน 16
        remainder = decimal_number % 16
        stack.push(hex_map[remainder])
        decimal_number //= 16

    while not stack.is_empty(): #ข้อมูลจากstack มาสร้างเลขฐาน 16
        hex_result += stack.pop()

    return hex_result

user_input = int(input("ป้อนตัวเลขฐาน 10: ")) #รับค่าจากผู้ใช้
binary_result = decimal_to_binary_stack(user_input)
hex_result = decimal_to_hexadecimal_stack(user_input)

print(f"เลขฐาน 2: {binary_result}")
print(f"เลขฐาน 16: {hex_result}")