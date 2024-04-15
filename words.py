def print_upper_words(words, starts_with):
  """Print words in a list as all uppercased
  
    or only print if it starts_with

  """
  
  for word in words:
     for letter in starts_with:
        if word.startswith(letter):
           print(word.upper()) 
  






print_upper_words(['hello', 'goodbye', 'find', 'look'], ['l', 'h'])