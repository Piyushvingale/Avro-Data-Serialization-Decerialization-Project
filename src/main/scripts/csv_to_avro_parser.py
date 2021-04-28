# Library imports
import csv
import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter
from output.hindi.movie import Movie,MovieDb

# Reading avro file and schema file
schema = avro.schema.parse(open("target/schema/MovieDb.avsc", "rb").read())
writer = DataFileWriter(open('output/hindi_movies.avro', "wb"), DatumWriter(), schema)

# Creating object of MovieDb
movie_db = MovieDb()

# Reading Csv file and storing it into MovieDb with Movie object
with open('data/hindi-movies-list.csv', newline='') as csvfile:
    for row in csv.DictReader(csvfile):
        movie = Movie()
        movie.name = row["Movie"]
        movie.genre = row["Genre"].split(",")
        movie.director = row["Director"].split(",")
        movie.actor = row["Actors"].split(",")
        movie_db.movies.append(movie)

# Writing movie_db to avro file and closing the file
writer.append(movie_db)
writer.close()
