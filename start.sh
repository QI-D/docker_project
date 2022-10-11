docker build -t qidang/project1:frontend frontend/
docker build -t qidang/project1:backend backend/
docker build -t qidang/project1:storage storage/
docker network create -d bridge project1
docker-compose up