
docker rm -f naa
docker build -t naa-img .
docker tag naa-img mamedshahmaliyev/naa:1
docker push mamedshahmaliyev/naa:1
docker run --name=naa -it -d -p 8001:80 naa-img
# docker rm -f naa