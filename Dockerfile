FROM python


# Start and enable SSH
RUN apt-get update \
    && apt-get install -y --no-install-recommends dialog \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd 
COPY sshd_config /etc/ssh/
COPY app.py /opt/
COPY requirements.txt /opt
WORKDIR /opt
RUN pip install -r requirements.txt
EXPOSE 80 2222

CMD ["sh", "-c", "service ssh start && python app.py"]
