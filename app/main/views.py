from flask import render_template, request, redirect, url_for, abort
from . import main  
from .forms import CommentsForm, UpdateProfile, BlogForm, LikeForm
from ..models import Comment, Blog, User 
from flask_login import login_required, current_user
from .. import db,photos

import markdown2



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best bloging Website Online'

    search_blog = request.args.get('blog_query')
    blog= Blog.get_all_blogs()  


    return render_template('index.html', title = title ,blog=blog)


@main.route('/blog/<int:blog_id>')
def blog(blog_id):

    '''
    View blog page function that returns the blog details page and its data
    '''
    found_blog= get_blog(blog_id)
    title = blog_id
    blog_comments = Comment.get_comments(blog_id)

    return render_template('blog.html',title= title ,found_blog= found_blog, blog_comments= blog_comments)

@main.route('/search/<blog_name>')
def search(blog_name):
    '''
    View function to display the search results
    '''
    searched_blogs = search_blog(blog_name)
    title = f'search results for {blog_name}'

    return render_template('search.html',blogs = searched_blogs)

@main.route('/blog/new/', methods = ['GET','POST'])
@login_required
def new_blog():
    '''
    Function that creates new blogs
    '''
    form = BlogForm()


    if User is None:
        abort( 404 )

    if form.validate_on_submit():
        blog= form.content.data
        user_id = form.user_id.data
        new_blog= blog(blog= blog, user_id= user_id)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', new_blog_form= form, User= User)


@main.route('/blog/comments/new/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
    vote_form = LikeForm()
    if form.validate_on_submit():
        new_comment = Comment(blog_id =id,comment=form.comment.data,username=current_user.username,votes=form.vote.data)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    title = f'{blog_result.id} review'
    return render_template('new_comment.html',comment_form=form, vote_form= vote_form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    
    return render_template('profile/update.html',form =form)

@main.route('/view/comments/<int:id>')
def view_comments(id):
    '''
    Function that returs  the comments belonging to a particular blog
    '''
    comments = Comment.get_comments(id)
    return render_template('view_comments.html',comments = comments, id=id)



@main.route('/test/<int:id>')  
def test(id):
    '''
    this is route for basic testing
    '''
    blog =Blog.query.filter_by(id=1).first()
    return render_template('test.html',blog= blog)


    return render_template('new_blog.html', new_blog_form= form, user= user)
