from collections import deque
from string import ascii_lowercase
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        unvisited_words = set(wordList)
        unvisited_words.add(beginWord)
        def get_neighbors(word):
            res = []
            for i in range(len(word)):
                for c in ascii_letters:
                    new_word = word[:i]+c+word[i+1:]
                    if new_word in unvisited_words:
                        res.append(new_word)
                        unvisited_words.remove(new_word)
            return res
        queue = deque([beginWord])
        unvisited_words.remove(beginWord)
        depth = 1
        while queue:
            n = len(queue)
            depth += 1
            for _ in range(n):
                word = queue.popleft()
                for w in get_neighbors(word):
                    if w == endWord: return depth
                    queue.append(w)
        return 0
        