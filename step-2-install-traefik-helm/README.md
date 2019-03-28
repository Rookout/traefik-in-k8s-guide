# Traefik Helm

### Guide and chart taken from: https://github.com/helm/charts/tree/master/stable/traefik

[Traefik](https://traefik.io/) is a modern HTTP reverse proxy and load balancer made to deploy
microservices with ease.

## Introduction

This bootstraps Traefik as a Kubernetes ingress controller with optional support for SSL and
Let's Encrypt.

## Installing the Chart

To install the chart (Default namespace)

```bash
$ helm install stable/traefik --name traefik  --set rbac.enabled=true --set kubernetes.ingressClass=traefik
```

Great - now we should have traefik up and running! 

You check it worked by running this

```bash
$ kubectl get pods
```

And you should by something like this:
```bash
traefik-XXXX 0/1     Running   0          12s
```

---
[//]: #URLs

   [helm]: <https://helm.sh/>
