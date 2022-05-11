class TrieNode(object):
    
    def __init__(self):
        self.children = {}
        self.isEnd = False
        

class WordDictionary(object):

	# same as regular Trie
    def __init__(self):
        self.root = TrieNode()
        
	# same as regular Trie
    def addWord(self, word):
        node = self.root
        
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.isEnd = True

        
    def search(self, word):
	
        self.res = False
        
        
        def track_trie(word, node):
            
            # once the word is found, then return and do not waste time on future search
            if self.res == True:
                return
            
            # if we have compared all the characters in the word, then return true if we found a word, else return false
            if not word:
                self.res = node.isEnd
                return
            
            # for remaining word characters, if it is . ==> it can be any children characters, then track all
            if word[0] == '.':
                for sub_node in node.children.values():
                    track_trie(word[1:], sub_node)
            
            # if the current character is not . ==> regulare trie search
            else:
                # if the current char is not found, return. default is false
                if word[0] not in node.children:
                    return
                
                # if the current char is in the children nodes, then check next char
                track_trie(word[1:], node.children[word[0]])
        
        
        track_trie(word, self.root)
        
        return self.res
