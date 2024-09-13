from flask import  flash
from flask_login import login_user, logout_user
from forms import LoginForm, RegisterForm
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from models import db, User, Task
from forms import TaskForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email address already in use.', 'danger')
            return redirect(url_for('main.register'))

        username = form.username.data
        password = form.password.data
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('register.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter(Task.users.any(id=current_user.id)).all()
    return render_template('dashboard.html', tasks=tasks)


@main.route('/create_task', methods=['GET', 'POST'])
@login_required
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            status=form.status.data
        )

        selected_user_ids = form.users.data or []
        task.users = User.query.filter(User.id.in_(selected_user_ids)).all()
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    all_users = User.query.all()
    return render_template('create_task.html', form=form, all_users=all_users)



@main.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)
    form.users.data = [user.id for user in task.users]

    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.status = form.status.data
        task.users = []
        for user_id in form.users.data:
            user = User.query.get(user_id)
            if user:
                task.users.append(user)

        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('edit_task.html', form=form, task=task)

@main.route('/delete_task/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.dashboard'))
