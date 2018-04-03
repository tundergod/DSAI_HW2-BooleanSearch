#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
import jieba_fast as jieba

jieba.add_word('76')
a =  'NBA76人拉騎士下馬 順道向詹皇招手'
seg_list = jieba.cut(a, cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式
seg_list = jieba.cut(a, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut(a)  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search(a)  # 搜索引擎模式
print(", ".join(seg_list))
'''

a = ['aa','bb','cc','dd']
b = ['euwijlkdfnfvhijoskldfjhvudjaafklmdksvjdkdalms','bbsdfghgf']

# or
for j in b:
    if any(i in j for i in a):
        print('or')

b = 'aafhokldajsjbbhsjdiosfkpdldjdjccaksjilkdsjdd'
# and
c = 0
for i in a:
    if i in b:
        c = c + 1
        if c == len(a):
            print('and')

b = 'aadsfisjdklfnieovns'
# not
c = 0
if a[0] in b:
    for i in range(1, len(a)):
        if a[i] not in b:
            c = c + 1
            if c == len(a)-1:
                print('not')
    

print('\n\n')    
a = ['a','b']
b = ['c','d']
c = []
c.append(b)
c.append(a)
print(c)
