# Description

This is a coding excercise microservice that exposes an API for managing posts in a local database.

# Installation

1. Download this repo
```
git clone git@github.com:the-tomato/amcef-interview-test.git
```

2. Install the dependencies
```
pip install flask py-ms[all] flask_sqlalchemy openapi-spec-validator werkzeug==2.0.0
```

3. Run
```
python3 main.py
```

# Usage

### Fetching posts
A single post
```
GET /posts/{postId}
```

All posts
```
GET /posts
```

Posts by userId
```
GET /posts?userId={userId}
```


### Removing posts:
```
DELETE /posts/{postId}
```

### Adding posts:
```
POST /posts?userId={userId}
```
with a request body
```
{
  "title": {title},
  "body": {body}
}
```

### Editing posts:
```
PATCH /posts/{postId}
```
with a request body
```
{
  "title": {title},
  "body": {body}
}
```
