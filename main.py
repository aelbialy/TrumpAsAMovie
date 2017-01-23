"""
This is our main python file for Trump as a Movie for January monthly Hack
"""

import requests
r = requests.get("http://www.omdbapi.com/?t=mall+Cop+&y=&plot=short&r=json")
print(r.json())
data = r.json()
print(data["imdbRating"])