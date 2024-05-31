from pathlib import Path

from flask_sqlalchemy import SQLAlchemy

from yacut import app, db

BASE_DIR = Path(__file__).resolve(strict=True).parent
print(BASE_DIR)

tmp_path = BASE_DIR / 'tmp/'
db_path = tmp_path / 'test_db.sqlite3'
db_uri = 'sqlite:///' + str(db_path)
app.config.update({
    'TESTING': True,
    'SQLALCHEMY_DATABASE_URI': db_uri,
    'WTF_CSRF_ENABLED': False,
})
print(app.config['SQLALCHEMY_DATABASE_URI'])
with app.app_context():
    db.engine.echo = True
    db.create_all()
    print(db.engine.url.database)
#     db.drop_all()
#     db.session.close()
#     db_path.unlink()
