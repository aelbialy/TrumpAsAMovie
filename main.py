"""
This is our main python file for Trump as a Movie for January monthly Hack
"""

import requests


movie = input("Enter movie name: ")
#print("This is your movie " + movie)
movie_title_bit = movie.replace(' ', '+')
#print(movie_title_bit)



r = requests.get("http://www.omdbapi.com/?t="+movie_title_bit+"&y=&plot=short&r=json")
#print(r.json())
data = r.json()
print(movie + "'s Movie rating is " + str(float(data["imdbRating"])*10) + "%") 
print("And Trump's Approval rating is (inserted data here)")

r = requests.get("http://elections.huffingtonpost.com/pollster/donald-trump-favorable-rating.json")
polls = r.json()['polls']
latest_poll_favourable_result = polls[len(polls) - 1]['choices']['Favorable']

print("And Trump's Approval rating is " + latest_poll_favourable_result)

print(data["imdbRating"])


