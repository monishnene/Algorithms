from scramble_support import sort_letters

class Trie:

    def __init__(self,letter_value = None):
        self.letter = letter_value
        self.data = []
        self.branches = []
        
    def add_data(self,path,word):
        print("path = ",path,"word = ",word)
        found = False
        if path == []:
            self.data.append(word)
            print("Added word",word)
            return        
        for node in self.branches:
            if node.letter == path[0]:
                found = True
                break
        if found:
            print("Previous branch found for ",path[0])
            node.add_data(path[1:],word)
        else:
            print("New branch created for ",path[0])
            new_node=Trie(path[0])
            self.branches.append(new_node)
            new_node.add_data(path[1:],word)
        return

    def print_trie(self):
        print("letter value = ",self.letter)
        print("data = ",self.data)
        print("Branches = ",len(self.branches))
        for node in self.branches:
            print("Branch ",self.letter,"->",node.letter)
            node.print_trie()
    
    def check_data(self,path):
        None

root = Trie()    

def word_adder(word):
    path=list(word)
    sort_letters(path)
    root.add_data(path,word)

if __name__ == "__main__":
    word_adder("monish")
    word_adder("hmintu")
    root.print_trie()
