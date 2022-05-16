p_A=0.3
p_B=0.6
#Since A and B are given to be independent events
p_AB=p_A*p_B
#part 2
p_2=p_A*(1-p_B)
#part 3
p_3=p_A+p_B-p_AB
#part 4
p_4=1-p_3
#verification
if(p_AB==0.18):
    print("part 1 verified")
if(p_2==0.12):
    print("part 2 verified")
if(p_3==0.72):
    print("part 3 verified")
if(p_4==0.28):
    print("part 4 verified")


