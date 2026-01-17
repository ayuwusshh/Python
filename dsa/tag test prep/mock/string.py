#2. STRINGS (LOGIC HEAVY)
#Q5. First Non-Repeating Character
'''
Given a string, find the first non-repeating character.
If none, print -1.
Input : aabbcdde
Output : c
'''
# from collections import Counter
# s=input()
# freq=Counter(s)
# for ch in s:
#   if freq[ch]==1:
#     ans=ch
#     break
# print(ans)
# print(freq)

#Q7. Longest Substring Without Repeating Characters
'''
Find the length of the longest substring with all unique characters.
Input: abcabcbb
Output: 3
'''
# from collections import Counter
# s=input()
# substr=[]
# for i in range(len(s)):
#   for j in range(i,len(s)):
#     temp=s[i:j+1]
#     substr.append(temp)
# length=0
# ans=0
# for word in substr:
#   freq={}
#   freq=Counter(word)
#   for ch in word:
#     if freq[ch]>1:
#       length=0
#       break
#     else:
#       length=len(word)
#   ans=max(ans,length)
# print(ans)