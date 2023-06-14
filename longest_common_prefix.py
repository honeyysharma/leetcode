"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    strs.sort(key=len)
    item = strs[0]
    out = ''
    remaining_list = strs[1:]
    for i in range(len(item)):
        if all(item[i]==s[i] for s in remaining_list):
            out += item[i]
        else:
            break

    return out