from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = False


'''
#make the format for test table
class Test(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        msg = db.Column(db.String(80))

        def __init__(self, id, msg):
            self.id= id
            self.msg = msg

        def __repr__(self):
            return '<Test id: {0}, msg: {1}>'.format(self.id, self.msg)
'''

#main site. entering ip will lead to this page
@app.route("/")
def home():
    return render_template("main.html")



if __name__ == "__main__": #when runpy
    #db.create_all()
    app.run(host = '0.0.0.0')

