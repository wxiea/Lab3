"""
CS 2302
Lab 3 A 
"""

import math
from AVL import Node 
from AVL import AVLTree
from RBT import RBTNode
from RBT import RedBlackTree
def Number_of_Nodes(Ctree):
    if Ctree is None:
        return 0
    left = Number_of_Nodes(Ctree.left)
    right = Number_of_Nodes(Ctree.right)
    return left + right +1

def Get_Height(Ctree):
    if Ctree == None:
        return -1
    L = Get_Height(Ctree.left)
    R = Get_Height(Ctree.right)
    return max(L,R) + 1

def In_Order(Ctree, file):
    if Ctree == None:
        return    
    In_Order(Ctree.left , file)
    file.write(Ctree.key +"\n")
    In_Order(Ctree.right , file)

def At_Depth(Ctree, file, k):
    if Ctree == None:
        return
    if k != 0:
        At_Depth(Ctree.left, file, k-1)
        At_Depth(Ctree.right, file, k-1)
        return
    file.write(Ctree.key + "\n")
    return
    
def Similarity(filename, Tree):

    with open(filename, encoding ="utf8") as file:
        for line in file:
            values = line.split()
            # the two lines below first search for the words in the tree
            Word_1 = Tree.search(values[0])
            Word_2 = Tree.search(values[1])
            
            # if either of the words is not found then there is no need to compare 
            if Word_1 == None or Word_2 == None:
                print("One of the words was not found Similarity = 0")
                continue
            Word_1_Magnitude = 0
            Word_2_Magnitude = 0
            Dot_Product = 0
            
            # the following block of code follows the equation to find the cosine Distance 
            for i in range(len(Word_1.embedding)):
                Word_1_Magnitude += math.pow(float(Word_1.embedding[i]),2)
                Word_2_Magnitude += math.pow(float(Word_2.embedding[i]),2)
                Dot_Product += float(Word_1.embedding[i]) * float(Word_2.embedding[i])
            Word_1_Magnitude = math.sqrt(Word_1_Magnitude)
            Word_2_Magnitude = math.sqrt(Word_2_Magnitude)
            # cosine distance = Dot product/(magnitude of word 1 *magnitude of word 2)
            likeness = Dot_Product/((Word_1_Magnitude)*Word_2_Magnitude)
            
            print(Word_1.key + " and " + Word_2.key + " have a Simliarity of " + str(likeness))



def Get_Words(filename, Tree):
    Dictionary = Tree
    with open(filename, encoding ="utf8")as file:
        if(isinstance(Tree, RedBlackTree)):
            for line in file:
                values = line.split()
                if values[0][0] < 'a' or values[0][0] > 'z':
                    continue
                name = values.pop(0)
                Dictionary.insert(name, values)
        else:
            for line in file:
                values = line.split()
                if values[0][0] < 'a' or values[0][0] > 'z':
                    continue
                name = values.pop(0)
                NodeC = Node(name, values)
                Dictionary.insert(NodeC)
        return Dictionary

def main():
    request = input("What kind of Binary Tree Would you like to use? (Enter either AVL or RedBlack) ")
    request = request.lower()
    if request == "avl" :
        Tree = AVLTree()
    else:
        Tree = RedBlackTree()
    Tree = Get_Words("glove.6B.50d.txt", Tree)

    print("There are " + str(Number_of_Nodes(Tree.root)) + " nodes in the tree.")

    print("The tree is of height " + str(Get_Height(Tree.root)))

    f = open("Words_Inorder.txt", "w+", encoding ="utf8")
    In_Order(Tree.root, f)
    f.close()

    f = open("Words_At_Depth", "w+", encoding = "utf8")
    Depth = int(input("Enter Desired Depth "))
    At_Depth(Tree.root,f ,Depth)
    
    Similarity("Similarity.txt", Tree)
main()
