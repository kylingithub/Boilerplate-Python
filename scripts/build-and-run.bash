export repo_name="project_name"

docker build \
-t ${repo_name}:local \
-f ./Dockerfile .

docker run --rm --env-file ./config/.env.template --net host ${repo_name}:local