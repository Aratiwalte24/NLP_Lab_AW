# Name: Arati Walte
# NLP ASSIGNMENT 4 (Paragraph)
# TITLE: Generating Unigrams,Bigrams and Trigrams in nltk (paragraph).

from nltk.util import ngrams


#Function for generating n_grams
def n_grams(n):
  #sample input
  para = '''Google LLC is an American multinational corporation from the United States. 
  It is known for creating and running one of the largest search engine the World (WWW).
  Every day more than a billion people use.the most popular search engine in world.'''
  grams = ngrams(para.split(), n)

  for i in grams:
    print(i)


#input for each n-gram
print("Unigrams:")
n_grams(1)
print("\nBigrams:")
n_grams(2)
print("\nTrigrams:")
n_grams(3)

#OUTPUT:
# Unigrams:
# ('Google',)
# ('LLC',)
# ('is',)
# ('an',)
# ('American',)
# ('multinational',)
# ('corporation',)
# ('from',)
# ('the',)
# ('United',)
# ('States.',)
# ('It',)
# ('is',)
# ('known',)
# ('for',)
# ('creating',)
# ('and',)
# ('running',)
# ('one',)
# ('of',)
# ('the',)
# ('largest',)
# ('search',)
# ('engine',)
# ('the',)
# ('World',)
# ('(WWW).',)
# ('Every',)
# ('day',)
# ('more',)
# ('than',)
# ('a',)
# ('billion',)
# ('people',)
# ('use.the',)
# ('most',)
# ('popular',)
# ('search',)
# ('engine',)
# ('in',)
# ('world.',)

# Bigrams:
# ('Google', 'LLC')
# ('LLC', 'is')
# ('is', 'an')
# ('an', 'American')
# ('American', 'multinational')
# ('multinational', 'corporation')
# ('corporation', 'from')
# ('from', 'the')
# ('the', 'United')
# ('United', 'States.')
# ('States.', 'It')
# ('It', 'is')
# ('is', 'known')
# ('known', 'for')
# ('for', 'creating')
# ('creating', 'and')
# ('and', 'running')
# ('running', 'one')
# ('one', 'of')
# ('of', 'the')
# ('the', 'largest')
# ('largest', 'search')
# ('search', 'engine')
# ('engine', 'the')
# ('the', 'World')
# ('World', '(WWW).')
# ('(WWW).', 'Every')
# ('Every', 'day')
# ('day', 'more')
# ('more', 'than')
# ('than', 'a')
# ('a', 'billion')
# ('billion', 'people')
# ('people', 'use.the')
# ('use.the', 'most')
# ('most', 'popular')
# ('popular', 'search')
# ('search', 'engine')
# ('engine', 'in')
# ('in', 'world.')

# Trigrams:
# ('Google', 'LLC', 'is')
# ('LLC', 'is', 'an')
# ('is', 'an', 'American')
# ('an', 'American', 'multinational')
# ('American', 'multinational', 'corporation')
# ('multinational', 'corporation', 'from')
# ('corporation', 'from', 'the')
# ('from', 'the', 'United')
# ('the', 'United', 'States.')
# ('United', 'States.', 'It')
# ('States.', 'It', 'is')
# ('It', 'is', 'known')
# ('is', 'known', 'for')
# ('known', 'for', 'creating')
# ('for', 'creating', 'and')
# ('creating', 'and', 'running')
# ('and', 'running', 'one')
# ('running', 'one', 'of')
# ('one', 'of', 'the')
# ('of', 'the', 'largest')
# ('the', 'largest', 'search')
# ('largest', 'search', 'engine')
# ('search', 'engine', 'the')
# ('engine', 'the', 'World')
# ('the', 'World', '(WWW).')
# ('World', '(WWW).', 'Every')
# ('(WWW).', 'Every', 'day')
# ('Every', 'day', 'more')
# ('day', 'more', 'than')
# ('more', 'than', 'a')
# ('than', 'a', 'billion')
# ('a', 'billion', 'people')
# ('billion', 'people', 'use.the')
# ('people', 'use.the', 'most')
# ('use.the', 'most', 'popular')
# ('most', 'popular', 'search')
# ('popular', 'search', 'engine')
# ('search', 'engine', 'in')
# ('engine', 'in', 'world.')