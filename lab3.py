"""
CS 2302
Lab 3 A 
"""

import math
from AVL import Node 
from AVL import AVLTree
from RBT import RBTNode
from RBT import RedBlackTree
#This is to get the total number of node in AVL or RedBlack
def numNodes(RT):
    if RT is None:
        return 0
    return 1 + numNodes(RT.right) + numNodes(RT.left)
#return height for root
def height(RT):
    if RT is None:
        return -1
    right = height(RT.right)
    left = height(RT.left)
    if left < right:
        return 1 + left
    return 1 + right
"""
#found depth k in the tree
def Depth(RT, file, k):
    if RT is None:
        return
    if k != 0:
        file.write(RT.key + "\n")
        return
    else:
        Depth(RT.left, file, k - 1)
        Depth(RT.right, file, k - 1)
"""
#open the file, read two words
#find the words inthe tree
#if find, print the result    
def Similarity(filename, Tree):
    with open(filename, encoding ="UTF8") as file:
        for line in file:
            values = line.split()
            # the two lines below first search for the words in the tree
            Word1 = Tree.search(values[0])
            Word2 = Tree.search(values[1])           
            # if either of the words is not found then there is no need to compare 
            if Word1 == None or Word2 == None:
                print("err")
                continue
            W1=0
            W2=0
            DotProduct=0           
            # the following block of code follows the equation to find the cosine Distance 
            for i in range(len(Word1.embedding)):
                W1 += math.pow(float(Word1.embedding[i]),2)
                W2 += math.pow(float(Word2.embedding[i]),2)
                DotProduct += float(Word1.embedding[i]) * float(Word2.embedding[i])
            W1 = math.sqrt(W1)
            W2 = math.sqrt(W2)
            # cosine distance = Dot product/(magnitude of word 1 *magnitude of word 2)
            result = DotProduct/((W1)*W2)          
            print(Word1.key + " and " + Word2.key + " have a Simliarity of " + str(result))
#read the file with guven name and create tree
def GetWords(filename, Tree):
    Dictionary = Tree
    with open(filename,encoding ="UTF8")as file:
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
    request = input("AVL or RedBlack ")
    if request == "AVL" :
        Tree = AVLTree()
    else:
        Tree = RedBlackTree()
    Tree = GetWords("glove.6B.50d.txt", Tree)
    print("There are " + str(numNodes(Tree.root)) + " nodes in the tree.")
    print("The tree is of height " + str(height(Tree.root)))
    """
    Thedepth = int(input("Number "))
    with open("words_at_d.txt", "w", encoding='UTF8') as file:
                Depth(Tree, Thedepth, file)
    """
    Similarity("Similarity.txt", Tree)
main()
