

docker-compose exec airflow-webserver airflow users create \ 
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email nevil.p.88@gmail.com