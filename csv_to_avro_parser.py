from output.schema_classes import SchemaClasses
from avro import datafile, io
from output import SpecificDatumReader as MovieReader
import avro.schema, csv
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

movie_list = SchemaClasses.hindi.movie.movie_listClass
schema = avro.schema.parse(open("target/schema/movie_list.avsc", "rb").read())

movie = movie_list()
object_list = []

with open('hindi-movies-list.csv', newline='') as csvfile:
    for row in csv.DictReader(csvfile):
        movie = movie_list()
        movie.movie = row["Movie"]
        movie.genre = row["Genre"]
        movie.director = row["Director"]
        movie.actor = row["Actors"]
        object_list.append(movie)

writer = DataFileWriter(open('hindi_movies.avro', "wb"), DatumWriter(), schema)
for i in object_list:
    writer.append({"movie": i.movie, "genre": i.genre.split(','), "director": i.director.split(','), "actor": i.actor.split(',')})
writer.close()
