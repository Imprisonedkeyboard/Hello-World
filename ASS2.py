"""""""""
    先把文件路径导入得到文件，
    第一个等级——找到关键词的个数：
    你要知道哪些是关键词，然后你再去遍历文件，如果出现了关键词，关键词数就加一
    遍历时找switch
    if(那个词==switch)：
        switch数就++
        继续一个for循环找case的数量，找到了就++

"""""""""
import collections
import re
import os
#from pythonds.basic.stack import Stack
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
        self.switchpos = list()
        self.casenum=list()
        self.if_elsenum=0
        self.if_elif_elsenum=0
    '''
    def Read(self):
        with open(self.dirname, encoding='utf-8') as file:
            text = file.read()
        return text
    '''
    def Find(self):
        with open(self.dirname, encoding='utf-8') as file:
            text = file.read()
        if self.level==1:
            dep_1_text = text.replace(";\n", " ;\n")
            dep_2_text = dep_1_text.replace("(", " (")
            dep_3_text = dep_2_text.replace(":\n", " :\n")
            dep_4_text = dep_3_text.replace("{", " {")
            dep_text = dep_4_text.split(" ")
            print(dep_text)
            for words in dep_text:
                if words in c_Keywords:
                    print(words)
                    self.keynum=self.keynum+1
            print("keynums: ", self.keynum)
        elif self.level==2:
            dep_1_text = text.replace(";\n", " ;\n")
            dep_2_text = dep_1_text.replace("(", " (")
            dep_3_text = dep_2_text.replace(":\n", " :\n")
            dep_4_text = dep_3_text.replace("{", " {")
            dep_text = dep_4_text.split(" ")
            print(dep_text)
            '''for line in text:
                while line.find('switch'):
                    pass
                if line.find('switch')>=0:
                    self.switchnum=self.switchnum+1
            print("switchnums: ",self.switchnum)'''
            case_count = []
            switch_num = 0
            for words in dep_text:
                if words == 'switch':
                    case_count.append(0)
                    switch_num += 1
                if words == 'case':
                    case_count[-1] += 1
            print("switchnums: ",switch_num)
            print("casenums: ",case_count)
            '''nowpos=0
            for i in range(0,dep_text.count("switch")):
                #self.casenum[i]='0'
                self.switchpos[i]=dep_text.index('switch',nowpos)
                nowpos=self.switchpos[i]+1
                #if words =='case':
            print(self.switchpos)
            print("switchnums: ", dep_text.count("switch"))
            #print("casenums: ",self.casenum)'''
        elif self.level==3 or self.level==4:
            dep_1_text = text.replace(";\n", " ;\n")
            dep_2_text = dep_1_text.replace("(", " (")
            dep_3_text = dep_2_text.replace(":\n", " :\n")
            dep_4_text = dep_3_text.replace("{", " {")
            dep_5_text = dep_4_text.replace("else if", " elif")
            dep_text = dep_5_text.split(" ")
            print(dep_text)
            elif_state = 0

            s = []
            for words in dep_text:

                if words =='if':
                    s.append(words)
                    print(s)

                if words == 'elif':
                    s.append(words)
                    print(s)
                if words == 'else':
                    for i in range(len(s)):
                        temp = s.pop()
                        print(s)
                        if temp == 'elif':
                            elif_state = 1
                        elif temp == 'if':
                            if elif_state == 1:
                                self.if_elif_elsenum += 1
                            else:
                                self.if_elsenum += 1
                            elif_state = 0
                            break;
            print("if-else nums: ",self.if_elsenum)
            print("if-else if-else nums: ",self.if_elif_elsenum)
    def del_comment_c(self):#删掉原文档的注释和字符串
        f_in = open(self.dirname, "r", encoding='UTF-8')
        write_buf = []
        line = f_in.readline()
        slash_flag = 0
        while line:
            line = line.split("\n")[0]
            if line.find("//") >= 0:
                p = line.split("//")[0]  # 存在返回起始坐标，从0开始，不存在，则返回-1
                if p != "" and (p.isspace() != True):
                    write_buf.append(p)
            elif line.find("/*") >= 0 and line.find("*/") >= 0:
                p = line.split("/*")[0]
                if p != "" and (p.isspace() != True):  # 排除只剩全空格或为空
                    write_buf.append(p)
                p = line.split("*/")[-1]
                if p != "":
                    write_buf.append(p)
            elif line.find("'") >= 0 and line.find("'") >= 0:  # 不看所有字符串，排除字符串中可能含有的keywords
                p = line.split("'")[0]
                if p != "" and (p.isspace() != True):  # 排除只剩全空格或为空
                    write_buf.append(p)
                p = line.split("'")[-1]
                if p != "":
                    write_buf.append(p)
            elif line.find("/*") >= 0:
                p = line.split("/*")[0]
                if p != "":
                    write_buf.append(p)
                slash_flag = 1
            elif line.find("*/") >= 0:
                p = line.split("*/")[-1]
                if p != "" and p != "\n":
                    write_buf.append(p)
                slash_flag = 0
            elif slash_flag == 1:
                line = f_in.readline()
                continue
            else:
                write_buf.append(line)
            line = f_in.readline()
        #print(write_buf)
        f_out = open(self.dirname, "w")
        f_out.write('\n'.join(write_buf))
        f_out.close()
        f_in.close()
        return
file = r'C:\Users\Administrator\Desktop\软工\作业\Lab2示例.c'
myfile = Countkey(file, 3)
myfile.del_comment_c()
myfile.Find()





