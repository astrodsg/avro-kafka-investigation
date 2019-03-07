import avro
from avro.datafile import DataFileReader
from avro.io import DatumReader



def read_avro_simple(avro_filepath):
    print("\nfile:{}".format(avro_filepath))
    with open(avro_filepath, 'rb') as f:
        with DataFileReader(f, DatumReader()) as dfr:
            for record in dfr:
                print(record)

def read_avro_with_schema(avro_filepath, schema_filepath):
    print("\nfile:{}\nschema:{}".format(avro_filepath, schema_filepath))

    with open(schema_filepath) as f:
        schema = avro.schema.Parse(f.read())

    datum_reader = DatumReader(reader_schema=schema)
    with open(avro_filepath, 'rb') as f:
        with DataFileReader(f, datum_reader) as dfr:
            for record in dfr:
                print(record)

if __name__ == '__main__':

    # read without schema
    avro_filepath = 'data/users_v1.avro'
    read_avro_simple(avro_filepath)

    # read with the right schema
    avro_filepath = 'data/users_v1.avro'
    schema_filepath = 'schemas/schema_v1.json'
    read_avro_with_schema(avro_filepath, schema_filepath)

    # read with old schema
    avro_filepath = 'data/users_v2.avro'
    schema_filepath = 'schemas/schema_v1.json'
    read_avro_with_schema(avro_filepath, schema_filepath)

    # read mixed schema file with new schema
    avro_filepath = 'data/users_v1_and_v2.avro'
    schema_filepath = 'schemas/schema_v2_add_field.json'
    read_avro_with_schema(avro_filepath, schema_filepath)

    # read with subset of fields
    avro_filepath = 'data/users_v1.avro'
    schema_filepath = 'schemas/schema_v4_read_subset.json'
    read_avro_with_schema(avro_filepath, schema_filepath)

    # read with incompatible schema
    avro_filepath = 'data/users_v1.avro'
    schema_filepath = 'schemas/schema_v3_incompatible.json'
    try:
        read_avro_with_schema(avro_filepath, schema_filepath)
    except avro.schema.SchemaParseException as e:
        print(e)




