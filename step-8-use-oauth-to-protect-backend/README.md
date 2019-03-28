# Use traefik + oauth to protect our backend:

Now let's try and add some protection for our website. 

We are going to use our old backend, but this time the ingress will use some auth mechanism BEFORE forwarding the request to backend server.
 
This can be super useful when you have a web that MUST be internet facing, but you still want to protect it.
Routing your users-requests by some unique token inside the headers and much more.

How will it look like:

Client --> Traefik --> Gatekeeper --> Service

## Traefik + oauth 

We are going to use : https://github.com/thomseddon/traefik-forward-auth to do the actual auth request.

We will deploy everything using a single helm chart:

	```bash
	helm install ./traeifik-using-oauth --name traefik-using-oauth
	```
	
We added the following lines to our ingress object:
```yaml

    ingress.kubernetes.io/auth-type: forward
    ingress.kubernetes.io/auth-url: http://traefik-oauth:4181
    ingress.kubernetes.io/auth-response-headers: X-Forwarded-User

``` 

This will make sure each request the arrive to one of our backend, will first be forwarded to traefik-oauth service.
 

Our env variable (secrets generated in advanced):
```yaml
        - name: CLIENT_ID
          valueFrom:
            secretKeyRef:
              name:  oauth-client-id
              key: token
        - name: CLIENT_SECRET
          valueFrom:
            secretKeyRef:
              name:  oauth-client-secret
              key: token
        - name: DOMAIN
          value: "rookout.com"
```


* Easy way to generate those secrets
```bash
      kubectl create secret generic oauth-client-secret --from-literal=token=YOUR_TOKEN
```



You can now try and visit: 
http://oauth-traefik.rookout-demo.com/ , sadly you can't login as your not a prat of Rookout :)

---
[//]: #URLs

   [helm]: <https://helm.sh/>
