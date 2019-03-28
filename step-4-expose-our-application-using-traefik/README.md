# Install the ingress:

Now everything is set - time to expose our application to the world!

We are going to use a ingress 


1. We define the ingress object
2. We give it a name
3. GKE (where our demo is running) - assume all ingress are google ingress ->
	This is why we give it a class
	```yaml
	annotations:
	 kubernetes.io/ingress.class: traefik
	```
4. We add routing rules to the ingress, This rules config our traefik frontend:
	* We match by host( `traefik.rookout-demo.com`)
	* We match by path (`path: /`)
	
	Then we add the backend:
	* backend: `hello-world-service:80`
```yaml
  - host: traefik.rookout-demo.com
    http:
      paths:
      - path: /
        backend:
          serviceName: hello-world-service
          servicePort: 80
```          
5. Basically we configure our traefik, this time not using config map but using k8s ingress object! 


To install
```bash
helm install ./traefik-ingress-helm --name traefik-ingress
```

You can now visit: http://traefik.rookout-demo.com/ and check out app!

---
[//]: #URLs

   [helm]: <https://helm.sh/>
