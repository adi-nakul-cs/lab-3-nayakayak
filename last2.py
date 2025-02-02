# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

def last2(str):
  count = 0
  if len(str) <= 2:
    return 0
  if len(str) > 2:
    end = str[len(str)-2:len(str):] # Instead you could use str[-2:]
    beginning = str[0:len(str)-1]
    for i in range(len(beginning) - 1):
      # would be more readable to combine the two if statements
      if beginning[i] == end[0]:
        if beginning[i + 1] == end[1]:
          count = count + 1
    return count
