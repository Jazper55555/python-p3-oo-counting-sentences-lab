import re

class MyString:
  def __init__(self, value='') -> None:
      self.value = value

  @property
  def value(self):
      return self._value
  
  @value.setter
  def value(self, value):
     if isinstance(value, str):
        self._value = value
     else:
        print('The value must be a string.')
  
  def is_sentence(self):
      if self.value.endswith('.'):
         return True
      else:
         return False
      
  def is_question(self):
     if self.value.endswith('?'):
        return True
     else:
        return False
     
  def is_exclamation(self):
    if self.value.endswith('!'):
      return True
    else:
      return False
    
  def count_sentences(self):
     split_str = re.split('[!.?]', self.value)
     split_str = list(filter(None, split_str))
     return len(split_str)

# breakpoint()