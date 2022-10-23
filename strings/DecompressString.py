# w4a3 

'''
while itring through the string, if we meet an alphabet add to stack, 
if we meet a number, mulitply stack.pop() by that number and add to string. 

'''

def decompress( word : str) :

    if word == '': return None
    stack = [] 
    out = ''

    for char in word: 

        if  char.isdigit(): 

            out = out + str(stack.pop()*int(char)) 

        stack.append(char) 

    return out

def main():
  tests = [
    { 'input': "", 'output': None },
    { 'input': "w3", 'output': "www" },
    { 'input': "a1", 'output': "a" },
    { 'input': "w4a3", 'output': "wwwwaaa" },
    { 'input': "w4a3d1e1x6", 'output': 'wwwwaaadexxxxxx' },
  ]

  for i in range(len(tests)):
    print(f'Test {i+1}:', decompress(tests[i]['input']) == tests[i]['output'])

main()    