from app import create_app,db
from flask_script import Manager,Server
from app.models import User, Comment,Blog
from  flask_migrate import Migrate, MigrateCommand

#creating an app instance  
app = create_app('development')  


manage = Manager(app)
manage.add_command('server',Server)

# manager.add_command('server',Server)

migrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)

@manage.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, blog = blog, Comment = Comment ) 

if __name__ == '__main__':
    manage.run()
