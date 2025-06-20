    FROM confluentinc/cp-kafka-connect:7.5.0
    ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"
    USER root

    # Download and extract Debezium PostgreSQL connector
    RUN mkdir -p /usr/share/confluent-hub-components/debezium-connector-postgres && \
        curl -L https://repo1.maven.org/maven2/io/debezium/debezium-connector-postgres/2.4.1.Final/debezium-connector-postgres-2.4.1.Final-plugin.tar.gz \
        -o /tmp/debezium-connector-postgres.tar.gz && \
        tar -xvzf /tmp/debezium-connector-postgres.tar.gz -C /usr/share/confluent-hub-components/debezium-connector-postgres && \
        rm /tmp/debezium-connector-postgres.tar.gz
    
 

    # Install Confluent Elasticsearch Sink Connector
    RUN confluent-hub install --no-prompt confluentinc/kafka-connect-elasticsearch:14.0.9

    USER appuser