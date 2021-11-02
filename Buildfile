docker build -t register .
docker tag register acobley/register
docker push acobley/register
docker stop register
docker rm register
docker run -p 5000:5000 --name register --link some-mysql:mysql acobley/register