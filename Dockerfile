FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update \ 
 && apk add postgresql-dev \ 
            gcc \ 
            python3-dev \ 
            musl-dev \ 
            postgresql-client \
            # Pillow dependencies
            jpeg-dev \
            zlib-dev \
            freetype-dev \
            lcms2-dev \
            openjpeg-dev \
            tiff-dev \
            tk-dev \
            tcl-dev \
            harfbuzz-dev \
            fribidi-dev \
 && mkdir /code

WORKDIR /code

COPY src/requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY src/ /code/

RUN adduser -D dctalbot
USER dctalbot

CMD ./entrypoint.sh
