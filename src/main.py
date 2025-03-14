import flet as ft
import spacy
import random
import os
from IPython.display import clear_output

nlp = spacy.load('es_core_news_sm')

lista_frases = open('storage/data.txt', 'r').readlines()

with open('storage/data.txt', 'r') as arquivo:

  for frase in arquivo.readlines():

    lista_frases.remove(frase)
    lista_frases.append(frase)
    # Aplicando a tokenização
    doc = nlp(frase)
    # Extraindo os tokens
    tokens = [token.text.casefold() for token in doc]
    random.shuffle(tokens)
    for i in (['.', '\n', '?', '¿', ',', '¡', '!']):
      if i in tokens:
        tokens.remove(i)
    print(tokens)
    k = input('mostrar resultado (c)')
    if k == 'c':
      with open('storage/data.txt', 'w') as novo_arquivo:
        for frase in lista_frases:
          novo_arquivo.writelines(frase)
      print(frase)
    l = input('seguir? (c)')
    if l == 'c':
      clear_output()
    else:
      clear_output()
      break