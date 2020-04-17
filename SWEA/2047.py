string = 'The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.'

a = ''
for s in string:
    if ord('a') <= ord(s) and ord(s) <= ord('z'):
        a += chr(ord(s) - 32)
    else:
        a += s
else: print(a)

print(string.upper())