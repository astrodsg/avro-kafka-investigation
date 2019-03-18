#!env bash

# https://stackoverflow.com/questions/16284399/purge-kafka-topic 

DOCKER_COMPOSE_FILE='../cp-docker-images/examples/cp-all-in-one/docker-compose.yml'

docker-compose -f $DOCKER_COMPOSE_FILE \
    exec broker \
    kafka-topics \
    --zookeeper zookeeper:2181 \
    --alter --topic $1 \
    --config retention.ms=1

sleep 1

docker-compose -f $DOCKER_COMPOSE_FILE \
    exec broker \
    kafka-topics \
    --zookeeper zookeeper:2181 \
    --alter --topic $1 \
    --config retention.ms=86400000
