

docker ps -a | awk '/pyt-classifier/{print "docker kill "$1"\ndocker rm -f "$1}'|sh
docker run --name pyt-classifier -p 5000:5000 pyt-classifier
