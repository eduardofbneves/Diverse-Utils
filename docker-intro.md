







## Remove docker volumes

Clean up resources (images, containers, volumes, networks, ...) that are dangling - not tagged or associated with a container:
```bash
docker system prune 
```

To additionally remove any stopped containers and all unused images:
```bash
docker system prune -a
```


