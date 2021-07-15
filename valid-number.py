from os import pread


class Solution:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def is_valid_number(number: str) -> bool:
        digit_flag = dot_flag = exponent_flag = False
        count_sign = 0
        n = len(number)
        for i in range(n):
            if number[i].isdigit():
                digit_flag = True
            elif number[i] == '+' or number[i] == '-':
                if count_sign == 2:
                    return False
                if i == n-1:
                    return False
                if i > 0 and not (number[i-1] == 'e' or number[i-1] == 'E'):
                    return False
                count_sign += 1
            elif number[i] == '.':
                if dot_flag == True:
                    return False
                if exponent_flag == True:
                    return False
                if i == n-1 and digit_flag == False:
                    return False
                dot_flag = True
            elif number[i] == 'e' or number[i] == 'E':
                if exponent_flag == True:
                    return False
                if digit_flag == False:
                    return False
                if i == 0 or i == n-1:
                    return False
                exponent_flag = True
            else:
                return False

        return True

if __name__ == '__main__':
    Object = Solution()
    print(Object.is_valid_number(""))