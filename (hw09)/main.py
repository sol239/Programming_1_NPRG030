n = input()

n = n.split()[::-1]


def solution(n):
    error_message = "ERROR"
    stack_numbers = []
    stack_operators = []

    for x in n:
        try:
            stack_numbers.append(int(x))
        except ValueError:
            stack_operators.append(x)

    for operator in stack_operators:
        try:
            num_1 = stack_numbers.pop()
            num_2 = stack_numbers.pop()
        except IndexError:
            return error_message

        if operator == "+":
            stack_numbers.append(num_1 + num_2)
        elif operator == "-":
            stack_numbers.append(num_1 - num_2)
        elif operator == "*":
            stack_numbers.append(num_1 * num_2)
        elif operator == "/":
            try:
                stack_numbers.append(num_1 // num_2)
            except ZeroDivisionError:
                return error_message
    if len(stack_numbers) > 1:
        return error_message
    return int(stack_numbers[0])




print(solution(n))