#! usr/bin/python3

def loadData(data):
    data = open(data).read().splitlines()
    return data

def booleanSearch(data, query):
    ans = []
    dic = createDic(query)
    data = segData(data, dic)
    
    for i in query:
        if ' and ' in i:
            tmp = []
            keyWords = i.split(' and ')
            for j in data:
                c = 0
                for k in keyWords:
                    if k in j:
                        c = c + 1
                        if c == len(keyWords):
                            tmp.append(j[0])
            if len(tmp) == 0:
                tmp.append('0')
            ans.append(tmp)

        if ' or ' in i:
            tmp = []
            keyWords = i.split(' or ')
            for j in data:
                if any(k in j for k in keyWords):
                    tmp.append(j[0])
            if len(tmp) == 0:
                tmp.append('0')
            ans.append(tmp)

        if ' not ' in i:
            tmp = []
            keyWords = i.split(' not ')
            for j in data:
                c = 0
                if keyWords[0] in j:
                    for k in range(1, len(keyWords)):
                        if keyWords[k] not in j:
                            c = c + 1
                            if c == (len(keyWords) - 1):
                                tmp.append(j[0])
            if len(tmp) == 0:
                tmp.append('0')
            ans.append(tmp)
    return ans

# segment data using dictionary
def segData(data, dic):
    seg = []
    tmp = []
    for i in range(len(data)):
        tmp = []
        for j in range(len(dic)):
            if dic[j] in data[i]:
                tmp.append(dic[j])
        if len(tmp) != 0:
            tmp.insert(0,i+1)
            seg.append(tmp)
        
    return seg

# create dictionary base on query
def createDic(query):
    dic = []
    for i in query:
        if ' and ' in i:
            i = i.split(' and ')
        elif ' or ' in i:
            i = i.split(' or ')
        elif ' not ' in i:
            i = i.split(' not ')
        dic.extend(i)
    dic = sorted(set(dic))

    return dic

if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                       default='source.csv',
                       help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    args = parser.parse_args()

    # Load source
    data = loadData(args.source)

    # Load query
    query = loadData(args.query)

    # search
    ans = booleanSearch(data, query)

    # write output file 
    with open(args.output, 'w') as output_file:
        for i in ans:
            l = map(str, i)
            l = ",".join(l)
            output_file.write(l + '\n')
