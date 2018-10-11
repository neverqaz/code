mlist=[1,2,3,4]
count=0
if mlist[0]==1:
       mlist.pop(0)
       for i in [0,1,2]:
              if i==0:
                     for j in[i+1,2]:
                            for x in[j+2,0]:
                                   qaz="{}{}{}".format(mlist[i],mlist[j],mlist[x])
                                   print(qaz)
                                   count+=1
              if i==1:
                     for j in[i-1,2]:
                            for x in [j+2,1]:
                                   qaz="{}{}{}".format(mlist[i],mlist[j],mlist[x])
                                   print(qaz)
                                   count+=1

print("count: "+count)
       
