1. Run to bash command for the following:
	a. download avro-tools-1.8.2.jar
	b. Converting AVDL to AVPR (json format)
	c. Generating python code from the Avro Schema
	d. Generating Schema file in JSON format - needed for processing records
bash src/main/scripts/update_class.sh

2. Convert CSV to Avro
python src/main/scripts/csv_to_avro_parser.py

3. Convert Avro to CSV
python src/main/scripts/avro_to_csv_parser.py

4. Read Avro file
python src/main/scripts/read_avro_file.py

