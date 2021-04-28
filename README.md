# Avro-Data-Serialization-Decerialization-Tutorial

1. Run to bash command for the following: <br>
	a. download avro-tools-1.8.2.jar <br>
	b. Converting AVDL to AVPR (json format) <br>
	c. Generating python code from the Avro Schema <br>
	d. Generating Schema file in JSON format - needed for processing records <br>
bash src/main/scripts/update_class.sh

2. Convert CSV to Avro <br>
python src/main/scripts/csv_to_avro_parser.py

3. Convert Avro to CSV <br>
python src/main/scripts/avro_to_csv_parser.py

4. Read Avro file <br>
python src/main/scripts/read_avro_file.py

