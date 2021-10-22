#將HarryPotter.txt 刪除空格後裡用jieba切字 複寫至 HarryPotter_content_words.txt


f=open("HarryPotter.txt",encoding='UTF-8')
content = f.read()
f.close()

content = content.replace("　", "")

import jieba
import paddle
import jieba.posseg
import jieba.analyse

paddle.enable_static()#paddle 2.x default改成dynamic，所以要初始設定static
jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
jieba.load_userdict("Lib_HarryPotter_people.txt")#匯入自製人名字典



f=open("HarryPotter_content_words.txt",'w',encoding='UTF-8')

seg_list = jieba.cut(content, cut_all=False)
f.write(",".join(seg_list))


print("analyse:")
for x, w in jieba.analyse.extract_tags(content,topK=100, withWeight=True):
    print('%s %s' % (x, w))
