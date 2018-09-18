# Deployment

### Requirements:
- python 3.6

### Installation
- Create Virtual Environment
```
python -m venv venv
```
- Activate it
```
source venv/bin/activate
```
- Install dependencies
```
pip install -r requirements.txt
```

### Locally
- Run the server
```
python api/app.py
```
- Send a request
```
curl -X POST -H "Content-Type: application/json" -d '{"data": [[1.1, 2.4]]}' http://localhost:5000/
```


### Deployment
- First time
```
zappa deploy dev
```

- Updates
```
zappa update dev
```
