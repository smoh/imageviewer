from astropy.table import Table

from flask import Flask, render_template, request

app = Flask(__name__)

IMGDIR="http://www.astro.princeton.edu/~semyeong/images/"
table = Table.read('s.fits')

@app.route('/')
def hello_world():
    return 'Index'

@app.route('/<int:ind>/')
def image_view(ind=None):
    return render_template(
            'imageview.html', ind=ind, IMGDIR=IMGDIR, iauname=table['IAUNAME'][ind])
    

if __name__ == '__main__':
    app.run(debug=True)
