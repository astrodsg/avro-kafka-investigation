

# Avro Reading and Writing

## Writing Avro
I created a file named "avro_writer.py" which uses the `avro-python3` library (not the `avro` library) in python to write avro files. This [getting started with python](https://avro.apache.org/docs/1.8.2/gettingstartedpython.html) post on apache helped me get going in under 30 minutes (note: it's written for python2 so a bit outdated). 

In the "avro_writer.py" I ran the following tests. 

1. write to a file with a giving schema, also check incorrect writing.
1. write to a new file with an updated schema.
1. write to a single file with both schemas. 

## Reading Avro
I created a file named "avro_reader.py" which also uses the `avro-python3` library. 

I ran the following tests

1. read without a schema
1. read with the right schema
1. read with an old schema
1. read a mixed schema file with the new schema
1. read with an incomplete schema (missing fields)
1. read with an incompatible schema to see if it fails

## Reading from command line

Following the tutorial [Reading and Writing Avro Files from the Command Line](https://www.michael-noll.com/blog/2013/03/17/reading-and-writing-avro-files-from-the-command-line/) I'm able to use the command line to read the files with and without a schema. You can download [avro-tools-1.8.2.jar](http://www.us.apache.org/dist/avro/stable/java/avro-tools-1.8.2.jar)

    java -jar avro-tools-1.8.2.jar tojson users_v1.avro


# Message Schemas 

## Benefits of Schema Evolution

[schema evolution](https://docs.oracle.com/database/nosql-12.2.4.4/GettingStartedGuide/schemaevolution.html#schemaevolutionhow)
* A field with a default value is added.
* A field that was previously defined with a default value is removed.
* A field's doc attribute is changed, added or removed.
* A field's order attribute is changed, added or removed.
* A field's default value is added, or changed.
* Field or type aliases are added, or removed.
* A non-union type may be changed to a union that contains only the original type, or vice-versa.

Other links
* https://avro.apache.org/docs/1.8.1/spec.html
* https://docs.confluent.io/current/schema-registry/docs/avro.html
* https://github.com/ottomata/kafka-connect-jsonschema

# With Confluent Kafka

Installing via the [Confluent Quick Start Instructions](https://docs.confluent.io/current/quickstart/cos-docker-quickstart.html). I went through all the steps to set up the `cp-all-in-one` container, have it running, and test it. 

For python, using the [Confluent Python Library](https://github.com/confluentinc/confluent-kafka-python). 

    docker-compose exec broker kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic example.users

    docker-compose exec broker kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic example.numtest

Note: our stage kafka should have a check which looks for what topics are there. The producers can auto generate topics which could get unruly if not maintained.  

Note: schema registry kind of sucks. 
















