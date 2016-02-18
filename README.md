# Community - local news app

# What is Community?

Community essentially gathers local news based off local news URL’s in Python, organizes it within a database connection, create a PHP-generated JSON page for Android to output the news to the user.

I thought about this idea during my Mobile App Development class and sought to enhance it during that time and possibly after. I wanted to find a way to automate data 

# Why Python?

Python uses the beautifulSoup library to search through XML tags and appends data based on its available functions.

We could however use JSoup, but there was little documentation or YouTube videos online that could help start the project quicker. On the other hand, Python’s BeautifulSoup library had a plethora of examples available online for anyone to learn it works!

Before the database access of my app became depreciated, I had a cronjob running in the background of my Linux environment.

# Why MySQL?

MySQL was not at all difficult to use or setup on a server. However, I could easily swap MySQL for MongoDB or NoSQL

# Why PHP?

This idea came from a fellow friend for security measures when establishing a database connection with your application. Ideally it would be preferable to do a socket connection with the Android and MySQL, but I opted for a JSON interaction. 

Essentially PHP creates JSON objects for Android to parse appropriately and organized into a listView for the application.


# Why Android?

I felt much more comfortable with Java’s syntax rather than Objective-C, plus it was the primary language used to teach Mobile Application during class. 
