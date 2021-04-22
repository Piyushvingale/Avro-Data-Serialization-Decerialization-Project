import avro.schema, csv
from avro.datafile import DataFileReader
from avro.io import DatumReader

schema = avro.schema.parse(open("target/schema/movie_list.avsc", "rb").read())

with open('movies_list_output.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = ['Movie', 'Genre', 'Director', 'Actors'])
    reader = DataFileReader(open('hindi_movies.avro', "rb"), DatumReader())
    writer.writeheader()
    for movie in reader:
        writer.writerow({'Movie': movie["movie"], 'Genre': ','.join(movie["genre"]), 'Director': ','.join(movie["director"]), 'Actors': ','.join(movie["actor"])})
    reader.close()
