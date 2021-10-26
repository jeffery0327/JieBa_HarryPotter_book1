from collections import Counter
import jieba
import jieba.analyse
import jieba.posseg
from wordcloud import WordCloud
import numpy as np
from PIL import Image


# 匯入字典
jieba.load_userdict("HarryPotter\Lib\Lib_HarryPotter_people.txt")
jieba.load_userdict("HarryPotter\Lib\Lib_HarryPotter_location.txt")
jieba.load_userdict("HarryPotter\Lib\Lib_HarryPotter_SentimentPositive.txt")
jieba.load_userdict("HarryPotter\Lib\Lib_HarryPotter_SentimentPositive.txt")


# 讀取停用詞
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath,'r',encoding="UTF-8").readlines()]
    return stopwords

# 去除(停用詞 + 單一字詞) + 分詞
def seg_sentence(content):
    sentence_seged = jieba.cut(content)
    stopwords = stopwordslist('HarryPotter\Lib\Lib_stopwordslist.txt')
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t' and len(word)!=1 :
                outstr += word
                outstr += "/"
    return outstr

# 生成取代同義詞的新文章
def replaceSynonymWords(content):
    # 1讀取同義詞表，並生成一個字典。combine_dict = {}
    # synonymWords.txt是同義詞表，
    # 每行是一系列同義詞，用空格分割
    combine_dict = {}
    for line in open("HarryPotter/Lib/Lib_HarryPotter_synonymous.txt", "r", encoding='utf-8'):
        seperate_word = line.strip().split(" ")
        num = len(seperate_word)
        for i in range(1, num):
            combine_dict[seperate_word[i]] = seperate_word[0]
            # print(seperate_word)
            # print(combine_dict)

    # 3.將語句切分成單詞
    seg_list = jieba.cut(content)
    f = "/".join(seg_list).encode("utf-8")
    f = f.decode("utf-8")
    # print(f)

    # 4.返回同義詞替換後的句子
    final_sentence = ""
    for word in f.split('/'):
        if word in combine_dict:
            word = combine_dict[word]
            final_sentence += word
        else:
            final_sentence += word
    return final_sentence

# 讀取原文
with open('HarryPotter/HarryPotter.txt','r',encoding='UTF-8') as fr:
    content = fr.read()

# 生成新文章
content_new = replaceSynonymWords(content)



#///////////////////////// 功能 /////////////////////////////
# 去除(停用詞 + 單一字詞) + 分詞
words = seg_sentence(content_new)

# 生成文字雲

# 文字雲圖片、字體
mask = np.array(Image.open('HarryPotter/picture/hat.jpg'))
font = 'D:\\mingliu.ttc'

# 設定
my_wordcloud = WordCloud(font_path=font,mask=mask,background_color='white').generate(words)

my_wordcloud.to_file('HarryPotter/picture/result.png')

# # 生成分詞結果文檔
# with open('HarryPotter/Result/HarryPotter_clear.txt','w',encoding='UTF-8') as fw:
#     fw.write(words)

# # 獲取單個詞
# for word in words.split('/'):
#     print(word)

# # 前20名名字
# tags = jieba.analyse.extract_tags(words, topK=20)

# # 生成前20名名字檔案
# with open('HarryPotter/Result/HarryPotter_20name.txt','w',encoding='UTF-8') as fw:
#     for word in tags:
#         fw.write('%s\n' % word)

# 計算出現次數
dict_data = dict(Counter(words.split('/')))

# 刪除唯一出現詞
dict_data_new = {key:value for key,value in dict_data.items() if value != 1}















