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