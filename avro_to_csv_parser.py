import avro.schema, csv
from output.schema_classes import SchemaClasses
from avro import datafile, io
from output import SpecificDatumReader as MovieReader
from avro.datafile import DataFileReader
from avro.io import DatumReader

movie_list = SchemaClasses.hindi.movie.movie_listClass
schema = avro.schema.parse(open("target/schema/movie_list.avsc", "rb").read())

movie = movie_list()
object_list = []

with open('hindi_movies.avro', 'rb') as f:
    reader = datafile.DataFileReader(f, MovieReader(readers_schema=schema))
    for i in reader:
        movie = movie_list()
        movie.movie = i.movie
        movie.genre = i.genre
        movie.director = i.director
        movie.actor = i.actor
        object_list.append(movie)
    reader.close()

with open('movies_list_output.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = ['Movie', 'Genre', 'Director', 'Actors'])
    writer.writeheader()
    for movie in object_list:
        writer.writerow({'Movie': movie.movie, 'Genre': ','.join(movie.genre), 'Director': ','.join(movie.director), 'Actors': ','.join(movie.actor)})
    reader.close()
