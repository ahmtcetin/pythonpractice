# Creating favorite movies tuple
favorite_movies = ("The Lord Of The Rings", "Pulp Fiction", "Kill Bill", "This Is The End", "The Godfather")

# Printing all moview
print("First Movie: ", favorite_movies[0])
print("Second Movie: ", favorite_movies[1])
print("Third Movie: ", favorite_movies[2])
print("Fourth Movie: ", favorite_movies[3])
print("Fifth Movie: ", favorite_movies[4])

# Determining length of tuple
length = len(favorite_movies)

# Printinh tuple length
print("Number of movies: ", length)

# Asking a moview from user
movie_from_user = input("Enter a movie name: ")

# Cheking if the movie is inside of the tuple
if movie_from_user in favorite_movies:
    print("Given movie is already exist!")
else:
    print("Given movie is not exist.")

# Getting a new movie to axpend tuple
movie_from_user = input("Enter a movie to add the list: ")
new_favorite_movies = favorite_movies + tuple(movie_from_user.split(","))

# Print all movies inside ot the tuple
for movie in new_favorite_movies:
    print(movie)