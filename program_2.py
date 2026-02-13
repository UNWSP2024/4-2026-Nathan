# By Nathan Nelsen
# Written 2/13/2026
# Movie Tix

# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many
# tickets are desired for each movie.
# At the end of the program it prints out the total number of tickets desired by the user.
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    total_tickets = 0

    while True:
        movie_name = input("Enter movie name (type 'thats all' when done): ")

        if movie_name == "thats all":
            break

        tickets = int(input(f"How many tickets for {movie_name}?: "))
        total_tickets += tickets

    print("Total tickets: ", total_tickets)

if __name__ == '__main__':
    main()
