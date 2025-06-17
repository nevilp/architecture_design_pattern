FROM confluentinc/cp-kafka-connect:7.5.0
ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"
USER root
RUN rm -rf /usr/share/confluent-hub-components/debezium-debezium-connector-postgresql

# Fresh install from Confluent Hub
RUN confluent-hub install --no-prompt debezium/debezium-connector-postgresql:latest

# Install Confluent Elasticsearch Sink Connector
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-elasticsearch:13.0.0

USER appuser