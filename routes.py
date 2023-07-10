from flask import redirect, render_template, request, session
from app import app
from models import User, Contact, db


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/home')
    return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect('/home')

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id
        return redirect('/home')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect('/home')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['user_id'] = user.id
            return redirect('/home')
        else:
            return redirect('/login')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('home_visited', None)
    return redirect('/login')


@app.route('/contacts')
def contacts():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = session['user_id']
    contacts = Contact.query.filter_by(user_id=user_id).all()
    return render_template('contacts.html', contacts=contacts)


@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/login')
    user_id = session['user_id']
    user = User.query.get(user_id)
    username = user.username.upper()
    return render_template('home.html', username=username)


@app.route('/contacts/add', methods=['GET', 'POST'])
def add_contact():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        user_id = session['user_id']

        contact = Contact(name=name, email=email, phone_number=phone_number, user_id=user_id)
        db.session.add(contact)
        db.session.commit()

        return redirect('/contacts')

    return render_template('add_contact.html')


@app.route('/contacts/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    if 'user_id' not in session:
        return redirect('/login')

    contact = Contact.query.get(id)

    if contact.user_id != session['user_id']:
        return redirect('/contacts')

    if request.method == 'POST':
        contact.name = request.form['name']
        contact.email = request.form['email']
        contact.phone_number = request.form['phone_number']
        db.session.commit()

        return redirect('/contacts')

    return render_template('edit_contact.html', contact=contact)


@app.route('/contacts/delete/<int:id>', methods=['POST', 'GET'])
def delete_contact(id):
    if 'user_id' not in session:
        return redirect('/login')

    contact = Contact.query.get(id)

    if contact.user_id != session['user_id']:
        return redirect('/contacts')

    db.session.delete(contact)
    db.session.commit()

    return redirect('/contacts')
