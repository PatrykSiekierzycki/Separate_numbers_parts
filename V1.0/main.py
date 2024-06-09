"""
Brief: function separate a initiger value from float value of one number.
Param: float
Return:
"""
def separate_digit_number(number:float) -> tuple[int, float]:
    int_part = ""
    float_part = ""
    flag = False
    for char in number:
        if char == ".": flag = True
        if flag == False: int_part += char
        else: float_part += char

    int_part = int(int_part)
    float_part = float(float_part)
    return int_part, float_part
