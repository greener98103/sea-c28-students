def rot13(x):
  import string
  #load in a string
  x = str(x)
#make it lowercase

  rot13_ids = {'a' : 'n', 'b' : 'o', 'c' : 'p' , 'd' : 'q', 'e' : 'r', 'f' : 's', 'g' : 't', 'h' : 'u', 'i' : 'v', 'j' : 'w','k' : 'x','l' : 'y','m' : 'z','n' : 'a','o' : 'b', 'p' : 'c','q' : 'd','r' : 'e','s' : 'f','t' : 'g','u' : 'h','v' : 'i','w' : 'j','x' : 'k','y' : 'l','z' : 'm'}

  # add capitalized characters

  #{'a' : 'n', 'b' : 'o', 'c' : p , 'd' : q, 'e' : r, 'f' : s, 'g' : t, 'h' :u, 'i' : v, 'j' : w,'k' : x,'l' : y,'m' : z,'n' : a,'o' : b, 'p' : c,'q' : d,'r' : e,'s' : f,'t' : g,'u' : h,'v' : i,'w' : j,'x' : k,'y' : l,'z' : m}


  #create an empty list to write our converted, concatenated results to
  s = ''
  results = list(s)

  #make it lowercase
  #split letters up
  split_list = list(x)
  # convert values to rot13 values

  for id in split_list:
    if id.isspace():
      results += "".join(id)
    if id in string.punctuation:
      results += "".join(id)

    else:
      results += "".join(rot13_ids[id])

  return results


if __name__ == '__main__':
  print(rot13('ab'))
  print(rot13('ba'))
  print(rot13('abcdefghi'))
  print(rot13('rich%'))
  #print(rot13('Rich'))
  #print(rot13('Green '))
