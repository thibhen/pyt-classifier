
FROM python:3

COPY . /app
WORKDIR /app
EXPOSE 5000

RUN pip install --upgrade pip && \
	pip install textblob nltk && \
	python -m textblob.download_corpora lite 
	
RUN chmod +x /app/server.py
CMD [ "./server.py" ]
