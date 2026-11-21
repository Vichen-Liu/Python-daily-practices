word_count={}
def count_word_frequency():
    with open("D:\\学习\\Python 100题\\Introduction of Jay Chou",encoding="utf-8") as f:
        for line in f.readlines():
            line = line[:-1]
            words=line.split()
            if words:
                for word in words:
                    if word not in word_count:
                        word_count[word]=1
                    else:
                        word_count[word]+=1

    count=sorted(word_count.items(),key=lambda x:x[1],reverse=True)
    print(count[:10])

count_word_frequency()