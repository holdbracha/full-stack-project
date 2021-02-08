from flask import Flask, render_template, request, redirect, url_for
from db_utils import *



app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def home2():
    return redirect(url_for("home"))

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

# @app.route('/gallery')
# def gallery():
#     halls = get_all_halls()
#     return render_template("blog.html", halls)

@app.route('/gallery')
def gallery_filtered():
    data = request.args
    if not data:
      halls = get_all_halls()
      return render_template("gallery.html", list_halls = halls)
    halls = get_halls_by_filter(data)
    return render_template("gallery.html", list_halls = halls)

@app.route('/gallery-single-post/<hall_id>')
def hall_single_post(hall_id):
    hall = get_hall_by_id(hall_id)
    # hall = get_hall_by_id("5ffec6cfa2673a61f7064e81")
    return render_template("gallery-single-post.html", hall_obj = hall)

@app.route('/hall-single-post2')
def hall_single_post2():
    return render_template("gallery-single-post.html")    

@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.route('/add_place')
def add_place():
  return render_template("add_place.html")

@app.route('/add_place', methods = ['POST'])
def submitt_new_place():
    data = dict(request.form)
    save_hall(data)
    return render_template("index.html")

@app.route('/sending_contact', methods = ['POST'])
def sending_contact():
    data = dict(request.form)
    save_contact(data)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=3000)