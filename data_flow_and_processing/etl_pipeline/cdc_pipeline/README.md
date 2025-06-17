

docker exec -it cdc_pipeline-elasticsearch-1 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic


curl -X POST -H "Content-Type: application/json" --data @connect/elasticsearch-sink.json http://localhost:8083/connectors

curl -X POST -H "Content-Type: application/json" --data @connect/postgres-connector.json http://localhost:8083/connectors

curl -X GET http://localhost:8083/connectors

curl -X DELETE http://localhost:8083/connectors/postgres-connectompo

#to delete old kafka topics
kafka-topics --bootstrap-server localhost:29092 --delete --topic ecommerce_server.public.products

kafka-console-consumer \
  --bootstrap-server localhost:29092 \
  --topic ecommerce_server.public.products \
  --from-beginning \
  --max-messages 10

{
    "name": "postgres-connector",
    "config": {
      "transforms": "unwrap",
      "transforms.unwrap.type": "io.debezium.transforms.ExtractNewRecordState",
      "transforms.unwrap.drop.tombstones": "false"  ,
      "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
      "plugin.name": "pgoutput",
      "tasks.max": "1",
      "database.hostname": "postgres",
      "database.port": "5432",
      "database.user": "postgres",
      "database.password": "password",
      "database.dbname": "ecommerce",
      "database.server.name": "ecommerce_server", 
      "topic.prefix": "ecommerce_server",           
      "table.include.list": "public.products",
      "slot.name": "debezium",
      "key.converter": "org.apache.kafka.connect.json.JsonConverter",
      "value.converter": "org.apache.kafka.connect.json.JsonConverter",
      "key.converter.schemas.enable": "false",
      "value.converter.schemas.enable": "false",
      "snapshot.mode": "initial"
    }
  }




