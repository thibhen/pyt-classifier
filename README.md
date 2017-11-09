

This is a sample demo presenting test classification exposed as WebService (powered by Python and Flask)


Inspired from https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
Pre-requisites :
pip install textblob
flask/bin/pip install textblob
python -m textblob.download_corpora

Test Command :
curl http://localhost:5000/api/classify?message=hello
curl -H "Content-Type: application/json" -X POST -d '{"message":"hello","tag":"Home"}' "http://localhost:5000/api/update"
