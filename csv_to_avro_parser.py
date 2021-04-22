import avro.schema, csv
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

schema = avro.schema.parse(open("target/schema/movie_list.avsc", "rb").read())

writer = DataFileWriter(open('hindi_movies.avro', "wb"), DatumWriter(), schema)
with open('hindi-movies-list.csv', newline='') as csvfile:
    for row in csv.DictReader(csvfile):
        writer.append({"movie": row['Movie'], "genre": row['Genre'].split(','), "director": row['Director'].split(','), "actor": row['Actors'].split(',')})
writer.close()
