

a = input("Enter input A\n\n (T/F) > ")
b = input("\n\nEnter input B\n\n (T/F)> ")

def input_interpreter(value):
    value = value.upper()
    if value == "T":
        return True
    elif value == "F":
        return False

if a.upper() in ("T", "F") and b.upper() in ("T", "F"):
    a = input_interpreter(a)
    b = input_interpreter(b)

    r_and = a and b
    r_or = a or b
    not_a = not a
    not_b = not b
    r_e = a == b
    r_i = (not a) or b
    rr_i = (not b) or a

    print("(AND) A AND B:", r_and)
    print("(OR) A OR B:", r_or)
    print("(NOT A) NOT A:", not_a)
    print("(NOT B) NOT B:", not_b)
    print("(IF...THEN) If A then B:", r_i)
    print("(IF AND ONLY IF) A if and only if B:", r_e)

    input("\n\nPress to generate truth table...")

    print("\n\nAND,  OR,  NOT A, NOT B,  IF...THEN, IF AND ONLY IF")
    print("----------------------------------------------------")
    print(r_and, r_or, ' ' + str(not_a), '  ' + str(not_b), '   ' + str(r_i), '      ' + str(r_e))

print("Enter a valid value")