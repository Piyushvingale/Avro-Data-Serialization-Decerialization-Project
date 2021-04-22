1. download avro-tools-1.8.2.jar

2. Converting AVDL to AVPR (json format)
java -jar avro-tools-1.8.2.jar idl hindi_movie.avdl hindi_movie.avpr

3. Generating python code from the Avro Schema
python generate_python_class.py

4. Generating Schema file in JSON format - needed for processing records
java -jar avro-tools-1.8.2.jar idl2schemata hindi_movie.avdl target/schema/

5. Convert CSV to Avro
python csv_to_avro_parser.py

6. Convert Avro to CSV
python avro_to_csv_parser.py

7. Read Avro file
python read_avro_file.py

