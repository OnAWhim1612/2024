from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    message = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    markers = Marker.query.all()
    return render_template('index.html', markers=markers)

@app.route('/add_marker', methods=['POST'])
def add_marker():
    lat = float(request.form.get('lat'))
    lng = float(request.form.get('lng'))
    message = request.form.get('message')

    new_marker = Marker(lat=lat, lng=lng, message=message)
    db.session.add(new_marker)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
