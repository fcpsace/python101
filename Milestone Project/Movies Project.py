movies = []


def menu():
    user_input = 'add'

    while user_input != 'quit':
        if user_input == 'add':
            add_movie()
        elif user_input == 'list':
            list_movies()
        else:
            print('Unknown command-please try again.')

        user_input = input("Enter 'add' to add a song \n" +
                        "Enter 'list' to list songs \n" +
                        "Enter 'quit' to save movies and exit \n")
        
def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'name': name,
        'director': director,
        'year': year
     
    })
    

def list_movies():
    for movie in movies:
        print(f"Name: {movie['name']}")
        print(f"Director: {movie['director']}")
        print(f"Release year: {movie['year']} \n\n")


menu()
