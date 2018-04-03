#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import jieba_fast as jieba
import time

start_time = time.time()

def loadData(data):
    data = open(data).read().splitlines()
    return data

def wordSegment(data, numH):
    
    hashTable = createHashTable(numH)
    

    for i in range(len(data)):
        #words = jieba.cut_for_search(data[i])
        words = jieba.cut(data[i], cut_all=True)
        words = list(words)
        words = [j for j in words if 
            (j != '' ) and
            (
                ((j[0] > u'\u4e000' and j[0] < u'\u9fff') and (len(j) == 2 or len(j) == 3)) or # Chinese 
                (ord(j[0]) >= 65 and ord(j[0]) <= 90) or # Lower letter
                (ord(j[0]) >= 97 and ord(j[0]) <= 122) # Upper letter
            )
        ]

        if i == 23238:
            print(words)    
        hashTable = buildHashTable(words, i, numH, hashTable)
    return hashTable

def createHashTable(numH):
    hashTable = [[] for i in range(numH)]
    return hashTable

def buildHashTable(words, index, numH, hashTable):
    for i in words:
        tmp = hash(i) % numH
        hashTable[tmp].append(i + '/' + str(index))
    return hashTable

def booleanSearch(query, numH, hashTable, data):
    a = ' and '
    b = ' or '
    c = ' not '
    for i in query:

        # and case
        if a in i:
            ansList = []
            rowList = []
            keyWord = i.split(a)

            # boolean search 
            tmp = hash(keyWord[0]) % numH

            # search the row number for the first element, list them in rowList
            for j in hashTable[tmp]:
                if keyWord[0] in j:
                    rowN = int(j.split('/')[1])
                    rowList.append(rowN)
            
            for j in range(1, len(keyWord)):
                for k in range(len(rowList)):
                    if keyWord[j] in data[rowList[k]]:
                        ansList.append(rowList[k])

            for j in range(len(ansList)):
                ansList[j] = ansList[j] + 1
            ansList = sorted(list(set(ansList)))

            print('[{0}]'.format(','.join(map(str, ansList))))
                            
                
        # or case
        elif b in i:
            ansList = []
            keyWord = i.split(b)

            # boolean search 
            for j in keyWord:
                tmp = hash(j) % numH
                for k in hashTable[tmp]:
                    if j in k:
                        rowN = int(k.split('/')[1])
                        ansList.append(rowN)

            for j in range(len(ansList)):
                ansList[j] = ansList[j] + 1

            ansList = sorted(list(set(ansList)))

            print('[{0}]'.format(','.join(map(str, ansList))))

        # not case
        elif c in i:
            ansList = []
            rowList = []
            keyWord = i.split(c)

            # boolean search 
            tmp = hash(keyWord[0]) % numH

            # search the row number for the first element, list them in rowList
            for j in hashTable[tmp]:
                if keyWord[0] in j:
                    rowN = int(j.split('/')[1])
                    rowList.append(rowN)

            for j in range(1, len(keyWord)):
                for k in range(len(rowList)):
                    if keyWord[j] not in data[rowList[k]]:
                        ansList.append(rowList[k])

            for j in range(len(ansList)):
                ansList[j] = ansList[j] + 1

            ansList = sorted(list(set(ansList)))
            print('[{0}]'.format(','.join(map(str, ansList))))

        else:
            print('WRONG')

    #return ans 

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


    # Load data as list
    data = loadData(args.source)
    
    # Word segmentation, build Hash table
    numH = 4096
    hashTable = wordSegment(data,numH)
    
    # load query and execute boolean search
    query = loadData(args.query)
    booleanSearch(query, numH, hashTable, data)
    print("--- %s seconds ---" % (time.time() - start_time))
