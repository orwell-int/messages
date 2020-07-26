FROM ubuntu:19.10

## for apt to be noninteractive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

ENV ORWELL_DISABLE_TEST_BROADCAST 1

RUN mkdir -p /workdir
WORKDIR /workdir
COPY . /workdir
RUN cd /workdir
RUN ls
RUN pwd

# Install
RUN apt-get -qq update

## preseed and install tzdata
RUN echo "tzdata tzdata/Areas select Europe" > /tmp/preseed.txt; \
	echo "tzdata tzdata/Zones/Europe select Berlin" >> /tmp/preseed.txt; \
	debconf-set-selections /tmp/preseed.txt && \
	rm -f /etc/timezone && \
	rm -f /etc/localtime && \
	apt-get install -y tzdata

RUN apt-get install -y -qq libprotobuf-dev protobuf-compiler
RUN apt-get install -y -qq libzmq3-dev
RUN make test
