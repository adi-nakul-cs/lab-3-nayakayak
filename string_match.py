# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

def string_match(a, b):
  count = 0
  if len(a) >= len(b):
    for i in range(len(b) - 1):
      if b[i] == a[i]:
        if b[i+1] == a[i+1]:
          count = count + 1
  if len(a) < len(b):
    for i in range(len(a) - 1):
      if b[i] == a[i]:
        if b[i+1] == a[i+1]:
          count = count + 1
  return count
