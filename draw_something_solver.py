import sys

word_list = {}
def init():
  words = open('dict')
  
  for word in words:
    word = word.rstrip()
    if not len(word) in word_list:
      word_list[len(word)] = []
    word_list[len(word)].append(word)

def contained(word, characters):
  word_c = {}
  char_c = {}

  for letter in word:
    if letter in word_c:
      word_c[letter] += 1
    else:
      word_c[letter] = 1

  for letter in characters:
    if letter in char_c:
      char_c[letter] += 1
    else:
      char_c[letter] = 1

  for letter in word:
    try:
      if word_c[letter] > char_c[letter]:
        return False
    except KeyError:
      return False

  return True

def solve(length_word, characters):
  for word in word_list[int(length_word)]:
    if contained(word, characters):
      print word

if __name__ == '__main__':
  init()
  solve(sys.argv[1], sys.argv[2])
