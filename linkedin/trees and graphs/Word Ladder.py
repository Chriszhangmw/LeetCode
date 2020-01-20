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







'''
python inplement DFS
'''
def depth_first_search():
    order = []
    visited = {}
    def dfs(node):
        visited[node] = True
        order.append(node)
        for n in node.neighbors():
            if n not in visited:
                dfs(n)










