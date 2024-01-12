# initializes your image with a basic Linux environment plus the latest version of Python
FROM python

# creates a new directory at /service to contain your microservice code
RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY recommendations/ /service/recommendations/

# gives Docker a WORKDIR /service/recommendations instruction, which is kind of like doing a cd inside the image.
# Any paths you give to Docker will be relative to this location, and when you run a command, it will be run in this directory.
WORKDIR /service/recommendations
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN python3 -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto
RUN python3 -m unittest -v
# tells Docker that you’re going to run a microservice on port 50051, and you want to expose this outside the image.
# once you create a network for your services, there no need to expose this port
#EXPOSE 50051

# tells Docker how to run your microservice.
ENTRYPOINT ["python3", "run.py"]