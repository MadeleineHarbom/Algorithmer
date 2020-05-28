#Opgave G: 40%
#TODO
#n er integer. Antal er antal deltager
#k er en integet. Antal pladser
#x er en list men deres partner-krav
def G_2014(n, seats, x):
    introverts = []
    popular = [0]*(n+1) #brug mig
    lucky_party_goers = []

    hopefuls = [0] + x
    circle_of_homies = check_circular_dependencies(hopefuls)
    print('Circlea of Homies')
    print(circle_of_homies)
    for i in range(1, len(hopefuls)):
        if i == hopefuls[i]:
            introverts.append(i)

    for j in range(len(hopefuls)):
        if j != hopefuls[j]:
            popular[hopefuls[j]] += 1
    print('popular')
    print(popular)

    while add_biggest_circle(circle_of_homies, seats, lucky_party_goers):
        continue
    while add_most_popular(popular, lucky_party_goers, seats):
        continue
    full_up_introverts(seats, lucky_party_goers, introverts)
    return lucky_party_goers


def check_circular_dependencies(x):
    #returns a list of lists with the ids of all circular dependencies
    dependencies = []
    for i in range(1, len(x)):
        if not already_circlular(i, dependencies):
            find_circkle(x, i, dependencies)
    return dependencies


def find_circkle(x , start_person, dependencies):
    target = x[start_person]  # id på personen i vil ha med
    temp_list = [start_person]
    while target not in temp_list and not target == start_person:
        temp_list.append(target)
        target = x[target]

    if target == temp_list[0] and len(temp_list) > 1:
        dependencies.append(temp_list)

def already_circlular(person, dependencies):
    for dep in dependencies:  # går galt
        if person in dep:
            return True
    return False

def find_longest_list(lissst, free_seats):
    longest_list_index = None
    if len(lissst) > 1:
        for i in range(0, len(lissst)):
            if len(lissst[i]) <= free_seats:
                if longest_list_index is None or len(lissst[longest_list_index]) < len(lissst[i]):
                    longest_list_index = i
    return longest_list_index

def add_biggest_circle(circle_of_homies, seats, lucky_party_goers):
    if len(circle_of_homies) > 0:
        longest_homie_list = find_longest_list(circle_of_homies, seats - len(lucky_party_goers))
        if longest_homie_list is not None:
            for ppl in circle_of_homies[longest_homie_list]:
                lucky_party_goers.append(ppl)
            circle_of_homies.remove(circle_of_homies[longest_homie_list])
            print(lucky_party_goers)
            return True
        else:
            return False
    else:
        return False

def add_most_popular(popular, lucky_party_goers, seats):
    most_popular = max(popular)
    if most_popular != 0 and seats - len(lucky_party_goers) > 0:
        most_popular_index = popular.index(most_popular)
        lucky_party_goers.append(most_popular_index)
        popular[most_popular_index] = 0
        return True
    else:
        return False

def full_up_introverts(seats, lucky_party_goers, introverts):
    while len(lucky_party_goers) < seats and len(introverts) > 0:
            person = introverts[0]
            lucky_party_goers.append(person)
            introverts.remove(person)




print('Sample input 1')
data1 = str(G_2014(4, 4, [1, 2, 3, 4]))
print('Final 1:' + str(data1))

print('Sample input 2')
data2 = str(G_2014(12, 3, [2, 3, 4, 5, 6, 7, 4, 7, 8, 8, 12, 12]))
print('Final 2:' + str(data2))
print('Sample input 3')
data3 = str(G_2014(5, 4, [2, 3, 1, 5, 4]))
print('Final 3:' + data3)