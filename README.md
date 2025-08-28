Hi! 

In this project, im taking on the task of building a webscraper that scours the web to collect data on bubble tea shops in london! 

I love tea so why not combine my love for tea with my desire to develop my coding abilities. 

The aim of this project is to: 
- Improve my ability to code in python. 
- Create a small program that collects data which I could use for my SQL and python projects. 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Attempt 1: (27/08/2025)
Attempted to create an a webscraper using "Building a Web Scraping Tool in Python | Step-by-Step Tutorial" by Masterng Programming. 

Was using this link as my target: 
    https://www.google.com/search?sa=X&sca_esv=ba24c2d2484ecd3d&tbm=lcl&sxsrf=AE3TifOBVBcsDZOoPSp6xTxbxqxHLireEw:1756331709703&q=bubble+tea+shops+in+central+london&rflfq=1&num=10&ved=2ahUKEwj6rai9_auPAxVtVUEAHav-AJoQjGp6BAgvEAE&biw=1197&bih=1190&dpr=0.8#rlfi=hd:;si:;mv:[[51.5400213,0.0467541],[51.507119100000004,-0.15539809999999998]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2

I ran the code but didn't receive any results on terminal. 

I figured this could be due to multiple reasons: 
- Wrong targets i.e. "class" 
- No variables being stored as a result hence no out put

Upon some research, I identified that most sites can potentially stop web scraping and could also be against terms of service. 


Plan of action: 
In my research I identified that a Google API could be used for web scraping which is a legal work around. 
The API in question is places API. 
I could potentially use this api moving forward. 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

(28/08/2025)
After further Reading I discovered that the Google Places API costs money. 

Time to find a free alternative. Or make one. 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Attempt 2: (27/08/2025)

Tried to use Selenium library which opens the browser dynamically and can extract elements once page has rendered. 

Again, nothing was being posted on my terminal. 

Decided to run the code provided by on the link "https://www.geeksforgeeks.org/python/python-web-scraping-tutorial/" and got results on the terminal! This meant a few things: 

    The issue could most definitely be the website itself preventing my script from scraping. it is google after all.

    Wrong target classes could be an issue - they can potentially change and in the case with one of my targets, it had a space which meant that it also probably was a changing/mutable class. 

Plan of Action: 
    FIND WORK ARROUNDS? 
    Look for more suitable targets for my script to scrape. 

I want to scrape websites with a lot of data so that I can get a bigger data set to manipulate for my projects but it migth be the case where i would need to use an official api to collect the data. 

Through my research I saw someone use the yelp api to scrape their reviews for bubble tea shops. might have to do the same. but i really want this to work!

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
