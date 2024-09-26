'''
This program presents a database with movie information such as:

Title/Genre/Duration/Year of release/rating.

The program determines:

-The most popular genre
-How many movies were released in each decade
-What is the average duration of each genre.
'''

import numpy as np

# Array with movie data
peliculas = np.array([    
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Acción', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 6.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Acción', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 125, 1980, 6.8],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]
])

#Most popular genre
    ##Search for the one that appears the most times
generos, conteos = np.unique(peliculas[:,1], return_counts=True) #Returns unique indices and how many times each one appears

    #Sort counts in descending order
conteos_desc = np.argsort(conteos) [::-1] #Returns the index where counts is the highest and goes down

    #Show most popular genre based on their appearances
genero_pop = generos[conteos_desc[0]]
print(f"El género más popular es: {genero_pop} ")

#How many movies released per decade
    ##Extract decades
decadas = np.unique(peliculas[:,3].astype(int) // 10 * 10)#Find unique elements, pass to int,
                                                          # make division with approximation to the lowest integer (floor division)
                                                          # and multiply by 10 to get decade

    #Count the movies released in each decade
for decada in decadas:
    cont_decadas = np.count_nonzero((peliculas[:,3].astype(int) // 10 * 10 >= decada) & (peliculas[:,3].astype(int) // 10 * 10 < decada + 10))
                                                         #Count the repetitions of each year in column 3 of movies,
                                                         # if they are equal to or greater than their decade or less than the next
    print(f"En la década {decada} se estrenaron {cont_decadas} películas")

#Average duration of each genre
    ##Separate gender column data
full_generos = peliculas[:,1]
    ##Separate duration column data
duracion = peliculas[:,2]
    ##Create array to calculate average durations by genre
duracion_media = np.zeros(len(generos))
    ##Scroll the list of genres
for i in range (len(generos)):
    duracion_media[i] = np.mean(duracion[full_generos == generos[i]].astype(float)) ##Calculate the average duration if the genre in movies
                                                                                    ##match i in genders and convert to float
    print(f"La duración media del género de {generos[i]} es de {duracion_media[i]:.1f} minutos  ")
