class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
def insertInToBST(root,ele):
    if root==None:
        newBlock=TreeNode(ele)
        return newBlock


    if root.data<ele:
        root.right=insertInToBST(root.right,ele)
    else:
        root.left=insertInToBST(root.left,ele)
    return root

def printInOrder(root):
    if root == None:
        return
 

    printInOrder(root.left)
    print(root.data, end = " ")
    printInOrder(root.right) 
def searchInBST(root,target):

    if root==None:
        return False
    elif root.data==target:
        return True
    elif root.data<target :
        return searchInBST(root.right,target)
    return searchInBST(root.left,target)
n=int(input())
nums = list(map(int, input().split()))
target=int(input())
root=None
for ele in nums:
    root=insertInToBST(root,ele)
if searchInBST(root,target)==True:
    print("Target element is found")
else:
    print("Target element is not found")
