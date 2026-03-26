export tag="version"
export repo_name="project_name"
export registry_host="registry.io"

docker buildx build --platform linux/amd64,linux/arm64 \
-t ${registry_host}/${repo_name}:${tag}  \
-f ./Dockerfile . --push