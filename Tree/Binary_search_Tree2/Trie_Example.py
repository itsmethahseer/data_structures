''' Time is O(n*m) for insertion (n is the number of words, m is the max len), O(m) for search. Space is O(n * m)'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.end_of_word = True
    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.end_of_word
    def starts_with(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True
    def auto_complete(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return []
            current = current.children[letter]
        return self._dfs(current, word)
    def _dfs(self, node, word):
        result = []
        if node.end_of_word:
            result.append(word)
        for letter in node.children:
            result.extend(self._dfs(node.children[letter], word + letter))
        return result
trie = Trie()
trie.insert("haseebmalappuram")
# print(trie.search("haseeb"))
print(trie.auto_complete("has"))
