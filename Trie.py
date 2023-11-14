"""A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise."""
 
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  
        self.is_end_of_word = False 

class Trie:
    def __init__(self):
        self.root = TrieNode() 
    def insert(self, word: str) -> None:
        current_node = self.root
        # Traverse the Trie and insert each character of the word
        for char in word:
            char_index = ord(char) - ord("a")  # Calculate the index of the character
            if not current_node.children[char_index]:
                # If the character's node doesn't exist, create a new TrieNode
                current_node.children[char_index] = TrieNode()
            current_node = current_node.children[char_index]  # Move to the next node
        current_node.is_end_of_word = True  # Mark the last node as the end of a word     


    def search(self, word: str) -> bool:
        current_node = self.root
        # Traverse the Trie to find the word
        for char in word:
            char_index = ord(char) - ord('a')
            if not current_node.children[char_index]:
                return False  # Return False if the character doesn't exist
            current_node = current_node.children[char_index]  # Move to the next node

        return current_node.is_end_of_word  # Return True if the word is found


    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        # Check if the Trie contains the given prefix
        for char in prefix:
            char_index = ord(char) - ord('a')
            if not current_node.children[char_index]:
                return False  # Return False if the prefix is not found
            current_node = current_node.children[char_index]  # Move to the next node

        return True  # Return True if the prefix exists in the Trie

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)