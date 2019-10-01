class Data(object):
    def __init__(self, category=None, bio=None,name=None,freq=1):
        self.category = category
        self.bio = bio
        self.name=name
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

def train_test(cls_list,data_list,cls,bio,description):
    if cls not in cls_list:
        cls_list.append(cls)
        data_list.append(Data(cls,bio))
    else:
        for data in data_list:
            if data.category==cls:
                data.bio=' '.join(description).strip()
                data.freq+=1
                break
    return cls_list,data_list

def retrive_data(train_num,file):
    lines=file.readlines()
    i=num=0
    name=cls=""

    train_data_list = []
    test_data_list = []
    train_cls_list=[]
    description=[]

    for line in lines:

        i=i+1
        line=line.strip()

        if not line:
             bio=' '.join(description).strip()
             if bio.strip():
                 num+=1
                 if num<train_num:
                     train_cls_list,train_data_list=train_test(train_cls_list,train_data_list,cls,bio,description)
                 else:
                    test_data_list.append(Data(cls,bio,name))
             i=0
             description.clear()
        else:
            if i==1:
                name=line
            elif i==2:
                cls=line
            elif i!=1:
                description.append(remove_stopwords(line.lower()))
    return  train_data_list,test_data_list

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

    return result_data_list,number_of_class,number_of_words,len(word_frequency.keys())

def word_freq(data,word):
    cnt = 0
    for datum in data:
        for w in datum.bio.split():
            if w == word:
                cnt+=1
    return cnt

def word_freq_class(data, word):
    cnt = 0
    for datum in data.keys():
        if datum== word:
            return data[datum]
    return cnt

def main():
    file=open('bioCorpus.txt','r')
    print('enter train number:')
    train_num=int(input())

    train_data_list,test_data_list=retrive_data(train_num,file)
    word_frequency_by_class, number_of_class, number_of_words, word_count = process_data(train_data_list)

   # word_count = 10

    print(number_of_class, number_of_words, word_count)

    total_test_data = len(test_data_list)
    test_corrected = 0
    for data in test_data_list:
        t_p = 0
        _class = data.category
        p = 0
        for all_class in word_frequency_by_class:
            temp_class = all_class.category
            p_of_class = all_class.prob
            total_word = all_class.total_word
            word_freq_by_c = all_class.word_freq
            p_of_s = 1
            p_of_s_c = 1
            for w in data.bio.split():
                w_freq = word_freq(train_data_list,w)
                if w_freq != 0:
                    p_of_w = (w_freq)/(number_of_words)
                    p_of_s *= p_of_w
                    w_freq_by_c = word_freq_class(word_freq_by_c,w)
                    p_of_w_c = (w_freq_by_c+1)/(total_word+word_count)
                    p_of_s_c *= p_of_w_c
            e_probability = (p_of_s_c*p_of_class)/p_of_s
            t_p+=e_probability

            print( temp_class,e_probability,end="  ")
            if e_probability < p:
                _class = temp_class
                p = e_probability

        print("\n",data.name,end="  ")
        print("Prediction : "+_class,end=" ")
        if data.category ==_class:
            print("Right")
            test_corrected += 1
        else:
            print("Wrong")
        print()
    print("accuracy" , test_corrected*100/total_test_data,"%")

main()

