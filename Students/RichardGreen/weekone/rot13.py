def rot13(x):
  import string
  #load in a string
  x = str(x)
#Create a dictonary that handles the conversion/encryption of letters. Add a place at the end for whitespace
  rot13_ids = {'a' : 'n', 'b' : 'o', 'c' : 'p' , 'd' : 'q', 'e' : 'r', 'f' : 's', 'g' : 't', 'h' : 'u', 'i' : 'v', 'j' : 'w','k' : 'x','l' : 'y','m' : 'z','n' : 'a','o' : 'b', 'p' : 'c','q' : 'd','r' : 'e','s' : 'f','t' : 'g','u' : 'h','v' : 'i','w' : 'j','x' : 'k','y' : 'l','z' : 'm','A' : 'N', 'B' : 'O', 'C' : 'P' , 'D' : 'Q', 'E' : 'R', 'F' : 'S', 'G' : 'T', 'H' : 'U', 'I' : 'V', 'J' : 'W','K' : 'X','L' : 'Y','M' : 'Z','N' : 'A','O' : 'B', 'P' : 'C','Q' : 'D','R' : 'E','S' : 'F','T' : 'G','U' : 'H','V' : 'I','W' : 'J','X' : 'K','Y' : 'L','Z' : 'M', ' ': ' '}

  #create an empty list to write our converted, concatenated results to
  s = ''
  results = list(s)

 #split letters up
  split_list = list(x)
  # interate through each character

  for id in split_list:
# convert values to rot13 values
    if id in string.whitespace:
      results += "".join(id)
    if id in string.punctuation:
      results += "".join(id)
    else:
      results += "".join(rot13_ids[id])
  return results


if __name__ == '__main__':
  print(rot13('ab'))
  print(rot13(' R'))
  #lets test punctuation
  print(rot13('%$abcdefghi'))
  #lets test lowercase and punctuation
  print(rot13('rich%'))
  #lets test upper and lower case
  print(rot13('Rich '))
  #lets test upper and lower case again
  print(rot13('Code'))
  #lets test all upper case
  print(rot13('FELLOWS'))
