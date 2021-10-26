import jieba


def replaceSynonymWords(string1):
    jieba.load_userdict("HarryPotter\Lib_HarryPotter_people.txt")
    jieba.load_userdict("HarryPotter\Lib_HarryPotter_location.txt")
    # 1讀取同義詞表，並生成一個字典。combine_dict = {}
    # synonymWords.txt是同義詞表，
    # 每行是一系列同義詞，用空格分割
    combine_dict = {}
    for line in open("HarryPotter/Lib_HarryPotter_synonymous.txt", "r", encoding='utf-8'):
        seperate_word = line.strip().split(" ")
        num = len(seperate_word)
        for i in range(1, num):
            combine_dict[seperate_word[i]] = seperate_word[0]
            print(seperate_word)
            print(combine_dict)

    # 3將語句切分成單詞
    seg_list = jieba.cut(string1, cut_all=False)

    f = "/".join(seg_list).encode("utf-8")
    f = f.decode("utf-8")
    # print(f)

    # 4返回同義詞替換後的句子
    final_sentence = ""
    for word in f.split('/'):
        if word in combine_dict:
            word = combine_dict[word]
            final_sentence += word
        else:
            final_sentence += word
    f = open("nhjk.txt", 'w', encoding="UTF-8")
    f.write(final_sentence)
    f.close()
    return final_sentence


string1 = open('HarryPotter\HarryPotter.txt', 'r', encoding="UTF-8").read()
print(replaceSynonymWords(string1))
