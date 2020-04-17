'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # wordArr = word.split("")
    count = 0
    wordHolder = word
    if wordHolder[0:2] == "th":
      wordHolder = wordHolder[1:]
      count += 1
    elif wordHolder[0:2] != "th":
      if len(wordHolder) > 2:
        wordHolder = wordHolder[1:]
      else:
        wordHolder = ""

    if len(wordHolder) == 0:
      return count
    else:
      return count_th(wordHolder) + count
      

