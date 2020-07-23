from app import create_app, db
from app.models import *
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask import render_template

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


# @app.errorhandler(404)
# def page_not_found(error):
#     """
#     404
#     """
#     return render_template("home/404.html"), 404


if __name__ == '__main__':
    manager.run()

'''

python manage.py db init # 创建迁移仓库，首次使用
python manage.py db migrate # 创建迁移脚本
python manage.py db upgrade # 把迁移应用到数据库中

python manage.py runserver

'''