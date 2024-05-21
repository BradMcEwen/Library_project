from library import Library


def main():
    library = Library()

    while True:
        print("\n1. Book Operations \n2. User Operations \n3. Author Operations \n4. Genre Operations \n5. Quit")
        direction = input("Please select an option above: ")
        try:
            if direction == "1":
                print("\n1. Add Book \n2. Checkout book \n3. Return Book \n4. Search for a book \n5. display all books \n6. Exit")
                choice = input("Enter your choice: ")
                try: 
                    if choice == "1":
                        library.add_book()
                    elif choice == "2":
                        library.checkout_book()
                    elif choice == "3":
                        library.return_book()
                    elif choice == "4":
                        library.search_for_book()
                    elif choice == "5":
                        library.display_books()
                    elif choice == "6":
                        print("Thanks for supporting your public Library! Have a nice day :)")
                    else:
                        print("Please enter a valid choice")
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif direction == "2":
                print("\n1. Add new user \n2. View user details \n3. Display all user \n4. Exit to menu")
                user_choice = input("Enter your choice: ")
                try:
                    if user_choice == "1":
                        library.add_user()
                    elif user_choice == "2":
                        library.view_user()
                    elif user_choice == "3":
                        library.display_users()
                    elif user_choice == "4":
                        print("returning to main menu")
                    else:
                        print("Please enter a valid choice")
                except Exception as e:
                    print(f"An Error has occurred: {e}")
            elif direction == "3":
                print("\n1. Add a new author \n2. View author details \n3. Display all authors \n4. Exit to menu")
                author_choice = input("Enter your choice: ")
                try:
                    if author_choice == "1":
                        library.add_author()
                    elif author_choice == "2":
                        library.view_author()
                    elif author_choice == "3":
                        library.display_authors()
                    elif author_choice == "4":
                        print("returning to main menu")
                    else:
                        print("Please enter a valid choice")
                except Exception as e:
                    print(f"An Error has occurred: {e}")
            elif direction == "4":
                print("\n1. Add a new genre \n2. View genre details \n3. Display all genres \n4. Exit to menu")
                genre_choice = input("Enter your choice: ")
                try:
                    if genre_choice == "1":
                        library.add_genre()
                    elif genre_choice == "2":
                        library.view_genre()
                    elif genre_choice == "3":
                        library.display_genres()
                    elif genre_choice == "4":
                        print("returning to main menu")
                    else:
                        print("Please enter a valid choice")
                except Exception as e:
                    print(f"An Error has occurred: {e}")
            elif direction == "5":
                print("Thank you for visiting the library! Have a great day!")
                break
            else:
                print("Enter a valid choice")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()