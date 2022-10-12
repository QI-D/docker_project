docker build -t qidang/project1:analysis analysis/
docker build -t qidang/project1:frontend frontend/
docker build -t qidang/project1:backend backend/
docker build -t qidang/project1:storage storage/
docker build -t qidang/project1:auth auth/
docker network create -d bridge project1
docker-compose up