# Creating required directories
mkdir -p target/schema
mkdir -p output

# Converting AVDL file to AVPR
echo "1. Converting AVDL to AVPR (json format)"
java -jar avro-tools-1.8.2.jar idl src/main/resources/hindi_movie.avdl target/schema/hindi_movie.avpr

# Generating python code from Avro Achema
echo "2. Generating python code from the Avro Schema"
python src/main/scripts/generate_python_class.py

# Generating schema file
echo "3. Generating Schema file in JSON format - needed for processing records"
java -jar avro-tools-1.8.2.jar idl2schemata src/main/resources/hindi_movie.avdl target/schema/

echo "4. Finished"
