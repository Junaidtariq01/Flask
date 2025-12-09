from flask import Flask, render_template
# from Flask_wtf  import FlaskForm

app=Flask(__name__)

# class Register(FlaskForm):
#     name=stringField("name",validators=[DataRequired()])
#     email=stringField("email",validators=[DataRequired() ])

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def login():
    return render_template('dashboard.html')

if __name__== "__main__":
    app.run(debug=True) 