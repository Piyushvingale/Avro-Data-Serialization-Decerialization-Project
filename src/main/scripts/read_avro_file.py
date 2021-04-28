# Library imports
from avro.datafile import DataFileReader
from avro.io import DatumReader

# Reading avro file
reader = DataFileReader(open("output/hindi_movies.avro", "rb"), DatumReader())

# Looping through each record
for movie_record in reader:
    print(movie_record)

# Closing DataFileReader
reader.close()
