seq = [
  '',
  '{[()]}',
  '()[]{}',
  '([])',
  '{{[[(())]]}}',
  '{[()([])]}',
  '([]',
  '[({)}]',
  ')(',
  '(([{()}])))',
]



def check_seq(seq):
  stack = [0]
  for c in seq:
    if c in ['{','(','[']:
      stack.append(c)
    elif c == '}' and stack[-1] == '{':
      stack.pop(-1)
    elif c == ']' and stack[-1] == '[':
      stack.pop(-1)
    elif c == ')' and stack[-1] == '(':
      stack.pop(-1)
    else:
      return False

  if stack == [0]:
    return True
  return False
    
  

for s in seq:
  print(check_seq(s))