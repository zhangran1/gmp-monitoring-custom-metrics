### Google Cloud Managed Service for Prometheus (GMP) with custom metrics

This repository contains sample application and PodMonitoring configuration to be used with (GMP). The sample application 
exports custom metrics and expose via metrics endpoints. Prometheus PodMonitoring Scrape interval could be adjusted in 
the PodMonitoring object.

### Getting Started
This repository include the following folders
- [gmp](gmp) - Kubernetes deployment script
- [src](src) - Python Flask sample application to customize metrics

To test the scripts, you may follow the following steps
1. Launch a GKE cluster with managed Prometheus (Refer to GKE Cluster Creation Section)
2. Containerize Python Flask sample application and deploy to GRC (Refer to App Building Section)
3. Deploy `PodMonitoring` resource (Refer to PodMonitoring Resource Section)

### GKE Cluster creation

```shell
gcloud beta container clusters create gmp-cluster --num-nodes=3 --zone asia-southeast1-a --enable-managed-prometheus
```


Create Name Space

```shell
kubectl create ns gmp-test
```

Refer gmp folder to deploy application and monitoring

Load test
```shell
kubectl -n gmp-test run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://flask-sample; done"
```

### App Building

Replace PROJECT_ID to your own project ID.

Build Docker Container
```shell
docker build -t flask-demo:0.1 .
```

Tag Docker container
```shell
docker tag flask-demo:0.10 gcr.io/PROJECT_ID/flask-demo:0.1
```

Push docker container to GCR under your project
```shell
docker push gcr.io/PROJECT_ID/flask-demo:0.1
```

### PodMonitoring Resource Section

Deploy flask demo app and deploy PodMonitoring
```shell
kubectl -n gmp-test apply -f flask-demo.yaml
kubectl -n gmp-test apply -f flask-monitoring.yaml
```

To troubleshoot the pod locally
```shell
kubectl port-forward flask-example-78d9c48c87-f2p9d 8080 -n gmp-test
```

To delete the pod and Pod monitoring
```shell
kubectl -n gmp-test delete -f flask-demo.yaml

kubectl -n gmp-test delete -f flask-monitoring.yaml
```


References

1. How to set up Prometheus monitoring for your services https://www.youtube.com/watch?v=qyfOE_78nT0
2. https://github.com/GoogleCloudPlatform/python-docs-samples/blob/3df11db721a99ffaf19d3d9dc8cb4c838f725b28/monitoring/prometheus/main.py
3. Get started with managed collection https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed
4. Prometheus API https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.4.3-gke.0/doc/api.md#podmonitoringspec
5. Prometheus Python Client https://github.com/prometheus/client_python
