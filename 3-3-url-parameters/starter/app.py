from flask import Flask

app = Flask(__name__)

posts = {
    1: {'title': 'Introduction to Flask', 'content': 'Flask is a lightweight WSGI web application framework...'},
    2: {'title': 'Understanding Routes in Flask', 'content': 'Routes are a fundamental concept in Flask...'}
}

@app.route('/')
def home():
    return '<h1>Welcome to My Blog</h1><p>Click on the posts to learn more about Flask.</p>'

@app.route('/post/<int:post_id>') # dynamic route to capture post_id from the URL
def show_post(post_id):
    post = posts.get(post_id) # retrieve the post based on the post_id from the URL
    if not post:
        return '<h1>404: Post not found</h1>', # if post does not exist return a 404 error message
    return f"<h1>{post['title']}</h1><p>{post['content']}</p>" # if post exists dynamically display an 
                                                                # HTML page with the post title and content

if __name__ == '__main__':
    app.run(debug=True)
