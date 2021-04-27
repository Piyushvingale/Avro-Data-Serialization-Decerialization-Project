import csv
from avro import datafile, io
from output import SpecificDatumReader as MovieReader
import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

from output.hindi.movie import Movie,MovieDb
from output.schema_classes import SchemaClasses

#movie_list = SchemaClasses.hindi.movie.movie_listClass
schema = avro.schema.parse(open("target/schema/MovieDb.avsc", "rb").read())

movie_db = MovieDb()
object_list = []
with open('hindi-movies-list.csv', newline='') as csvfile:
    for row in csv.DictReader(csvfile):
        movie = Movie()
        movie.name = row["Movie"]
        movie.genre = row["Genre"].split(",")
        movie.director = row["Director"].split(",")
        movie.actor = row["Actors"].split(",")
        movie_db.movies.append(movie)
        #break

writer = DataFileWriter(open('hindi_movies.avro', "wb"), DatumWriter(), schema)
writer.append(movie_db)
writer.close()
