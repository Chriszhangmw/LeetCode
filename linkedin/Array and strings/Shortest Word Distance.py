'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        list1 = []
        list2 = []
        res = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                list1.append(i)
            elif words[i] == word2:
                list2.append(i)

        for i in range(len(list1)):
            for j in range(len(list2)):
                res = min(res, abs(list1[i] - list2[j]))
        return res