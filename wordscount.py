from collections import Counter
from zhon.hanzi import punctuation
import string


with open('happiness_seg.txt', 'r', encoding="utf-8") as words_fr:
    word_list = words_fr.read().split()

print("总词数：",len(word_list))
print("词类数：",len(set(word_list)))


# 统计单个词的词频(不包含标点符号)
word1_dic = {}
for i in range(0, len(word_list)):
    if word_list[i] in punctuation:
        continue

    if word_list[i] in word1_dic:
        word1_dic[word_list[i]] += 1
    else:
        word1_dic[word_list[i]] = 1

word1_counter = Counter(word1_dic)
sorted_word1_list = word1_counter.most_common()
with open('word1_count.txt','w', encoding='utf-8') as word1_fw:
    for item in sorted_word1_list:
        word1_fw.write(f"词:{item[0]}\t词频:{item[1]}\n")



# 统计二元词组组数
word2_dic = {}
for i in range(1, len(word_list)):
    # 去除标点符号
    if word_list[i] in punctuation or word_list[i-1] in punctuation:
        continue
    if word_list[i] in string.punctuation or word_list[i-1] in string.punctuation:
        continue
    # 去除中文破折号“——”
    if word_list[i] =="—" or word_list[i-1] == "—":
        continue

    # 限定长度大于1，过滤单个字和标点符号
    # if len(word_list[i-1]) >1 and len(word_list[i])>1:
    word2_str = word_list[i-1] +" "+ word_list[i]
    if word2_str in word2_dic:
        word2_dic[word2_str] += 1
    else:
        word2_dic[word2_str] = 1

word2_counter = Counter(word2_dic)
sorted_word2_list = word2_counter.most_common()
with open('word2_count.txt','w', encoding='utf-8') as word2_fw:
    for item in sorted_word2_list:
        word2_fw.write(f"词:{item[0]}\t词频:{item[1]}\n")
