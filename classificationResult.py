# this code shows who each aricle/speech is biased to

# these input files are from the output of Mallet
frt = open('testoutput-trump.txt','r')
frs = open('testoutput-sanders.txt','r')
frcl = open('testoutput-clinton.txt','r')
frcz = open('testoutput-cruz.txt','r')

candidates = ['trump','sanders','clinton','cruz']
frt.readline()
frs.readline()
frcl.readline()
frcz.readline()

for r in frt:
    tokens1 = r.split()
    tokens2 = frs.readline().split()
    tokens3 = frcl.readline().split()
    tokens4 = frcz.readline().split()

    
    values = [float(tokens1[3]),float(tokens2[3]),float(tokens3[3]),float(tokens4[3])]

    # the file name + the persion who file is biased to
    print(tokens1[1]+'\t'+candidates[values.index(max(values))])


frt.close()
frs.close()
frcl.close()
frcz.close()
