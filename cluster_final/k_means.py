import math


def euclidean_distance(object1, object2):

    dis = 0
    for i in range(len(object1)):
        dis += ((object1[i]-object2[i])**2)
    dis = math.sqrt(dis)
    return round(dis, 1)


def centroid_calculate(_class):
    n = len(_class["class_member"])
    cent = [0] * len(_class["class_member"][0])
    for i in range(len(_class["class_member"])):
        for j in range(len(_class["class_member"][i])):
            cent[j] += _class["class_member"][i][j]

    for i in range(len(_class["class_member"][0])):
        cent[i] = round(cent[i]/n, 1)
    return cent


input_file = open("input_for_k_means", "r")

if input_file.mode == 'r':
    contents = input_file.read().split("\n")


number_of_sample = int(contents[0])
number_of_feature = int(contents[1])
number_of_cluster = int(contents[2])

samples = []
seeds = []
centroid = []
classes = []

for i in range(number_of_sample):
    data = contents[i+3].split()

    for j in range(len(data)):
        data[j] = int(data[j])

    samples.append(data)
    if i < number_of_cluster:
        centroid.append(data)
        classes.append({"class": [i + 1], "centroid": data.copy(),"class_member": [data.copy()]})
    else:
        cls = 1
        dis = 9999999
        for l in range(len(classes)):
            d = euclidean_distance(classes[l]['centroid'], data)
            if d < dis:
                dis = d
                cls = l
        classes[cls]["class_member"].append(data)
        new_centroid = centroid_calculate(classes[cls])
        classes[cls]["centroid"] = new_centroid
        print("        ", end=" ")
        for cls in classes:
            print(cls["centroid"], end=" ")
        print()


print("\n\nFinal Centroids", end=" ")
for cls in classes:
    print(cls["centroid"], end=" ")
print("\n")
for sample in samples:
    dis = []
    dd = 99990000
    cls_index =0
    for cls in range(len(classes)):
        d = euclidean_distance(classes[cls]["centroid"],sample)
        dis.append(d)
        if d < dd:
            dd = d
            cls_index = cls
    print("        distances :", end=" ")
    for d in dis:
        print(" ",d, end=" ")

    print("nearest : ", classes[cls_index]["centroid"])
