def uses_only(word, available):
    for letter in word:
      if letter not in available:
        return False
    
    return True
  
  
 def uses_only(word, available):
     return set(word) <= set(available)
  
  
  from collections import counter
  count = Counter('parrot')
  count
  Counter({'r',:2,'t':1,'o':1,'p':1, 'a':1})
