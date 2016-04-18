#This code cleans the train data 

# put candidate name here to clean the train data related to his/her articles
candidate = 'cruz'

#removing stopwords
frstop = open('stopwords.txt')
stopwords = []
for r in frstop:
    r  =r.lower()
    stopwords.append(r.split()[0])

frstop.close()

#removing names and months
stopwords.append('january')
stopwords.append('february')
stopwords.append('march')
stopwords.append('april')
stopwords.append('may')
stopwords.append('june')
stopwords.append('july')
stopwords.append('august')
stopwords.append('september')
stopwords.append('october')
stopwords.append('november')
stopwords.append('december')
stopwords.append('donald')
stopwords.append('trump')
stopwords.append('ted')
stopwords.append('cruz')
stopwords.append('hillary')
stopwords.append('clinton')
stopwords.append('bernie')
stopwords.append('sanders')



fr = open(candidate+'.txt','r')
fileid = 1
for r in fr:
    r = r.lower()
    r = r.replace('.',' ')
    r = r.replace(',',' ')
    r = r.replace(':',' ')
    r = r.replace('[',' ')
    r = r.replace(']',' ')
    r = r.replace('(',' ')
    r = r.replace(')',' ')
    r = r.replace('{',' ')
    r = r.replace('}',' ')
    r = r.replace('\'',' ')
    r = r.replace('"',' ')
    r = r.replace('$',' ')
    r = r.replace('%',' ')
    r = r.replace('-',' ')
    r = r.replace('_',' ')
    tokens = r.split()
    if len(tokens) < 10:
        continue

    tokens = [word for word in tokens if word not in stopwords and  not word.isdigit()]
    fw = open(candidate+'/'+str(fileid)+'.txt','w')
    fw.write(' '.join(tokens))
    fw.close()
    fileid+=1

fr.close()
