import itertools as it

x=[1,2,3,4]
sample_space=list(it.permutations(x))
n_1=n_2=n_3=n_4=n_5=0

for i in sample_space:
    if (i.index(1)<i.index(2)):
        n_1+=1
    if i.index(1)<i.index(2) and i.index(2)<i.index(3):
        n_2+=1
    if i.index(1)==0 and i.index(2)==3:
        n_3+=1
    if i.index(1)==1 or i.index(1)==0:
        n_4+=1
    if i.index(2)==i.index(1)+1:
        n_5+=1
n_s=len(sample_space)
print("Probability of Event 1 is {}".format(n_1/n_s))
print("Probability of Event 2 is {}".format(n_2/n_s))
print("Probability of Event 3 is {}".format(n_3/n_s))
print("Probability of Event 4 is {}".format(n_4/n_s))
print("Probability of Event 5 is {}".format(n_5/n_s))
