docker compose build deployment
docker tag portfolio-deployment:app registry.digitalocean.com/peterjung/portfolio-app:latest
docker push registry.digitalocean.com/peterjung/portfolio-app:latest
