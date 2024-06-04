# -*- coding: utf-8 -*-
"""binary_represent

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qiSVRD1fuasel8Pd97kV8WGyCfHEGUxp

You are given two strings s and t. String t is generated by random shuffling string s and then add one more letter at a random position. Return the letter that was added to t.

Test Case 1:

Input: s = "abcd", t = ”abcde”

Output: "e"

Test Case 2: Input: s = "", t = "y"

Output: "y"
"""

def find_extra_letter(s, t):
    # Initialize dictionaries to store character frequencies
    freq_s = {}
    freq_t = {}

    # Populate freq_s with characters from string s
    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1

    # Populate freq_t with characters from string t
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
    # Iterate through freq_t to find the extra character
    for char, count in freq_t.items():
        if char not in freq_s or count > freq_s[char]:
            return char

# Test cases
print(find_extra_letter("abcd", "abcde"))
print(find_extra_letter("abcd", "abbcde"))
print(find_extra_letter("abcd", "aabbcde"))