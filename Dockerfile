FROM python:2.7
ADD bank.py /
ADD node2.py /

EXPOSE 8002
CMD [ "python", "./node2.py" ]