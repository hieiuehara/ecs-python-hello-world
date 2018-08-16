# ecs-python-hello-world

## Send our container up to AWS
`docker build -t uehara/hello-world .` build your image

`aws ecr create-repository --region "region" --repository-name "teste"` create your Elastic Container Registry

`aws ecr get-login --region "region" --no-include-email` get docker url login

`docker login -u AWS -p "url"` run this command on terminal

`docker tag "image name":"version" "repositoryUrl"` tagging the image

`docker push "repositoryUrl"` pushing the image up to AWS ECR
