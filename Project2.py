import sys
from itertools import permutations
import string

#greeting
print('Hello User! Here we help generate possible words from the letters you are holding.')
print('Please enter your letters (? for blank tiles):')

inputLetters = input().strip().lower()
letters = set([])

capital = list(string.ascii_uppercase)

#add all possible letter combinations if '?' is in inputLetters 
count = inputLetters.count('?')
if count == 0:
  letters.add(inputLetters)
elif count == 1:
  for i in capital:
    letters.add( inputLetters.replace('?', i) )
else:
  fstIdex = inputLetters.index('?')
  secIdex = inputLetters.rindex('?')
  for i in capital:
    for j in capital:
      letters.add( inputLetters[:fstIdex] + i + inputLetters[fstIdex+1:secIdex] + j + inputLetters[secIdex+1:] )


#open file
try:
  file = open('scrabble_dict.txt')
except FileNotFoundError:
  print('File scrabble_dict.txt not found')
  sys.out()
content = set(file.read().split())

points = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8,
          'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1,
          'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

#add words and points to wordlist
wordlist = {}
for comb in letters:
  for i in range(2,len(comb)+1):
    permu = permutations(comb, i)
    for group in permu:
      word = ''.join(group)
      if word.lower() in content and word not in wordlist:
        p = 0
        for i in word:
          if i.isupper():
            continue
          p += points[i]
        wordlist.update({word:p})
    

#sort wordlist according to point
wordlist = sorted(wordlist.items(), key = lambda x: x[1], reverse = True)

#print result
print('Words you can play:')
for i in wordlist:
  print(i[0], ':', i[1])



