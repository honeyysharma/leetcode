"""
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
"""

def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    valid = False
    stack = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        elif i == ')' or i == ']' or i == '}':
            if not stack:
                valid = False
                break
            top = stack[-1]
            if brackets[top] == i:
                valid = True
                stack.pop()
            else:
                valid = False
                break
        else:
            valid = False
            break
    if stack:
        valid = False
    return valid