
cd $(dirname $0)

docker ps -a | awk '/pyt-classifier/{print "docker kill "$1"\ndocker rm -f "$1}'|sh
docker rmi pyt-classifier

docker image build . -f Dockerfile -t pyt-classifier
