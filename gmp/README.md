Deploy flask demo app and deploy Podmonitoring
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