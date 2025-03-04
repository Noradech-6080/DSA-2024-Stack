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


def evaluate_postfix(expression):
    stack = Stack()

    for char in expression.split():
        if char.isdigit():  #เป็นตัวเลข
            stack.push(int(char))
        else:  #เป็นโอเปอเรเตอร์
            operand2 = stack.pop() #ดึงค่าจาก stack สองค่า
            operand1 = stack.pop()

            #คำนวณตามโอเปอเรเตอร์
            if char == "+":
                stack.push(operand1 + operand2)
            elif char == "-":
                stack.push(operand1 - operand2)
            elif char == "*":
                stack.push(operand1 * operand2)
            elif char == "/":
                stack.push(operand1 / operand2)
            elif char == "%":
                stack.push(operand1 % operand2)
            elif char == "**":
                stack.push(operand1 ** operand2)

    return stack.pop()

user_input = input("ป้อน Postfix Expression (ตัวเลขและเครื่องหมายคั่นด้วยช่องว่าง): ")
result = evaluate_postfix(user_input)
print(f"ผลลัพธ์ของ Postfix Expression: {result}")