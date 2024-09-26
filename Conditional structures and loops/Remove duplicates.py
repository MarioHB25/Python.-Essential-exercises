'''
This program simulates a social network database that stores users and the friends they have.
However, there are people in the database with duplicate accounts.
The program is responsible for returning a database,
eliminating duplicate users and the person with the most contacts on the social network.
'''

#Creating the database
red_social = [
            ("Juan", ["Maria", "Pedro", "Luis"]), 
            ("Maria", ["Juan", "Pedro","Juan"]),
            ("Pedro", ["Juan", "Maria"]),
            ("Luis", ["Juan"])
            ]

#Creating a database to store without duplicate users
red_social_sin_dupli = []

#Removing duplicate accounts    
for usuarios, amigos in red_social:
    lista_amigos_sin_dupli = list(set(amigos))
    red_social_sin_dupli.append((usuarios, lista_amigos_sin_dupli))

#Counting number of friends
amigos_por_usuario = []
for usuario, amigo in red_social_sin_dupli:
    amigos_por_usuario.append((usuario, len(amigo)))

#Output: tuple of tuples with user + num. friends
amigos_por_usuario = tuple(amigos_por_usuario)
print(amigos_por_usuario)

#Output: user with most friends
usuarios1 = (tuple(tupla1[0] for tupla1 in amigos_por_usuario))
amigos1 = (tuple(tupla1[1] for tupla1 in amigos_por_usuario))
usuario_con_mas_amigos = amigos1.index(max(amigos1))
print(f"El usuario con más amigos es {usuarios1[usuario_con_mas_amigos]}")
