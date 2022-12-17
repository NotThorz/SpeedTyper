import time
import sys
import difflib
import requests
import os
from bs4 import BeautifulSoup

# Initialize the high scores dictionary
high_scores = {}

while True:
    # Clear the terminal
    os.system("cls")

    # Prompt the user for the URL of the webpage to scrape
    url = "input(\"Enter the URL of the webpage to scrape:\") "
    # u can take this as an input or just hard code it
    # Scrape the text from the webpage
    page = requests.get("http://example.com")
    soup = BeautifulSoup(page.content, "html.parser")
    text_to_type = "soup.get_text()"
    # soup.get_text() is the command but to test this program it s a string if u provided the url then u can remove the "

    # Display the countdown before starting the test
    print("3")
    time.sleep(1)
    os.system("cls")
    print("2")
    time.sleep(1)
    os.system("cls")
    print("1")
    time.sleep(1)

    # Clear the terminal
    os.system("cls")

    # Display the text to type in chunks
    chunk_size = 20
    for i in range(0, len(text_to_type), chunk_size):
        print(text_to_type[i:i+chunk_size])

    # Start the timer
    start_time = time.time()

    # Initialize the mistake counter
    mistakes = 0

    # Keep prompting the user for input until they type the text correctly
    typed_text = ""
    while True:
        # Get the user's input
        typed_text = input()
        # Check that the user's input has the same length as the original text
        if len(typed_text) != len(text_to_type):
            print(
                "Your input is not the same length as the original text. Please try again.")
            continue
        # Compare the user's input to the original text using the SequenceMatcher
        matcher = difflib.SequenceMatcher(None, typed_text, text_to_type)
        if matcher.ratio() < 1.0:
            # If the user made a mistake, increment the mistake counter and display the incorrect characters in red
            mistakes += 1
            for i in range(len(text_to_type)):
                if typed_text[i] != text_to_type[i]:
                    print("\033[31m" + typed_text[i] + "\033[0m", end="")
                else:
                    print(typed_text[i], end="")
            print()
            print("You made a mistake. Please try again.")
        else:
            # If the user typed the text correctly, break out of the loop
            break

    # Stop the timer
    end_time = time.time()

    # Calculate the elapsed time in minutes
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60

    # Clear the terminal
    os.system("cls")
    # Display the words per minute score and the number of mistakes
    print("Words per minute: {:.2f}".format(
        len(text_to_type.split()) / minutes))
    print("Number of mistakes: {}".format(mistakes))
    # Update the high scores dictionary
    # Update the high scores dictionary
    user_name = input("Enter your name: ")
    if user_name in high_scores:
        if high_scores[user_name]["wpm"] < len(text_to_type.split()) / minutes:
            high_scores[user_name] = {
                "wpm": len(text_to_type.split()) / minutes,
                "mistakes": mistakes
            }
    elif user_name not in high_scores:
        high_scores[user_name] = {
            "wpm": len(text_to_type.split()) / minutes,
            "mistakes": mistakes
        }

    # Display the high scores
    print("\nHigh Scores:")
    for name, score in high_scores.items():
        print("{}: {:.2f} wpm, {} mistakes".format(
            name, score["wpm"], score["mistakes"]))

    # Prompt the user to try again or close the program
    while True:
        choice = input("\nWould you like to try again? (y/n) ")
        if choice.lower() == "n":
            sys.exit()
        else:
            break
