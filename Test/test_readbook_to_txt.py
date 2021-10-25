f=open("Ni_Kuang.txt",encoding='UTF-8')
content = f.read()
f.close()

content = content.replace("　", "")
# content = content.replace("\n", "")
sentences = content.split("\n")

import jieba
import paddle

paddle.enable_static()#paddle 2.x default改成dynamic，所以要初始設定static
jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持

f=open("test_writebook.txt",'a',encoding='UTF-8')



for i in range(0,len(sentences)):
    seg_list = jieba.cut(sentences[i], cut_all=True)
    f.write("Full Mode: " + "/ ".join(seg_list))

# print(sentences[0])