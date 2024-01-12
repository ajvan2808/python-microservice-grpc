FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY marketplace/ /service/marketplace/
WORKDIR /service/marketplace

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN python3 -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto
RUN 2to3 ./*pb2*.py -w -n

EXPOSE 5000
ENV FLASK_APP=marketplace.py
# Flask will only accept connections from localhost (localhost inside the container is different from localhost outside, even on the same machine)
# this tell Flask to accept connections from anywhere
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]