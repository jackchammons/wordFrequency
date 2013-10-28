
totalWords = 1314517865


p = open('weightzzz.txt','w')

with open('weightedDictionary.txt') as f:
    for line in f:
        a,b = line.split(',')
        p.write('%s,%1.12f\n'%(a,float(b)/totalWords))




f.close()



