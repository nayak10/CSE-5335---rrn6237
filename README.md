# WebDataProject1
a. What server framework did you choose and why?

	This web application was developed using the Flask framework (A framework used for Python Programming language).
The flask framework is relatively new compared to other Python frameworks like Django and Pyramid and it is used for primarily
small applications. Flask is more flexible when compared to Django framework (for storage etc).
As I researched on which framework to use, I learned that Flask is easier for beginners (like me).

b. What client framework did you choose and why?
	The client side was developed using HTML, JQuery and AJAX. The interaction with the server side program is easy with client-side
	languages like Javascript and JQuery. Javascript is easily readable, and I had some prior experience with it.
	
c. What aspect of the implementation did you find easy, if any, and why?
	The server side implementation was easier than the client side because the server had to just pass the JSON data as it is, so
	that the client side interprets it and displays the data on the browser. There were lot of examples which I could find and easily understand
	the logic of implementation.
	
d. What aspect of the implementation did you find hard, if any, and why?
	Initially, I planned to use the data from the Weather API (wunderground API) which fetched data and returned it in the JSON format.
	The interpretation of this JSON data was hard to implement on the client side, because the data was not very well structured. Because of this,
	the data had to be formatted to display it on the browser. Hence, I used my own set of JSON data on the server side and then pulled it 
	to the client side to display dynamically on the browser.
	
e. What components OTHER than your client and server framework did you install,
if any, and if so, what is their purpose for your solution?
	Libraries like JSON, urllib2 were used on the server side to read the JSON data from the API side.
	JQuery Library was used on the client side to use Jquery functions.
	
f. What Ubuntu commands are required to deploy and run your server?
