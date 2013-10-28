res = {}

dictionaryWords = [line.strip() for line in open('theDictionary.txt')]




for spots in dictionaryWords:
    res[spots] = 0

i = 0

with open('cleanWikipedia.txt') as f:
    for line in f:
        i = i+1
        if i % 1000000 == 0:
            print 'Millions of lines processed: %d' % (i/1000000)
        thisline = line.split(" ");
        for werd in thisline:
            if res.has_key(werd.lower()):
                res[werd.lower()] = res[werd.lower()]+1





f = open('weightedDictionary.txt','w')
#print res['zyzzyvas']

for wird in dictionaryWords:
    #print '%s,%d' % (wird,res[wird])
    f.write('%s,%d\n'%(wird,res[wird]))


f.close()



