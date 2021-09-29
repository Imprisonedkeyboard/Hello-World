elif self.level == 2:
    dep_1_text = text.replace(";\n", " ;\n")
    dep_2_text = dep_1_text.replace("(", " (")
    dep_3_text = dep_2_text.replace(":\n", " :\n")
    dep_4_text = dep_3_text.replace("{", " {")
    dep_text = dep_4_text.split(" ")
    # print(dep_text)
    case_count = []
    switch_num = 0
    for words in dep_text:
        if words == 'switch':
            case_count.append(0)
            switch_num += 1
        if words == 'case':
            case_count[-1] += 1
    print("switchnums: ", switch_num)
    print("casenums: ", case_count)