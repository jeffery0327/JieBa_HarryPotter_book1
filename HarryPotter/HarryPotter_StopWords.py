from collections import Counter
import jieba

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath,'r',encoding="UTF-8").readlines()]
    return stopwords

def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('HarryPotter\Lib_stopwordslist.txt')
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

jieba.load_userdict("HarryPotter\HarrPotter_people.txt")

inputs = open('HarryPotter\HarryPotter.txt','r',encoding="UTF-8")
outputs = open('HarryPotter\HarryPotter_no_stopwords.txt','w',encoding="UTF-8")

for line in inputs:
    line_seg = seg_sentence(line)
    outputs.write(line_seg)
outputs.close()
inputs.close()

with open('HarryPotter\HarryPotter_no_stopwords.txt','r',encoding='UTF-8') as fr:
    data = jieba.cut(fr.read())
data = dict(Counter(data))

with open('HarryPotter\HarryPotter_wordcount.txt','w',encoding='UTF-8') as fw:
    for k,v in data.items():
        fw.write('%s,%d\n' % (k,v))