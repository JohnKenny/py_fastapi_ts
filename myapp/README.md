# sending a get request
curl http://127.0.0.1:5050/hello-world 

curl -X POST http://127.0.0.1:5050/hello-world-post
# running the app
uvicorn main:app --port 5050 --reload

# sending post request
curl -X POST "http://127.0.0.1:5050//submit-score" -H "Content-Type: application/json" -d 
'{
    "name": "John",
    "math_score": 66,
    "english_score": 79

}'
    

