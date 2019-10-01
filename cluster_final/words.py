def single_class_error(class1, all_sample):
    cnt = [0] * len(all_sample[0])
    n = len(class1['class'])

    for i in range(len(class1['class'])):
        for j in range(len(all_sample[0])):
            cnt[j] += all_sample[class1['class'][i]-1][j]

    for c in range(len(cnt)):
        cnt[c] = round(cnt[c]/n, 1)

    error = 0
    for i in range(len(class1['class'])):
        for j in range(len(all_sample[0])):
            error += ((cnt[j] - all_sample[class1['class'][i]-1][j])**2)

    return round(error, 1)

def class_error(class1, class2, all_sample):
    cnt = [0] * len(all_sample[0])
    n = len(class1['class'])+len(class2['class'])
    for i in range(len(class1['class'])):
        for j in range(len(all_sample[0])):
            cnt[j] += all_sample[class1['class'][i]-1][j]

    for i in range(len(class2['class'])):
        for j in range(len(all_sample[0])):
            cnt[j] += all_sample[class2['class'][i] - 1][j]

    for c in range(len(cnt)):
        cnt[c] = round(cnt[c]/n, 1)

    error = 0
    for i in range(len(class1['class'])):
        for j in range(len(all_sample[0])):
            error +=((cnt[j] - all_sample[class1['class'][i]-1][j])**2)

    for i in range(len(class2['class'])):
        for j in range(len(all_sample[0])):
            error += ((cnt[j] - all_sample[class2['class'][i]-1][j])**2)
    return round(error, 1)

def join_classes(all_classes, class1, class2):
    for c in range(len(all_classes)):
        if all_classes[c] == class1:
            for cc in class2['class']:
                all_classes[c]['class'].append(cc)
            all_classes[c]['class'].sort()

    for c in range(len(all_classes)):
        if all_classes[c] == class2:
            all_classes.remove(all_classes[c])
            break
    return all_classes

def print_classes(indx1, indx2, _classes):
    n = len(_classes)
    for i in range(0,n,1):
        if i == indx1:
            if i != 0:
                print(',', end="")
            print("{", _classes[indx1]["class"], end=",")
            print("", _classes[indx2]["class"], end="}  ")
        elif i != indx2:
            if i != 0:
                print(',', end="")
            print("{", _classes[i]["class"], end=" }  ")

input_file = open("input", "r")

if input_file.mode == 'r':
    contents = input_file.readlines()

number_of_sample = int(contents[0])
number_of_feature = int(contents[1])

samples = []
classes = []
for i in range(number_of_sample):
    data = contents[i+2].split()
    classes.append({"class": [i+1]})
    for j in range(len(data)):
        data[j] = int(data[j])
    samples.append(data)


while True:
    print(classes, "\n\n")

    if len(classes) == 1:
        break
    indx1 = indx2 = 0
    err = 999999
    for i in range(len(classes)):
        for j in range(i+1, len(classes)):
            e = k = 0
            n = len(classes)
            while k < n:
                if k == i:
                    e += class_error(classes[i], classes[j], samples)
                elif k != j:
                    e += single_class_error(classes[k], samples)
                k += 1

            print_classes(i, j, classes)
            print(" : ", e)
            if e < err:
                err = e
                indx1 = i
                indx2 = j

    classes = join_classes(classes, classes[indx1], classes[indx2])

    print(classes,"\n\n")
