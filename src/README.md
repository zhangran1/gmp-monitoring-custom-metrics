
Build Docker Container
```shell
docker build -t flask-demo:0.10 .
```

Tag Docker container
```shell
docker tag flask-demo:0.10 gcr.io/exploration-351204/flask-demo:0.10
```

Push docker container to GCR under your project
```shell
docker push gcr.io/exploration-351204/flask-demo:0.10
```
