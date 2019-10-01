from collections import Counter
import math
import matplotlib.pyplot as plt


def knn(data, query, k, distance_fn, choice_fn):
    neighbor_distances_and_indices = []
    for index, example in enumerate(data):
        distance = distance_fn(example[:-1], query[:-1])
        neighbor_distances_and_indices.append((distance, index))
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)
    k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]
    k_nearest_labels = [data[i][-1] for distance, i in k_nearest_distances_and_indices]
    return k_nearest_distances_and_indices , choice_fn(k_nearest_labels)

def mean(labels):
    return sum(labels) / len(labels)

def mode(labels):
    return Counter(labels).most_common(1)[0][0]

def euclidean_distance(point1, point2):
    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum_squared_distance)

def dataProcess(file,flag):
    dataset=[]
    lines=file.readlines()
    for line in lines:
        data=[]
        if "@"in line[0] or '%' in line[0]:
            continue
        attr=line.split(',')
        for d in attr[:-1]:
            data.append(float(d.strip()))
        if flag:
            data.append(attr[8].strip())
        else:
            data.append(float(attr[-1].strip()))
        dataset.append(data)
    return dataset

def plotgraph(x,y):
    plt.scatter(x, y, label= "accuracy", color= "green", marker= "*", s=30)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('knn Vs acuracy!')
    plt.legend()
    plt.show()


def calculate(train_set,test_set):
    kn=[3,5,7]
    accu=[]
    len_test=len(test_set)
    for k in kn:
        sum=0
        for reg_query in test_set:
            reg_k_nearest_neighbors, reg_prediction = knn(
                train_set, reg_query, k, distance_fn=euclidean_distance, choice_fn=mode)
            # print("Predicted class : {0}	Actual class : {1}".format(reg_prediction,reg_query[8]))
            if reg_prediction==reg_query[8]:
                sum+=1
        print('knn',k)
        print("Number of correctly classified instances : {0}".format(sum))
        print("Total number of instances : {0}".format(len_test))
        print("Accuracy : {0}".format(sum/len_test))

        accu.append(sum/len_test)
    plotgraph(kn,accu)


def calculate1(train_set,test_set):
    kn=[3,5,7]
    accu=[]
    len_test=len(test_set)
    for k in kn:
        sum=0
        for reg_query in test_set:
            reg_k_nearest_neighbors, reg_prediction = knn(
                train_set, reg_query, k, distance_fn=euclidean_distance, choice_fn=mean)
            sum+=math.fabs(reg_query[8]-reg_prediction)
        accu.append(sum/len_test)
    plotgraph(kn,accu)

def yest_main():
    train_file=open('yeast_train.arff')
    train_set=dataProcess(train_file,True)
    test_file=open('yeast_test.arff')
    test_set=dataProcess(test_file, True)
    calculate(train_set,test_set)

def wine_main():
    train_file=open('wine_train.arff')
    train_set=dataProcess(train_file,False)
    test_file=open('wine_test.arff')
    test_set=dataProcess(test_file,False)
    sum=0
    len_test=len(test_set)
    for reg_query in test_set:
        reg_k_nearest_neighbors, reg_prediction = knn(
            train_set, reg_query, k=3, distance_fn=euclidean_distance, choice_fn=mean)
        #print(train_set[reg_k_nearest_neighbors[0][1]],reg_query)
        print("Predicted value : {0}	Actual value : {1}".format(round(reg_prediction,2),reg_query[-1]))
        sum+=math.fabs(reg_query[-1]-reg_prediction)
    print("Total number of instances : {0}".format(len_test))
    print("Mean absolute error : {0}".format(sum/len_test))
    #calculate1(train_set,test_set)

wine_main()
