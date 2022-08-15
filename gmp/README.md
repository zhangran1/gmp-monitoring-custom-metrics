### PodMonitoring Resource Section

Remember to replace your project id under `flask-demo.yaml`. To adjust the Prometheus Scrape interval for `flask-exam`, 
change `interval` value, as of 15 Aug 2022, the minimum interval Google Managed Prometheus supports is 5 second. 

```shell
kubectl -n gmp-test apply -f flask-demo.yaml
kubectl -n gmp-test apply -f flask-monitoring.yaml
```

To troubleshoot the `flask-example` pod locally
```shell
kubectl port-forward POD_NAME 8080 -n gmp-test
```

To delete the pod and Pod monitoring
```shell
kubectl -n gmp-test delete -f flask-demo.yaml
kubectl -n gmp-test delete -f flask-monitoring.yaml
```