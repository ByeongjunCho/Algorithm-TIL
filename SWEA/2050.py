alpabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alpa_dict = {alpa: num + 1 for num, alpa in enumerate(list(alpabet))}


for a in alpabet:
    print(alpa_dict[a], end=' ')