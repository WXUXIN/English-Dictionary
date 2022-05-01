# English Dictionary for Beginners
#### Video Demo:  https://youtu.be/LPDmERXKvmo
#### Description:

**Hello World!**


The title for my final project is "English Dictionary for Beginners". The purpose of this web application is to allow amateur english learners to search for words and save them onto the web application with thier own notes, allowing them to view all their saved words and notes at a later time!

I used flask to run this web application. The first folder "flask_session" is to store all the sessions from all the users of the website. The static folder contains file "styles.css" that stores all the CSS code to beautify the website, books.jpg is the image I used for all of the background of the website.


In templates folder, it contains 11 html files that makes up the website.

1.) layout.html was used as a template for all of the other html pages except for search.html

2.) login.html gives us the login page

3.) register.html gives us the register page

4.) start.html gives us the home page for the website, it also displays all of the words, notes, date and time for all of the words saved

5.) failure.html displays an error message if the passoword field in login.html is not filled, or the password filled in is not the same as the password that was registerd into the database

6.) r1failure.html displays an error message when the username field in register.html is not filled

7.) r2failure.html displays an error message when the username is already taken

8.) r3lfailure.html displays an error message when the password field in register.html is not filled or if the 2 passwords are not the same

9.) r4lfailure.html displays an error message when the password field in register.html is not at least 9 characters long

10.) search.html displays the search page, which includes a iframe to dictionary.com and a div where the users can sae their words and notes

11.) searchfailure.html displays an error message when the user accidentaly submits no words but wants to submit a note'


app.py contains all of the python code used

helpers.py includes the login_required function that forces users to be logged in to access certain pages of the website, used in app.py

project.db contains users and words table that contains the users' information and all words saved amoung all the users respectively

requirements.txt includes all the modules needed to run this web application used in app.py

The following were some of the design difficulty:

1.) I had a difficult time centering all of the elements in all of the pages, especially on the search.html page where I had to reposition the save word div multiple times till I got the position I wanted.

2.) The background of the pages also took me a long while to find as it was difficult to find a background that I liked and also suitable for a website.

3.) Lastly it was difficult to actually design the logout button as i wanted it to be at the right side of the page and it took me a long while to actually find out how to do it.
