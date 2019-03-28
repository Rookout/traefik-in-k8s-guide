# Use traefik to split traffic by headers:

Now we are going to use some capabilities unique to traefik! 

We are going to route our traffic, not by the url patam but using the request headers.

This can be super useful:
 
Testing a new environment (using the header) and old one at the same time.

Routing your users-requests by some unique token inside the headers and much more.

Sadly k8s dosn't support route by header, so we are going to deploy a traefik container and use a configmap to config it.

## Route by headers 

We will deploy everything using a single helm chart:
	```bash
	helm install ./traefik-split-by-headers --name traefik-split-by-headers --namespace headers
	```
	
This time the route is done by the configmap.yaml:
```yaml
    [frontends.catchall]
    backend = "backend1"
      [frontends.catchall.routes.catchallrule]
        rule = "PathPrefix:/"
      [frontends.frontend1]
      backend = "backend1"
        [frontends.frontend1.routes.test_1]
          rule = "Headers:backend-version,1"

      [frontends.frontend2]
      backend = "backend2"
        [frontends.frontend2.routes.test_1]
          rule = "Headers:backend-version,2"

``` 

We load the config map using a volume:
```yaml
      volumes:
      - name: config
        configMap:
          name: traefik
```
And we also make sure have the latest config in each deployment:
```yaml
      annotations:
        checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
```



You can now visit: http://headers.traefik.rookout-demo.com/ try adding `backend-version:1` in the headers and see what happen!

---
[//]: #URLs

   [helm]: <https://helm.sh/>
