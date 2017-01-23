"""
This is our main python file for Trump as a Movie for January monthly Hack
"""

import requests

movie = input("Enter movie name: ")
print("This is your movie " + movie)
movie_title_bit = 

r = requests.get("http://www.omdbapi.com/?t=mall+Cop+&y=&plot=short&r=json")
#print(r.json())
data = r.json()
print("Mall Cop's Movie rating is " + str(float(data["imdbRating"])*10) + "%") 
print("And Trump's Approval rating is (inserted data here)")
