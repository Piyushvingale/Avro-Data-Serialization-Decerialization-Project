from avro.datafile import DataFileReader
from avro.io import DatumReader

reader = DataFileReader(open("hindi_movies.avro", "rb"), DatumReader())
for movie_record in reader:
    print(movie_record)
reader.close()
