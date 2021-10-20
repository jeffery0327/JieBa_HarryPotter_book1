f=open("Ni_Kuang.txt",encoding='UTF-8')
content = f.read()
f.close()

content = content.replace("　", "")
# content = content.replace("\n", "")
sentences = content.split("\n")


print(sentences)