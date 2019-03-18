#!env bash

# https://ronnieroller.com/kafka/cheat-sheet

DOCKER_COMPOSE_FILE='../cp-docker-images/examples/cp-all-in-one/docker-compose.yml'

docker-compose -f $DOCKER_COMPOSE_FILE \
    exec broker \
    kafka-console-consumer \
    --bootstrap-server localhost:9092 \
    --topic $1 \
    --from-beginning
