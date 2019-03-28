# Install demo app:

Ok great now that we have helm and traefik install - let's use it to install our demo app!

We will deploy a very simple hello-world service listening on port 80.


To install
```bash
helm install hello-world-helm --name hello-world
```

You can now use `kubectl get pods` to see the pod is up and runing.

You can also use `kubectl port-forward POD_NAME 8080:80` to check everything is working


---
[//]: #URLs

   [helm]: <https://helm.sh/>
