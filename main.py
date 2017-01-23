"""
This is our main python file for Trump as a Movie for January monthly Hack
"""

import requests


movie = input("Enter movie name: ")
movie_title_bit = movie.replace(' ', '+')

r = requests.get("http://www.omdbapi.com/?t="+movie_title_bit+"&y=&plot=short&r=json")
data = r.json()

movie_rating = float(data["imdbRating"])*10
print(movie + "'s Movie rating is " + str(movie_rating) + "%")

print('pls w8...')
r = requests.get("http://elections.huffingtonpost.com/pollster/donald-trump-favorable-rating.json")
polls = r.json()['polls']
trump_rating = float(polls[len(polls) - 1]['choices']['Favorable'])

print("And Trump's Approval rating is " + str(trump_rating) + '%')

if movie_rating > trump_rating:
    print('That means ' + movie + '\'s rating is ' + str(movie_rating - trump_rating) + '% better than Trump! :D')
else:
    print('That means Trump is ' + str(trump_rating - movie_rating) + '% better than ' + movie + '! D:')






