#!env bash

# https://stackoverflow.com/questions/16284399/purge-kafka-topic 

DOCKER_COMPOSE_FILE='../cp-docker-images/examples/cp-all-in-one/docker-compose.yml'

docker-compose -f $DOCKER_COMPOSE_FILE \
    run broker \
    kafka-configs --alter --entity-type topics \
    --zookeeper zookeeper:2181 \
    --add-config retention.ms=1 \
    --entity-name $1

docker-compose -f $DOCKER_COMPOSE_FILE \
    run broker \
    kafka-topics \
    --zookeeper zookeeper:2181 \
    --delete --topic $1 
