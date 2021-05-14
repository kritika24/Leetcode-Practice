'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
'''

class Solution:
    def reverse(self, x: int) -> int:
        x_str=str(x)
        if x<0:
            x_str='-'+x_str[::-1][:-1]
            x=int(x_str)
            x_and=x&-0x80000000
            if x_and==-0x80000000:
                return x
            else:
                return 0
        elif x==0:
            return 0
        else:
            x=int(x_str[::-1])
            x_and=x&0x7fffffff
            if x_and==x:
                return x
            else:
                return 0
