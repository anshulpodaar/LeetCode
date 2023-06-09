"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {")": "(", "}": "{", "]": "["}
        check_list = []
        for item in s:
            if item in parentheses_map.values():
                check_list.append(item)
            elif item in parentheses_map.keys():
                if len(check_list) > 0 and check_list[-1] == parentheses_map[item]:
                    check_list.pop(-1)
                else:
                    return False
        if len(check_list) == 0:
            return True
        else:
            return False


def _main():
    print(Solution.isValid(Solution(), "()"))
    print(Solution.isValid(Solution(), "()[]{}"))
    print(Solution.isValid(Solution(), "(]"))

    print(Solution.isValid(Solution(), "{()}"))
    print(Solution.isValid(Solution(), "{(})"))
    print(Solution.isValid(Solution(), "){}"))
    print(Solution.isValid(Solution(), "("))


if __name__ == "__main__":
    _main()
    print("\n#####################\n")


##############################################################################################

# import typing

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


# WRITE IS_BALANCED_PARENTHESES FUNCTION HERE #
def is_balanced_parentheses(s: str) -> bool:
    parentheses_map = {")": "(", "}": "{", "]": "["}
    check_list = Stack()
    for item in s:
        if item in parentheses_map.values():
            check_list.push(item)
        elif item in parentheses_map.keys():
            if check_list.is_empty() or check_list.pop() != parentheses_map[item]:
                return False
    if check_list.is_empty():
        return True
    else:
        return False


###############################################


balanced_parentheses = '((()))'
unbalanced_parentheses = '((())))'

print(is_balanced_parentheses(balanced_parentheses))
print(is_balanced_parentheses(unbalanced_parentheses))

"""
    EXPECTED OUTPUT:
    ----------------
    True
    False

"""