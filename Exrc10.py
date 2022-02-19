import math

### Main function
def Depiction(file):

  Display_file(file)
  inf = open(file, 'r')
  char_lst = [line.rstrip() for line in inf]
  
  pos = 0
  bad_chars = [';', ':', '!', "*", "."]
  # Get rid of spaces " " & unwanted characters
  for item in char_lst:
    char_lst[pos] = ''.join(item.split())
    for i in bad_chars : char_lst[pos] =  char_lst[pos].replace(i, "") 
    pos += 1

  print(char_lst)    
  Bin_lst = []
  Bits = []
  for i in range(len(char_lst)):
    
    B_lst = Convert_to_binary(char_lst[i])
    for item in B_lst: 
      Bin_lst.append(str(item))  
      coun = 0
      for j in str(item):
        if coun == 0 or coun == 1 or coun == 5 or coun == 6: Bits.append(j)
        coun += 1
  
  # Creating a separate list with the last 2 & 1st 2 binary digits
  Bits = ["".join(Bits)]
  Bits_16 = list()
  n_Bit_16 = list()
  for i in Bits[0]: Bits_16 += i
  pos = []
  for i in range(len(Bits_16)):
    if i % 16 == 0: pos.append(i)
  print(pos)
  
  print(Bits)
  print(n_Bit_16)   
  
## Shows the given file
def Display_file(f):    
    
  infile = open(f, 'r')
  for line in infile:
    print(line, end="")
    
  infile.close()

## Converts the given string to binary
def Convert_to_binary(c):
  
  l,m=[],[]
  for i in c:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m