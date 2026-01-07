# Trie (Prefix Tree) Data Structure Implementation in Python
# Use "python tree_data_structures/trie.py" in the terminal to run this code

# Define a TrieNode class to represent each character node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


# Define a Trie class to manage the trie structure
class Trie:

    # Initialize the trie with a root node
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the trie
    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.is_end_of_word = True

    # Search for a full word in the trie
    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]

        return current.is_end_of_word

    # Check if any word starts with the given prefix
    def starts_with(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True


# Create a Trie and insert words
trie = Trie()

words = ["cat", "car", "cart", "dog"]

for word in words:
    trie.insert(word)

print(trie.search("cat"))      
print(trie.search("cap"))      
print(trie.starts_with("ca"))  
print(trie.starts_with("do"))  
print(trie.starts_with("da"))  
