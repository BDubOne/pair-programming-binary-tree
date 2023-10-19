from collections import deque
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
        
    def __str__(self, level=0):
        def leaf_str():
            return '\t' * (level+1) + 'None\n'

        tree_str = '\t' * level + repr(self.value) + '\n'

        for child in [self.left, self.right]:
            tree_str += child.__str__(level+1) if child else leaf_str()

        return tree_str
    def convert_to_arr(self):
        arr = []
        
        if self.left != None:
            arr.extend(self.left.convert_to_arr())

        arr.append(self.value)

        if self.right != None:
            arr.extend(self.right.convert_to_arr())

        return arr
            
    def tree_search_v(self, value):
        
        if self.value == value:
            return value
        elif self.left is not None and value < self.value:
            
            return self.left.tree_search_v(value)
        
        elif self.right is not None and value > self.value:
        
            return self.right.tree_search_v(value)
        else:
            return None

    def tree_search_l(self):
        pass

    def print_tree(self):
        new_str = ""
        if self.left is not None:
            print("L")
            new_str += self.left.print_tree()
        print(self.value)
        new_str += " " + str(self.value) + " "
        
        if self.right is not None:
            print("R")
        
            new_str += self.right.print_tree()
        
        return new_str
    def dfs(self):
        print(self.value)
        if self.left:
        
            self.left.dfs()
        if self.right:
            self.right.dfs()

    def bfs(self):
        node_queue = deque()
        node_queue.append(self)

        while len(node_queue) > 0:
            current = node_queue.popleft()
            print(current.value)
            if current.left:
                node_queue.append(current.left)
            if current.right:
                node_queue.append(current.right)
        

    
    def insert_node(self, new_tree):
        if new_tree.value < self.value:
            new_tree.left = self.left
            self.left = new_tree
        else:
            new_tree.right = self.right
            self.right = new_tree
        
    def search_and_insert_node(self, new_tree):
        if new_tree.value < self.value:
            if self.left is not None:
                self.left.search_and_insert_node(new_tree)
            else:
                new_tree.left = self.left
                self.left = new_tree
        else:
            if self.right is not None:
                self.right.search_and_insert_node(new_tree)
            else:
                new_tree.right = self.right
                self.right = new_tree

    @staticmethod
    def binary_tree_insert(tree, new_value):
        if tree is None:
            return BinaryTree(new_value)
        
        if new_value < tree.value:
            print(f'new_value: {new_value} < {tree.value}. Going left')
            if tree.left is None:
                tree.left = BinaryTree(new_value)

            else:
                return BinaryTree.binary_tree_insert(tree.left, new_value)
        else:
            print(f"new_value {new_value} >= {tree.value}. Going right")
            if tree.right is None:
                tree.right = BinaryTree(new_value)
            else:
                return BinaryTree.binary_tree_insert(tree.right, new_value)

        return tree        


            


    
    def remove_node_by_value(self,value_removed,parent=None):
       
        if self.left is not None and value_removed < self.value:
            self.left.remove_node_by_value(value_removed, self)
            
        elif self.right is not None and value_removed > self.value:
            self.right.remove_node_by_value(value_removed, self)
        else:
            is_left = True
            if self.left == None:
                is_left = False
            # if value_removed < parent.value:
            #     parent.left = selected_side
            #     selected_side
            # elif value_removed > parent.value:
            #     pass
            # else:
                
            
             
                  


            
    
    def remove_node_by_node():
        #v
        pass
        

    
    # Search
# Print
# Add
# Delete
# 


myTree = BinaryTree(
    56,
    BinaryTree(
        22,
        BinaryTree(10),
        BinaryTree(30)
    ),
    BinaryTree(
        81,
        BinaryTree(77),
        BinaryTree(92)
    )
)
# print(myTree.insert_node(BinaryTree(23)))
# print(myTree.insert_node(BinaryTree(57)))
# print(myTree.insert_node(BinaryTree(23)))
# print(myTree.convert_to_arr())
# print(myTree.tree_search_v(77))
# print()
myTree2 = BinaryTree(50)
# myTree2.search_and_insert_node(BinaryTree(60))

# myTree2.search_and_insert_node(BinaryTree(40))
# myTree2.remove_node_by_value(50)

# print(myTree2.convert_to_arr())
# print(myTree2.print_tree())
# print(myTree2)
myTree3 = BinaryTree(50)

BinaryTree.binary_tree_insert(myTree3,23)
BinaryTree.binary_tree_insert(myTree3,23)
BinaryTree.binary_tree_insert(myTree3,30)
BinaryTree.binary_tree_insert(myTree3,10)
BinaryTree.binary_tree_insert(myTree3,20)
BinaryTree.binary_tree_insert(myTree3,40)
BinaryTree.binary_tree_insert(myTree3,90)
BinaryTree.binary_tree_insert(myTree3,80)
BinaryTree.binary_tree_insert(myTree3,60)
BinaryTree.binary_tree_insert(myTree3,55)
BinaryTree.binary_tree_insert(myTree3,22)

myTree2.search_and_insert_node(BinaryTree(23))
myTree2.search_and_insert_node(BinaryTree(23))
myTree2.search_and_insert_node(BinaryTree(30))
myTree2.search_and_insert_node(BinaryTree(10))
myTree2.search_and_insert_node(BinaryTree(20))
myTree2.search_and_insert_node(BinaryTree(40))
myTree2.search_and_insert_node(BinaryTree(90))
myTree2.search_and_insert_node(BinaryTree(80))
myTree2.search_and_insert_node(BinaryTree(60))
myTree2.search_and_insert_node(BinaryTree(55))
myTree2.search_and_insert_node(BinaryTree(22))
print(myTree2)
print(myTree3)
# print(myTree2.bfs())
# print(myTree2.dfs())