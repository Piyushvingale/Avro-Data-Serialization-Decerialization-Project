# Library imports
import csv
import avro.schema
from output import SpecificDatumReader as MovieReader
from avro.datafile import DataFileReader
from avro.io import DatumReader

# Reading MovieDb schema file
schema = avro.schema.parse(open("target/schema/MovieDb.avsc", "rb").read())

# Opening avro file for reading and writing records from avro to csv files
with open('output/hindi_movies.avro', 'rb') as f:
    reader = DataFileReader(f, MovieReader(readers_schema=schema))
    with open('output/movies_list_output.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = ['Movie', 'Genre', 'Director', 'Actors'])
        writer.writeheader()
        for i in reader:
            for j in i.movies:
               writer.writerow({'Movie': j.name, 'Genre': ','.join(j.genre), 'Director': ','.join(j.director), 'Actors': ','.join(j.actor)})
    reader.close()
