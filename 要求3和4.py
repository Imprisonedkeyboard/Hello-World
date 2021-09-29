elif self.level == 3 or self.level == 4:
    dep_1_text = text.replace(";\n", " ;\n")
    dep_2_text = dep_1_text.replace("(", " (")
    dep_3_text = dep_2_text.replace(":\n", " :\n")
    dep_4_text = dep_3_text.replace("{", " {")
    dep_5_text = dep_4_text.replace("else if", " elif")
    dep_text = dep_5_text.split(" ")
    # print(dep_text)
    elif_state = 0
    s = []
    for words in dep_text:
        if words == 'if':
            s.append(words)
        if words == 'elif':
            s.append(words)
        if words == 'else':
            for i in range(len(s)):
                temp = s.pop()
                # print(s)
                if temp == 'elif':
                    elif_state = 1
                elif temp == 'if':
                    if elif_state == 1:
                        self.if_elif_elsenum += 1
                    else:
                        self.if_elsenum += 1
                    elif_state = 0
                    break;
    print("if-else nums: ", self.if_elsenum)
    print("if-else if-else nums: ", self.if_elif_elsenum)