class TrieNode(object):
    def __init__(self):
        self.is_end=False
        self.next_nodes={}
        
class Trie(object):

    def __init__(self):
        self.is_end=False
        self.next_nodes={}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr_node=self
        for c in word:
            if c not in curr_node.next_nodes:
                curr_node.next_nodes[c]=TrieNode()
            curr_node=curr_node.next_nodes[c]
        curr_node.is_end=True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr_node=self
        for c in word:
            if c in curr_node.next_nodes:
                curr_node=curr_node.next_nodes[c]
            else:
                return False
        return curr_node.is_end
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr_node=self
        for c in prefix:
            if (c) in curr_node.next_nodes:
                curr_node=curr_node.next_nodes[c]
            else:
                return False
        return True
