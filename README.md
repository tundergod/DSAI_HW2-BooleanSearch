# DSAI HW1-AutoTrading

## Test Environment
- Programming Language: Python 3.5.2 (pip3 distribution)
- Operating System: Ubuntu 16.04.3 LTS

## usage
usage: main.py [-h] [--training TRAINING] [--testing TESTING]
                 [--output OUTPUT]
                 
optional arguments:
  -h, --help       show this help message and exit
  --source SOURCE  input source data file name
  --query QUERY    query file name
  --output OUTPUT  output file name

## HW Explanation
- main.py : using query that given to preprocess the source data
- notP.py : straight do the boolean search
- jieba.py : 
  - use [jieba_fast](https://github.com/deepcs233/jieba_fast) that rewrite jieba using cpython
  - use hash table to index the segmented words

