import math


def euclidean_distance(object1, object2):

    dis = 0
    for i in range(len(object1)):
        dis += ((object1[i]-object2[i])**2)
    dis = math.sqrt(dis)
    return round(dis, 1)


def seed_calculate(_classes, _samp):
    n = []
    flag = []
    j = 0
    for cls in _classes:

        if cls in flag:
            for i in range(len(n)):
                if n[i]['class'] == cls:
                    n[i]['freq'] += 1

                    for k in range(len(n[i]['feature'])):
                        n[i]['feature'][k] += _samp[j][k]

        else:
            flag.append(cls)
            n.append({"class": cls, 'freq': 1, 'feature': _samp[j].copy()})
        j += 1

    new_seed = []
    for i in range(len(n)):
        for j in range(len(n[i]['feature'])):
            n[i]['feature'][j] = round(n[i]['feature'][j] / n[i]['freq'], 1)
        new_seed.append(n[i]['feature'])
    return new_seed


input_file = open("input_for_forgy", "r")

if input_file.mode == 'r':
    contents = input_file.readlines()


number_of_sample = int(contents[0])
number_of_feature = int(contents[1])
number_of_seeds = int(contents[2])

samples = []
seeds = []

for i in range(number_of_seeds):
    data = contents[i+3].split()

    for j in range(len(data)):
        data[j] = int(data[j])
    seeds.append(data)

for i in range(number_of_sample):
    data = contents[i+3].split()

    for j in range(len(data)):
        data[j] = int(data[j])
    samples.append(data)

distances = []


samples2 = samples.copy()

temp_seeds = seeds.copy()

while True:
    temp_seeds = seeds.copy()
    print("Centroids : ", seeds, '\n')
    classes = []
    for sample in samples2:
        distance = 83839393
        temp = 99
        i = 0
        for seed in seeds:
            i += 1
            temp_distance = euclidean_distance(seed, sample)

            if temp_distance < distance:
                temp = i
                distance = temp_distance
        classes.append(temp)

    for i in range(len(samples)):
        print("Sample = ", i+1, " ( ", samples[i], " ) Class = ", classes[i])

    seeds = seed_calculate(classes, samples2)

    print()
    print()

    classes.clear()
    if temp_seeds == seeds:
        break
