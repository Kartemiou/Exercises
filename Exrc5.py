### Main function
def Converter(file):
    
  Display_file(file)
    
  inf = open(file, 'r')
  char_lst = [line.rstrip() for line in inf]
  l = len(char_lst)
  new_lst = []
  split_lst = []

  for i in char_lst:  new_lst += [char_lst[0].lower()] 
  for i in range(l): split_lst += new_lst[i].split()
    
  Popular(split_lst)
  Combinations(split_lst)

  inf.close()
    
## Shows the given file
def Display_file(f):    
    
  infile = open(f, 'r')
  for line in infile:
    print(line, end="")
    
  infile.close()

## Finds the 10 most popular words
def Popular(split_lst):

  times, words = []
  for item in split_lst:
    words.append(item)
    times.append(split_lst.count(item))
    valueToBeRemoved = item
    split_lst = [value for value in split_lst if value != valueToBeRemoved]
    if split_lst == []: break
      
  if len(words) < 10:
    print("Not enough words to compare")
  else: 
    times_zip = zip(times, words)
    sorted_pairs = sorted(times_zip)
    tuples = zip(*sorted_pairs)
    times, words = [list(tuple) for tuple in tuples]
    if len(words) > 10:
      del words[11:]
    
    print(words)

## Finds the 3 most common occurances of the 1st 2 & 3 letters
def Combinations(split_lst):

  # for the 1st 2 letters
  letters, occur2 = []
  pos = 0
  for item in split_lst:
    letters.append(split_lst[pos][:2]) 
    pos += 1
  
  new_letters_2 = []
  for j in letters:
    new_letters_2.append(j)
    occur2.append(letters.count(j))
    valueToBeRemoved = j
    letters = [value for value in letters if value != valueToBeRemoved]
    if letters == []: break
    
  if len(new_letters_2) < 3:
    return None
  else:
    times_zip = zip(occur2, new_letters_2)
    sorted_pairs = sorted(times_zip)
    tuples = zip(*sorted_pairs)
    occur2, new_letters_2 = [list(tuple) for tuple in tuples]
    if len(new_letters_2) > 3:
      del new_letters_2[3:]
    
    print(new_letters_2)

  # for the 1st 3 letters
  letters, occur3, new_letters_3 = []
  pos = 0
  for item in split_lst:
    letters.append(split_lst[pos][:3]) 
    pos += 1
  
  for j in letters:
    new_letters_3.append(j)
    occur3.append(letters.count(j))
    valueToBeRemoved = j
    letters = [value for value in letters if value != valueToBeRemoved]
    if letters == []: break
    
  if len(new_letters_3) < 3:
    return None
  else:
    times_zip = zip(occur3, new_letters_3)
    sorted_pairs = sorted(times_zip)
    tuples = zip(*sorted_pairs)
    occur3, new_letters_3 = [list(tuple) for tuple in tuples]
    if len(new_letters_3) > 3:
      del new_letters_3[3:]
    
    print(new_letters_3)