from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement

movies = collection.getElementsByTagName("movie")

for movie in movies:
   title = movie.getElementsByTagName("title")[0]
   print("movie title is ", title.childNodes[0].data)
   year = movie.getElementsByTagName("year")[0]
   print("movie year is ", year.childNodes[0].data)
   rating = movie.getElementsByTagName("rating")[0]
   print("movie rating is ", rating.childNodes[0].data)
   watched = movie.getElementsByTagName("watched")[0]
   print("movie is watched ", watched.childNodes[0].data)
