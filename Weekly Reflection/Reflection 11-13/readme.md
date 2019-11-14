I spent this refelction working on the first two exercises from Monfort, familiarizing myself with using Java in Processing. 
Although Montfort's book has been very helpful in building a great foundation fro understanding python, I do not quite see the purpose of using Java while in Processing. I personally think it would be much more beneficial to continue to stick with Python through the Processing chapters in the book. 
Regardless, I see Processing as an amazing IDE that I hope to use much more frequently in the future. 
I did run into a snag while following along in the book. In the first exercise we are given some code to try:

for(int circle = 0 ; circle <= 30 ; circle = circle + 1) {
     ellipse(790 – ((780/30) * circle), 10 + ((580/30) * circle), 20, 20);
    }

I receive an error that says "The left hand side of the assignment must be a variable." I tried changing some things around but could not get that code to run properly. To my understanding, ellipse() just requires the parameters for the ellipse. Why would Processing be loking for a variable at the begining of elipse(). 