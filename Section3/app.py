movies = [
    {"name": "RRR", "director": "Raj", "year": 2022},
    {"name": "Boss", "director": "XXX", "year": 2004},
    {"name": "Kick", "director": "YYY", "year": 2015}
]

option = input("Enter your option (a for add,f for find movie, l for list & q for quit): ")

while option != 'q':
    if option == 'a':
        name = input("Enter movie name: ")
        director = input("Enter movie director: ")
        year = input("Enter movie released year: ")
        movies.append({"name": name, "director": director, "year": year})
    elif option == 'l':
        print(movies)
    elif option == 'f':
        movie_name = input("Enter movie name: ")
        for movie in movies:
            if movie['name'].lower() == movie_name.lower():
                print(movie)
    elif option == 'q':
        break
    else:
        print("Enter correct option")
    option = input("Enter your option (a for add,f for find movie, l for list & q for quit): ")



                #           using first class function
# user_options = {
#     "a": add_movie,
#     "l": show_movies,
#     "f": find_movie
# }
#
# while option != 'q':
#     if option in user_options:
#         selected_fun = user_options[option]
#         selected_fun()
