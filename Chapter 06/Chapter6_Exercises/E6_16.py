s = 'The quick brown fox jumps over a lazy dog.'
if set('abcdefghijklmnopqrstuvwxyz') - set(s.lower()) == set():
    print('Pangram')
else:
    print('Not a pangram')
