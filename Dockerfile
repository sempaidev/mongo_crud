FROM python:3.9

#
ENV WEBAPP_DIR=./code

#RUN mkdir $WEBAPP_DIR
WORKDIR $WEBAPP_DIR
# 
ADD $WEBAPP_DIR/ /code/
RUN pwd
# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pwd
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]