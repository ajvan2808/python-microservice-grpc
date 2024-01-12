<h1 align="center"> Online Books For You Website </h1>
<div align="center">
	<code><img width="30" src="https://user-images.githubusercontent.com/25181517/192107855-e669c777-9172-49c5-b7e0-404e29df0fee.png" alt="gRPC" title="gRPC"/></code>
	<code><img width="30" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/></code>
	<code><img width="30" src="https://user-images.githubusercontent.com/25181517/117207330-263ba280-adf4-11eb-9b97-0ac5b40bc3be.png" alt="Docker" title="Docker"/></code>
	<code><img width="30" src="https://user-images.githubusercontent.com/25181517/183896132-54262f2e-6d98-41e3-8888-e40ab5a17326.png" alt="AWS" title="AWS"/></code>
</div>

<p align="center">✨ A website implementing Python microservice with gRPC, Docker, Kubernetes ✨</p>
<hr>

📌 **Marketplace** will be a very minimal web app that displays a list of books to the user. \
📌 **Recommendations** will be a microservice that provides a list of books in which the user may be interested. \
📌 API development follow gRPC framework, applying protocol buffer over REST API \
📌 Both microservices are in this repo, however they are isolated \
📌 Each services has their own Docker image, both locally and available on Docker Hub \


## Production Ready
Using Docker, Kubernetes, AWS EKS, ECR, EC2 instances
### Local
* The application deployed locally with Docker Desktop, and Kubernetes
* Pulling images from Docker Hub
* Deploying to Kubernetes cluster locally provided by Docker
* The `kubernetes.yaml` used for local deployment purpose

### Cloud Provider (AWS)
_(This later deleted from AWS account to stop costing)_
* Docker images are pushed to AWS' ECR under repositories `recommendations` and `marketplace`
* Kubernetes cluster: EKS
* Nodes are EC2 instances
* LoadBalancer Service used for `marketplace` to be accessible from outside