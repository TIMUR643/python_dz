
def div(s):
    return ' '.join(w[:1].upper() + w[1:] for w in s.split(' '))

source = input('Ваше слово: ').split()
res = []
for s in source:
    res.append(div(s))
print(' '.join(res))
