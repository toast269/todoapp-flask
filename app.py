from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = "ThisIsAVerySecretKey"

db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title} \n"
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(155), unique=True, nullable=False)
    passwd = db.Column(db.String(155), nullable=False)
    notes = db.relationship('Todo')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        return render_template('/')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    render_template('register.html')
    if request.method == "POST":
        email = str(request.form.get('email-id'))
        username = str(request.form.get('username'))
        passwd_set = str(request.form.get('password'))
        passwd_confirm = request.form.get('confirm-password')

        if len(email) < 4 and ["@", ".com"] not in email:
            flash("Invalid Email", category='error')
        if len(username) < 3:
            flash("Username cannot be less than 3 characters", category='error')
        if len(passwd_set) < 8:
            flash("Password cannot be leass than 8 characters", category='error')
        if passwd_set != passwd_confirm:
            flash("Passwords don't match", category='error')
        else:
            new_user = User(username=username, passwd=generate_password_hash(passwd_set, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created Successfully", category='success')
            return redirect('/login')

    return render_template('register.html')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method=="POST":
        todo = Todo(title=request.form['title'], desc=request.form['desc'])
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if request.method=="POST":
        todo.title=request.form['title']
        todo.desc=request.form['desc']
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('update.html', todo=todo)

if __name__ == "__main__":
    app.run(debug=True)