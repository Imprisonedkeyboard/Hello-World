with open(self.dirname, encoding='utf-8') as file:
    text = file.read()
    dep_1_text = text.replace(";\n", " ;\n")
    dep_2_text = dep_1_text.replace("(", " (")
    dep_3_text = dep_2_text.replace(":\n", " :\n")
    dep_4_text = dep_3_text.replace("{", " {")
    dep_text = dep_4_text.split(" ")