# speedtyper
This script is a simple typing test that prompts the user to type a passage of text as quickly and accurately as possible. It calculates the user's words per minute (WPM) score and displays it, along with the number of mistakes made. The script also maintains a list of high scores.

#Dependencies
This script requires the following libraries:

time
sys
difflib
requests
os
bs4
#Usage
To run the script, simply execute it in your terminal:


python typing_test.py


The script will prompt the user for the URL of the webpage to scrape and display the text to type. After the user has finished typing, it will display their WPM score and the number of mistakes made. The user can then enter their name to save their score in the high scores list.

The script will repeat this process until the user exits the program by pressing CTRL + C.

#Customization
You can customize the following aspects of the script:

The chunk size (the number of characters displayed at a time) can be modified by changing the chunk_size variable.
The countdown before the test starts can be skipped by removing the lines of code that display the countdown and sleep.
The high scores list can be reset by deleting the high_scores dictionary.
