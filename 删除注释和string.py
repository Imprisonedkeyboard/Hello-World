def del_comment_c(self):
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
    # print(write_buf)
    f_out = open(self.dirname, "w")
    f_out.write('\n'.join(write_buf))
    f_out.close()
    f_in.close()
    return