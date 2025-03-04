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

def precedence(operator): #กำหนดลำดับโอเปอเรเตอร์
    if operator in ["+", "-"]:
        return 1
    if operator in ["*", "/"]:
        return 2
    if operator == "^":
        return 3
    return 0

def apply_operator(operand1, operand2, operator): #ฟังก์ชันหาเลขสองตัว
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "^":
        return operand1 ** operand2

def evaluate_infix(expression): #ฟังก์ชันหาInfix Expression
    operators = Stack()
    operands = Stack()
    i = 0

    while i < len(expression):
        char = expression[i]

        if char == " ":
            i += 1
            continue

        if char.isdigit(): #ถ้าเป็นตัวเลข ให้ดึงเลขเต็ม
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            operands.push(num)
            continue

        elif char == "(": #ถ้าเป็นวงเล็บเปิดให้push ลงในstack
            operators.push(char)

        elif char == ")": #ถ้าเป็นวงเล็บปิด ให้ประเมินผลในวงเล็บ
            while not operators.is_empty() and operators.peek() != "(":
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                result = apply_operator(operand1, operand2, operator)
                operands.push(result)
            operators.pop()  #เอาวงเล็บเปิดออก

        elif char in "+-*/^": #ถ้าเป็นโอเปอเรเตอร์
            while (
                not operators.is_empty()
                and precedence(operators.peek()) >= precedence(char)
            ):
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                result = apply_operator(operand1, operand2, operator)
                operands.push(result)
            operators.push(char)

        i += 1

    while not operators.is_empty(): #ประเมินผลที่เหลือ
        operator = operators.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()
        result = apply_operator(operand1, operand2, operator)
        operands.push(result)

    return operands.pop()

user_input = input("ป้อน Infix Expression (เช่น 3 + 5 * ( 2 - 8 )): ")
result = evaluate_infix(user_input)
print(f"ผลลัพธ์ของ Infix Expression: {result}")