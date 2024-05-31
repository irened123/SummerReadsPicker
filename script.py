from data import *
from intro import *

print_intro()

# Code for user interaction

end_program = False

while (not end_program):
    user_input = str(input("\nWhich genre are you interested in reading?\nTo see if it's here, type the beginning of this genre and press enter.\n"))
    
    # Search for genres that begin the same as the user input.
    matching_genres = []
    for item in genres:
        if (item.startswith(user_input)):
            matching_genres.append(item)
    
    print("\nBased on the letters you've entered, your choices are ", matching_genres)
    
    if len(matching_genres) == 1:
        selected_genre = matching_genres[0]
        next_step = str(input("Your only choice is " + selected_genre + ". Enter 'y' if you want to view the top three book recommendations for this genre. Otherwise, enter 'n'.\n"))

        # Display top three book recommendations of selected genre
        if next_step == 'y': 
            diff_books = ["FirstBook", "SecondBook", "ThirdBook"]
            for item in diff_books:
                print(f"\nName: {book_recommendations[selected_genre][item]["name"]}")
                print(f"Author: {book_recommendations[selected_genre][item]["author"]}")
                print(f"Ratings: {book_recommendations[selected_genre][item]["rating"]}")
                print(f"Keywords: {book_recommendations[selected_genre][item]["keywords"]}")
                
            
                
                
            
        
        
    
    
    
    
    
    



