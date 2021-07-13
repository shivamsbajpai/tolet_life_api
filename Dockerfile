FROM python:3.8


ENV PORT 8000


# set working directory
WORKDIR /usr/src/toletlife
COPY . /usr/src/toletlife


RUN pip install -r ./requirements.txt
EXPOSE ${PORT}


CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]