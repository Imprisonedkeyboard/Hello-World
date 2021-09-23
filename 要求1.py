import collections
import re
import os
c_Keywords=["auto","short","int","long","float","while","goto","continue",
            "double","char","struct","union","enum","typedef","const",
            "unsigned","signed","extern","register","static","volatile",
            "void","if","else","switch","for","do","case","break","default",
            "sizeof","return"]

class Countkey():
    def __init__(self,dirname1,level1):
        self.dirname=dirname1
        self.level=level1
        self.keynum = 0
        self.switchnum = 0
    '''
    def Read(self):
        with open(self.dirname, encoding='utf-8') as file:
            text = file.read()
        return text
    '''
    def Find(self):
        with open(self.dirname, encoding='utf-8') as file:
            text = file.read()
            text.split()
            print(text)
        if self.level==1:
            for line in text:
                for i in range(32):
                    if line.find(c_Keywords[i])>=0:
                        print(c_Keywords[i])
                        self.keynum=self.keynum+1
            print("keynums: ",self.keynum)