from avrogen import write_protocol_files 

myfile= "hindi_movie.avpr"
output_directory = "output"

with open(myfile, 'r') as fh:
    protocol_json=fh.read().replace('\n', '')

write_protocol_files(protocol_json, output_directory,use_logical_types=False) 
