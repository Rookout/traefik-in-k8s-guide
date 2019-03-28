# Update the ingress to expose another backend application:

Now - let's try and add another service into the mix.

In this step we are going to add another backend service, and expose it using the same ingress!

## Path-based Routing

1. We are going to deploy another deployment and backend:

	`helm upgrade --install another-hello-world-backend another-hello-world-backend`
2. We are going to expose it using a different endpoint - but using the same ingress
3. We add routing rules to the ingress, This rules config our traefik frontend:
	* We match by host( `traefik.rookout-demo.com`)
	* We match by path (`path: /`) - for the old service
	* We match by path (`path: /another`) - for the newservice
	
	```yaml
	  - host: traefik.rookout-demo.com
	    http:
	      paths:
	      - path: /another
	        backend:
	          serviceName: another-hello-world-service
	          servicePort: 80
	```
5. Again we configure our traefik, not using config map but using k8s ingress object! 


You can now visit: http://traefik.rookout-demo.com/ and http://traefik.rookout-demo.com/another/backend and check out apps!

---
[//]: #URLs

   [helm]: <https://helm.sh/>
