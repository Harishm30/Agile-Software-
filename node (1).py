class Node():
  def __init__(self,val):
    self.val = val
    self.next = next 
s = Node(1,Node)
print(s.val,s.next) 

s2 = Node(2,Node)
print(s.val,s.next) 
s.next = s2
print("Connected list",s.val,s.next)

print(s.next.val)
print(s.next.next)