data_list=[]
c=k=1

def get_input():
    num_samp=int(input('input number of samples casees: '))
    num_att=int(input('input number of attributes: '))
    for i in range(num_samp):
        data=[]
        for j in range(num_att):
            a=int(input())
            data.append(a)
        data_list.append(data)
    return num_samp,num_att

def Adaptive_decision_boundary(num_samp,num_att):
    Flag=[False]*(num_samp)
    Coeffi=[0]*(num_att)
    print()
    print('i','[x   d]','[w   w1]','no error?')
    while True:
        for i in range(num_samp):
            data=data_list[i]
            d=sum([a*b for a,b in zip(data[:-1],Coeffi[1:])])
            d=Coeffi[0]+d
            if d==0:
                d=1
            if d*data[-1]<0:
                Flag[i]=False
                Coeffi[0]=Coeffi[0]+c*data[-1]*k
                for j in range(1,num_att,1):
                    Coeffi[j]=Coeffi[j]+c*data[-1]*data[j-1]
            else:
                Flag[i]=True
            print(i+1,data,Coeffi,Flag[i])
        if all(Flag):
            break

num_samp,num_att=get_input()
Adaptive_decision_boundary(2,2)

