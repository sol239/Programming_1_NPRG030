n = input()

n = n.split()[::-1]


def solution(n):
    error_message = "ERROR"
    stack = []
    for x in n:

        try:
            x = int(x)
            stack.append(x)
        except ValueError:
            try:
                prvni_cislo = int(stack.pop())
                druhe_cislo = int(stack.pop())
            except IndexError:
                return error_message

            if x == "+":
                stack.append(prvni_cislo + druhe_cislo)
            elif x == "−":
                stack.append(prvni_cislo - druhe_cislo)
            elif x == "*":
                stack.append(prvni_cislo * druhe_cislo)
            elif x == "/":
                try:
                    stack.append(prvni_cislo // druhe_cislo)
                except ZeroDivisionError:
                    return error_message
        print(x)
        print(stack)
        print("-----")
    if len(stack) != 1:
        return error_message

    return int(stack[0])


print(solution(n))