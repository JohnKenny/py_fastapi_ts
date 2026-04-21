
curl http://127.0.0.1:5050/hello-world 

curl -X POST http://127.0.0.1:5050/hello-world-post

uvicorn main:app --port 5050 --reload