# Deploying another ingress to support staging/prod:

Now - let say we want to add a staging environment. 

In order to do so - we need to deploy another instance of our backend, but also another instance of traefik. 

We can use the same instance - but separate can be helpful (checking traefik config changes, high load on staging etc...).

We are going to use the ingress class in order to separate between those environment. 

## Multi ingress 

1. We will deploy a new ingress-class:
	```bash
	helm install stable/traefik --name traefik  --set rbac.enabled=true --set kubernetes.ingressClass=staging-traefik --namespace staging
	```
	Notice: `staging-traefik` ingress class
2. We will deploy the new ingress:
	```bash 
	helm upgrade --install traefik-ingress  ./traefik-ingress-helm --namespace staging
	```
	Notice we are using the new ingress-class:
	```yaml
	metadata:
	  name: base-ingress
	  annotations:
	    kubernetes.io/ingress.class: staging-traefik
	```

3. Now all we need to do is deploy our application:
	```bash
	helm upgrade --install staging-hello-world-backend staging-hello-world-backend --namespace staging
	```
5. Again we configure our traefik, not using config map but using k8s ingress object! 


You can now visit: http://traefik.rookout-demo.com/ and http://staging.traefik.rookout-demo.com/, each served using a different traefik instance !

---
[//]: #URLs

   [helm]: <https://helm.sh/>
