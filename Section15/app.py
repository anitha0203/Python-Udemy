from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
posts = {
    0: {
        'id': 0,
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')
def home():
    return render_template('home.jinja2', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    p = posts.get(post_id)
    if not p:
        return render_template('404.jinja2', mess=f'A post with id {post_id} was not found.')
    return render_template('post.jinja2', post=p)


@app.route('/post/form')
def form():
    return render_template('form.jinja2')


@app.route('/post/create', methods=['POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}
        return redirect(url_for('post', post_id=post_id))
    return render_template('form.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
