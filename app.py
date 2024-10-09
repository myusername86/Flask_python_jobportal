from flask import Flask,render_template,jsonify
app=Flask(__name__)
# creating list of dictionary
JOBS=[
    {
        'id':1,
'title':'web developer',
'location':'Sweden',
        'salary':'Rs.100000'

    },
{
        'id':2,
'title':'web developer',
'location':'Sweden',
    'salary':'Rs.100000'


    },
{
        'id':3,
'title':'web developer',
'location':'Sweden',


    }
]
@app.route("/")
def hello_world():
    #i am passing my dictionary into my home.html
    return render_template('Home.html',jobs=JOBS,company_name="yuva")

@app.route("/api/jobs")
def list_jobs():
   return jsonify(JOBS)
if __name__ == '__main__':
    app.run(debug=True)

