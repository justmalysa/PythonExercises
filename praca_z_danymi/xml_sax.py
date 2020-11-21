import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
       self.currentdata = ""

   def startElement(self, tag, attributes):
       self.currentdata = tag
      
   def characters(self, content):
       if self.currentdata == "title":
           print("movie title is ", content)
       elif self.currentdata == "year":
           print("movie year is ", content)
       elif self.currentdata == "rating":
           print("movie rating is ", content)
       elif self.currentdata == "watched":
           print("movie is watched ", content)
           
   def endElement(self, tag):
       self.currentdata = ""


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = MovieHandler()
parser.setContentHandler( Handler )
parser.parse("movies.xml")
