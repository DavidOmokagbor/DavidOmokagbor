def welcome_user():
    # Get user's name
    name = input("Please enter your name: ")
    
    # Welcome message
    print(f"\nWelcome, {name}! 👋")
    
    # Get user's favorite programming language
    language = input("What's your favorite programming language? ")
    
    # Display personalized message
    print(f"\nThat's great! {language} is an excellent choice!")
    print("Thanks for using our program. Have a wonderful day! 🌟")

if __name__ == "__main__":
    welcome_user() 