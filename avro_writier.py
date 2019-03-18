import avro
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

if __name__ == '__main__':

    # write with schema v1
    schema_file = 'schemas/schema_v1.json'
    avro_file = 'data/users_v1.avro'
    with open(schema_file) as f:
        schema = avro.schema.Parse(f.read())
    with DataFileWriter(open(avro_file, 'wb'), DatumWriter(), schema) as dfw:
        dfw.append({"name": "Alyssa", "favorite_color": "red"})
        dfw.append({"name": "Ben"})
        dfw.append({"name": "Tim", "favorite_color": "green"})
        try:
            dfw.append({"favorite_color": "emerald"})
        except avro.io.AvroTypeException:
            pass 

    # write with schema v2
    schema_file = 'schemas/schema_v2_add_field.json'
    avro_file = 'data/users_v2.avro'
    with open(schema_file) as f:
        schema = avro.schema.Parse(f.read())
    with DataFileWriter(open(avro_file, 'wb'), DatumWriter(), schema) as dfw:
        dfw.append({"name": "Alyssa", "age": 2, "favorite_color": "red"})
        dfw.append({"name": "Ben", "age": 99, "favorite_color": "Blue"})
        dfw.append({"name": "Tim", "age": 10})


    # write with both schema v1 and v2 in the same file
    avro_file = 'data/users_v1_and_v2.avro'
    schema_file = 'schemas/schema_v1.json'

    with open(schema_file) as f:
        schema = avro.schema.Parse(f.read())
    with DataFileWriter(open(avro_file, 'wb'), DatumWriter(), schema) as dfw:
        dfw.append({"name": "Alyssa", "favorite_color": "red"})
        dfw.append({"name": "Ben"})
        dfw.append({"name": "Tim", "favorite_color": "green"})

    schema_file = 'schemas/schema_v2_add_field.json'
    with open(schema_file) as f:
        schema = avro.schema.Parse(f.read())
    #   note: this will update the schema in the avro file
    with DataFileWriter(open(avro_file, 'wb'), DatumWriter(), schema) as dfw:
        dfw.append({"name": "Alyssa", "age": 2, "favorite_color": "red"})
        dfw.append({"name": "Ben", "age": 99, "favorite_color": "Blue"})
        dfw.append({"name": "Tim", "age": 10})





