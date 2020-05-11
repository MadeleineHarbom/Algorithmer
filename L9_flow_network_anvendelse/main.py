from Handbold.eksempel.FlowNetwork import *

handboldnework = FlowNetwork()

o = handboldnework.insert_vertex('Origin', source=True)

kv = handboldnework.insert_vertex('Kolding - Viborg')
hv =  handboldnework.insert_vertex('Herning - Viborg')
hk = handboldnework.insert_vertex('Herning - Kolding')

h = handboldnework.insert_vertex('Herning')
k = handboldnework.insert_vertex('Kolding')
v = handboldnework.insert_vertex('Viborg')

t = handboldnework.insert_vertex('Sink', sink=True)


okv = handboldnework.insert_edge(12, o, kv)
ohv = handboldnework.insert_edge(2, o, hv)
ohk = handboldnework.insert_edge(2, o, hk)


kvv = handboldnework.insert_edge(12, kv, v)
kvk = handboldnework.insert_edge(12, kv, k)

hvv = handboldnework.insert_edge(2, hv, v)
hvh = handboldnework.insert_edge(2, hv, h)

hkk = handboldnework.insert_edge(2, hk, k)
hkh = handboldnework.insert_edge(2, hk, h)


#De mængde kampene max må give før at Aarhus ikke har en chance at vinde
vt = handboldnework.insert_edge(0, v, t)
kt = handboldnework.insert_edge(10, k, t)
ht = handboldnework.insert_edge(12, h, t)

#Hvis max flow er over hvad

print(handboldnework.find_max_flow())
print('Aarhus har  58 point')
print('Hvis de vinder alle deres resterende kampe, kan  de på 8 points mere')
print('Og dermed komme op på 66 points')
print('Mellem holden i grafen og sink, er capacity det de mangler for at komme op på 66 (Aathus max mulige)')
print('Hvis det er lige meget der kommer ned i sink, som kan komme ind, så har Aarhus stadig en chance')
print('Men da 16 går ind (det skal deles 16 points mere ud), og kun 14 kommer til sink, så har Aarhus ikke nogen chance')
