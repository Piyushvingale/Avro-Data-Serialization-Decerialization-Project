# Library imports
from avrogen import write_protocol_files

# Setting path for avpr file and output folder
myfile= "target/schema/hindi_movie.avpr"
output_directory = "output"

# Reading avpr file into json
with open(myfile, 'r') as fh:
    protocol_json=fh.read().replace('\n', '')

# Writing protocol to output folder using json
write_protocol_files(protocol_json, output_directory,use_logical_types=False)
