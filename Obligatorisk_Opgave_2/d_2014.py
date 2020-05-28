#25%
#dice

def D_2014(gunnars_dice, emmas_dice):
    g1 = range(gunnars_dice[0], gunnars_dice[1]+1)
    e1 = range(emmas_dice[0], emmas_dice[1]+1)
    g2 = range(gunnars_dice[2], gunnars_dice[3]+1)
    e2 = range(emmas_dice[2], emmas_dice[3]+1)

    g_avr = sum(g1)/len(g1) + sum(g2)/len(g2)
    print('Gunnars average ' + str(g_avr))
    e_avr = sum(e1)/len(e1) + sum(e2)/len(e2)
    print('Emmas average ' + str(e_avr))

    if e_avr > g_avr:
        return 'Emma'
    elif g_avr > e_avr:
        return 'Gunnar'
    else:
        return 'Trie'


print('Sample input 1')
D_2014([1, 4, 1, 4], [1, 6, 1, 6])
print('Sample input 2')
D_2014([1, 8, 1, 8], [1, 10, 2, 5])
print('Sample input 3')
D_2014([2, 5, 2, 7], [1, 5, 2, 5])