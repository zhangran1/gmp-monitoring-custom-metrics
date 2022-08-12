#### Quick Start

gmp folder: kubernetes deployment script

src folder: python sample application to customize metrics


Create cluster
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

References

1. How to set up Prometheus monitoring for your services https://www.youtube.com/watch?v=qyfOE_78nT0
2. https://github.com/GoogleCloudPlatform/python-docs-samples/blob/3df11db721a99ffaf19d3d9dc8cb4c838f725b28/monitoring/prometheus/main.py
3. Get started with managed collection https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed
4. Prometheus API https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.4.3-gke.0/doc/api.md#podmonitoringspec
5. Prometheus Python Client https://github.com/prometheus/client_python
