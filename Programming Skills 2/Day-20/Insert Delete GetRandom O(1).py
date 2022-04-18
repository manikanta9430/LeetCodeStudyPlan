from random import choice
class RandomizedSet:
    """
    Randomizes a set using a self balancing dict list 'tree' for O(1) time complexity.
    """
    def __init__(self):
        self.hash = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        else:
            self.hash[val] = len(self.list)
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        
        # remove val from dict, use position to find location in list
        if val in self.hash:
            position = self.hash.pop(val) # pop uses key but grabs value when removing item from dictionary
            item = self.list.pop()
            
            # since list will reduce length by one, take the last item and replace the item at position
            # and update position for that item. This way, other items ahead do not have to change position
            if position != len(self.list):
                self.list[position]=item
                self.hash[item]=position
            return True
        return False
    
    # choice is O(1) complexity. Sample can be used on sets directly but is O(n).
    def getRandom(self) -> int:
        return choice(self.list)
