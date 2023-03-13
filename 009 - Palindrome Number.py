class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        x_str = str(x)
        while len(x_str) > 1:
            if x_str[0] == x_str[-1]:
                x_str = x_str[1:-1]
                if len(x_str) == 0:
                    return True
                x_new = int(x_str)
                Solution.isPalindrome(x_new)
            else:
                return False
        return True


def _main():
    print(Solution.isPalindrome(1234321))
    print(Solution.isPalindrome(12344321))
    print(Solution.isPalindrome(1234564321))
    print(Solution.isPalindrome(1))
    print(Solution.isPalindrome(None))


if __name__ == '__main__':
    _main()
