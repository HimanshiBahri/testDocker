FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install net-tools

ENV PASSWORD='password'	
RUN echo 'root:'$PASSWORD | chpasswd	#Setting up a fixed password for root user on Ubuntu

RUN apt-get -y install openssh-server
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo 'export NOTVISIBLE="in users profile"' >> ~/.bashrc
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
ENTRYPOINT service ssh start && bash
