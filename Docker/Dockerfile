FROM ubuntu:18.04
# Dependencies Install
RUN apt-get update  && \
	apt-get -y install curl && \
	apt-get install -qy python3 && \
	apt-get install -qy python3-pip && \
	apt-get install -qy vim && \
	apt-get -y install git

WORKDIR /Docker
ADD . /workspace
WORKDIR /workspace

# Clone git repo
RUN git clone https://github.com/Laarogue/BigDataHadoop.git

RUN pip3 freeze > requirements.txt && \
	pip3 install -r requirements.txt && \
	pip3 install jupyter

# Expose 8000 Port
EXPOSE 8888

# Go to workspace
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]