### App Building

Python flask application uses Prometheus Client to create expose `Guage` data. In this application, `hsi_cpu_usage` 
used to register the CPU usage in percentage value.

Build Docker Container
```shell
docker build -t flask-demo:0.10 .
```

Tag Docker container, remember to replace PROJECT_ID to your project id
```shell
docker tag flask-demo:0.10 gcr.io/PROJECT_ID/flask-demo:0.10
```

Push docker container to GCR under your project, remember to replace PROJECT_ID to your project id
```shell
docker push gcr.io/PROJECT_ID/flask-demo:0.10
```
