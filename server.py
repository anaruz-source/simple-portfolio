from flask import Flask, render_template, request, redirect

app =  Flask(__name__)

@app.route('/')
def index(): # index.html resides in templates file
	return render_template('index.html')


@app.route('/<string:page_name>')
def page(page_name): # <page-name>.html resides in templates file
	return render_template(page_name+'.html')

@app.route('/send', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou')
    else:
        return 'something went wrong, come back later'