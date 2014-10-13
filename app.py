from astropy.table import Table

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

IMGDIR="http://www.astro.princeton.edu/~semyeong/projects/ETGOutskirts/test2/fig/image/"
table = Table.read('s.fits')

@app.route('/')
def hello_world():
    return 'Index'

@app.route('/<int:ind>/')
def image_view(ind=None):
    return render_template(
            'imageview.html', ind=ind, IMGDIR=IMGDIR, iauname=table['IAUNAME'][ind])

@app.route('/goto', methods=['POST', 'GET'])    
def goto():
    # error = None
    # if request.method == 'POST':
    return redirect('/' + request.form['index'])

if __name__ == '__main__':
    app.run(debug=True)
