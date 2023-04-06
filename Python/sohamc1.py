class BST:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
    
    #function to insert node
    def insert(self,root,val):
        if root is None:
            return BST(val)
        if val < root.val:
            root.left = self.insert(root.left,val)
        else:
            root.right = self.insert(root.right,val)
        return root
    
    #function to find node
    def find(self,root,val):
        if root is None:
            return None
        if val == root.val:
            return root
        if val < root.val:
            return self.find(root.left,val)
        else:
            return self.find(root.right,val)
        
    #function to print tree
    def print_tree(self,root):
        if root is None:
            return
        self.print_tree(root.left)
        print(root.val)
        self.print_tree(root.right)
    
    #function to delete node
    def delete(self,root,val):
        if root is None:
            return None
        if val < root.val:
            root.left = self.delete(root.left,val)
        elif val > root.val:
            root.right = self.delete(root.right,val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                temp = root.left
                while temp.right is not None:
                    temp = temp.right
                root.val = temp.val
                root.left = self.delete(root.left,temp.val)
        return root
    
    #function to find max value
    def max(self,root):
        if root is None:
            return None
        if root.right is None:
            return root.val
        else:
            return self.max(root.right)
    
    #function to find size of subtree
    def size(self,root):
        if root is None:
            return None
        return int(self.size(root.left) or 0)+1+int(self.size(root.right) or 0)
    
#main function
x=BST()
root=None
commands = int(input())
for i in range(commands):
    command=input().split(" ")
    if command[0] == "INSERT":
        try:
            root=x.insert(root,int(command[1]))
        except:
            pass
    elif command[0] == "REMOVE":
        try:
            root=x.delete(root,int(command[1]))
        except:
            pass
    elif command[0] == "SIZE":
        try:
            print (x.size(x.find(root, int(command[1]))))
        except:
            print("None")
    elif command[0] == "MAX":
        try:
            print(x.max(x.find(root, int(command[1]))))
        except:
            print("None")
