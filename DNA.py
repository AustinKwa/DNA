#  File: DNA.py

#  Description: Prints out the longest chain of common characters.

#  Student Name: Austin Kwa

#  Student UT EID: ak38754

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 1/20/2022

#  Date Last Modified: 1/20/2022

import sys

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.

def longest_subsequence (s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    temp = []
    longest = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                temp.append(list1[i])
                h = i + 1
                j = j + 1
                
                while h < len(list1) and j < len(list2):
                    if list1[h] == list2[j]:
                        temp.append(list1[h])
                        h = h + 1
                        j = j + 1
                    else:
                        break
            
            if len(temp) == len(longest):
                longest.append(temp)
            elif len(temp) > len(longest):
                longest = [temp]
            temp = []

    return longest

def main():
  # read the number of pairs
  num_pairs = sys.stdin.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)

  # for each pair call the longest_subsequence
  for i in range (num_pairs):
    st1 = sys.stdin.readline()
    st2 = sys.stdin.readline()

    st1 = st1.strip()
    st2 = st2.strip()

    st1 = st1.upper()
    st2 = st2.upper()

    # get the longest subsequences
    long_sub = longest_subsequence (st1, st2)

    # print the result
    if len(long_sub) == 1:
        submit = ""
        for i in range(len(long_sub[i])):
            submit = submit + long_sub[1][i]
        print(submit)
    else:
        for i in range(len(long_sub)):
            submit = ""
            for j in range(len(long_sub[i])):
                submit = submit + long_sub[i][j]
        print(submit)

    # insert blank line

if __name__ == "__main__":  
  main()