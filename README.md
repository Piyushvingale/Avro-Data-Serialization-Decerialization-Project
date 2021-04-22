# Avro-Data-Serialization-Decerialization-Project

1. download avro-tools-1.8.2.jar <br>

2. Converting AVDL to AVPR (json format) <br>
java -jar avro-tools-1.8.2.jar idl hindi_movie.avdl hindi_movie.avpr <br>

3. Generating python code from the Avro Schema <br>
python generate_python_class.py <br>

4. Generating Schema file in JSON format - needed for processing records <br>
java -jar avro-tools-1.8.2.jar idl2schemata hindi_movie.avdl target/schema/ <br>

5. Convert CSV to Avro <br>
python csv_to_avro_parser.py <br>

6. Convert Avro to CSV <br>
python avro_to_csv_parser.py <br>

7. Read Avro file <br>
python read_avro_file.py <br>

