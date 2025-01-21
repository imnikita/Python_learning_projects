from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if not name or not email or not password:
            flash("All fields are required.", "danger")
            return redirect(url_for('register'))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered. Please log in.", "danger")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(
            password=password,
            method='pbkdf2',
            salt_length=8
        )

        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        login_user(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('secrets'))

    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('secrets'))
            else:
                flash('Invalid password. Please try again.', 'danger')
        else:
            flash('No account found with that email address.', 'danger')

    return render_template("login.html")

@app.route('/secrets')
def secrets():
    return render_template("secrets.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")

if __name__ == "__main__":
    app.run(debug=True)
