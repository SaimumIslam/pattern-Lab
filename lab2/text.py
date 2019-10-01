class Data(object):
    def __init__(self, category=None, bio=None,freq=1):
        self.category = category
        self.bio = bio
        self.freq=freq

class ResultData(object):
    def __init__(self, category=None, prob=0, total_word=0, word_freq=None):
        self.category = category
        self.prob = prob
        self.total_word=total_word
        self.word_freq=word_freq


def remove_stopwords(data):
    file=open('stopwords.txt','r')
    stopwords = file.read().split()

    data = data.replace(',', '')
    data = data.replace('.', '')
    data = ' '.join(i for i in data.split() if i not in stopwords)
    return data


def retrive_data(file):
    data_list = []
    cls_list = []
    lines=file.readlines()
    i=0
    description=[]
    cls=""
    for line in lines:
        i=i+1
        line=line.strip()
        if not line:
             bio=' '.join(description).strip()
             if bio.strip():
                 if cls not in cls_list:
                     cls_list.append(cls)
                     data_list.append(Data(cls,bio))
                 else:
                     for data in data_list:
                         if data.category==cls:
                             data.bio=' '.join(description).strip()
                             data.freq+=1
                             break
             i=0
             description.clear()
        else:
            if i==2:
                cls=line
            elif i!=1:
                description.append(remove_stopwords(line.lower()))
    return  data_list

def process_data(data_list):
    number_of_words=0
    result_data_list=[]
    for data in data_list:
        word_frequency = {}
        for word in data.bio.split():
            word=word.strip()
            if word not in word_frequency.keys():
                word_frequency[word]=1
            else:
                word_frequency[word]+=1

        total_word=len(data.bio.split())
        number_of_words+=total_word

        number_of_class=len(data_list)
        prob_cls=data.freq/number_of_class

        result_data_list.append(ResultData(data.category,prob_cls,total_word,word_frequency))

    return result_data_list

def main():
    file=open('bioCorpus.txt','r')
    data_list=retrive_data(file)
    word_frequency_by_class= process_data(data_list)
    for da in word_frequency_by_class:
        print(da.category,da.prob,da.total_word)
main()

