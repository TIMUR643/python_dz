subjectt = {}
with open('6.txt', 'r') as init_f:
    for line in init_f:
        subject, lection, practice, lab = line.split()
        subjectt[subject] = int(lection) + int(practice) + int(lab)
    print(f'Часы по предмету- {subjectt}')
