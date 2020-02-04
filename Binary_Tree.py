# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 00:51:06 2019

@author: Zainey
"""
import timeit

class node:
    def __init__(self, value):
            self.value= value
            self.left= None
            self.right= None
    def child_node(self,n):
        if self.value > n.value:
            if self.left==None:
                self.left=n
            else:    
                self.left.child_node(n)
        elif self.value < n.value:
            if self.right==None:
                self.right=n
            else:    
                self.right.child_node(n)
    def visit(self):
        
            
        
        if self.left!=None:
            self.left.visit()
        print(self.value) 
        if self.right!=None:
            self.right.visit()  
            
    def find(self,val):
        
        if val==self.value:
            print("found value "+str(val) )
        elif val<self.value and self.left !=None:
           
            self.left.find(val)
            
        elif val>self.value and self.right !=None:
           
            self.right.find(val) 
        else:
            print("value not found")
       
       
        
         
        
             
            
        


class tree:
    def __init__(self):
            self.root=None
            
    def add_node(self,n):
        p=node(n)
        if self.root == None:
                self.root=p
        else: 
            self.root.child_node(p)
    def traverse(self):
        self.root.visit()
        
    def search(self,val):
        self.root.find(val)
        
        
    
        
        
T1=tree()


b1= T1.add_node(9)
b2= T1.add_node(4)
b3= T1.add_node(7)
b4= T1.add_node(111)
b5= T1.add_node(5)
b6= T1.add_node(34)



T1.traverse()
T1.search(5)
       

