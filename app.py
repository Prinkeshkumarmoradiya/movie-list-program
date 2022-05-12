movies = []

def add_movie():
    title = input('enter the movie name: ')
    hero = input('enter who is the hero/heroin: ')
    year = input('in which year this movie realased: ')

    movies.append({
        'title': title,
        'hero': hero,
        'year': year
    })


def show_movies(movie_list):
    for movie in movie_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"title: {movie['title']}")
    print(f"hero: {movie['hero']}")
    print(f"year: {movie['year']}")


def find_movie():
    search_by = input("enter name of your movie  ")
    looking_for = input("what are your searching?  ")

    found_movies = find_by_atribute(movies, looking_for, lambda x: x[0])

    show_movies(found_movies)


def find_by_atribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found




def menu():
    User_input = input("\nEnter 'a' to add movie, 'l' to see your movie, 'f' to find the movie by title, or 'q' to quit:  ")
    
    
    while User_input != 'q':
    
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("unknown command please try again..")

        user_input = input("\nEnter 'a' to add movie, 'l' to see your movie, 'f' to find the movie by title, or 'q' to quit:  ")


menu()
