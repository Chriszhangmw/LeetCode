print()
'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''


class Solution:
    def can_change(self, s1, s2):
        num = 0
        flag = True
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num += 1
            if num == 2:
                flag = False
                break
        return flag

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList or endWord not in wordList:
            return 0
        res = []
        self.help(beginWord, endWord, wordList, res)

    def helper(self, beginWord, endWord, wordList, res):
        if len(wordList) == 0:
            return 0

        for i in range(len(wordList)):
            temp = 0
            if self.can_change(beginWord, wordList[i]):
                beginWord = wordList[i]
                temp += 1
                wordList.remove(wordList[i])
                if beginWord == endWord:
                    res.append(temp)
                self.helper(beginWord, endWord, wordList, res)


import collections
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


from collections import defaultdict
import collections


class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        states = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                states[word[:i] + '*' + word[i + 1:]].append(word)

        search = collections.deque([(beginWord, 1)])
        seen = set()
        seen.add(beginWord)
        while search:
            current_node, path = search.popleft()
            # current_word, level = queue.popleft()
            # if current_node not in seen:
            #     seen.add(current_node)
            for i in range(len(current_node)):
                state_word = states[current_node[:i] + '*' + current_node[i + 1:]]
                if len(state_word) > 0:
                    # if endWord in state_word:
                    #     return path + 1

                    for word in state_word:
                        if word == endWord:
                            return path + 1
                        if word not in seen:
                            seen.add(word)
                            search.append((word, path + 1))
                states[current_node[:i] + '*' + current_node[i + 1:]] = []
        return 0


















