def get_user_info():
    # Get user's name
    name = input("Please enter your name: ")
    
    # Get user's email
    email = input("Please enter your email: ")
    
    # Welcome message
    print(f"\nWelcome, {name}! 👋")
    print(f"Email: {email}")
    
    # Get user's favorite programming language
    language = input("What's your favorite programming language? ")
    
    # Display personalized message
    print(f"\nThat's great! {language} is an excellent choice!")
    print("Thanks for using our program. Have a wonderful day! 🌟")

if __name__ == "__main__":
    get_user_info() 