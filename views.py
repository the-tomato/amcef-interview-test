from flask import current_app, g
from database import db, Post


# GET /posts/{postId}
def get_post(postId):
    # Try to get the post locally
    db.init_app(current_app)
    post = Post.query.filter_by(id=postId).first()

    if post is None:
        # Try to get the post externally
        response = current_app.ms.requests.get(f"https://jsonplaceholder.typicode.com/posts/{postId}")
        if response.status_code != 200:
            return {}, 404
        data = response.json()

        # Save the post locally
        post = Post(
            id=data.get('id'),
            userId=data.get('userId'),
            title=data.get('title'),
            body=data.get('body')
        );
        db.session.add(post)
        db.session.commit()
        
    return post.data()

# GET /posts[?userId={userId}]
def get_posts(userId=None):
    db.init_app(current_app)
    posts = None
    if userId is None:
        posts = Post.query.all()
    else:
        posts = Post.query.filter_by(userId=userId)
    return list(map(lambda post: post.data(), posts))

# DELETE /posts/{postId}
def delete_post(postId):
    # Try to get the post
    db.init_app(current_app)
    post = Post.query.filter_by(id=postId).first()

    # Post not found
    if post is None:
        return {}, 404
        
    # Delete the post
    db.session.delete(post)
    db.session.commit()
    return {}, 200

# PATCH /posts/{postId}
def edit_post(postId, data):
    # Try to get the post
    db.init_app(current_app)
    post = Post.query.filter_by(id=postId).first()

    # Post not found
    if post is None:
        return {}, 404

    # Update the values
    if data.get('title') is not None:
        post.title = data.get('title')
    if data.get('body') is not None:
        post.body = data.get('body')
        
    # Save the post
    db.session.commit()
    return post.data(), 200

# POST /posts?userId={userId}
def create_post(userId, data):
    # Check the userId
    response = current_app.ms.requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    # User ID not found
    if response.status_code != 200:
        return {}, 403

    # Add a new post
    post = Post(
        userId=userId,
        title=data.get('title'),
        body=data.get('body')
    )
    db.init_app(current_app)
    db.session.add(post)
    db.session.commit()
        
    return post.data(), 200
