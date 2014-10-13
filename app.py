from astropy.table import Table

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

imgdir = "http://www.astro.princeton.edu/~semyeong/projects/ETGOutskirts/test2/fig/image/"
profdir = "http://www.astro.princeton.edu/~semyeong/projects/ETGOutskirts/test2/fig/profile/"
table = Table.read('s.fits')

class Pager(object):
    def __init__(self, count):
        self.count = count
        self.current = 0

    @property
    def next(self):
        n = self.current + 1
        if n > self.count-1:
            n -= self.count
        return n

    @property
    def prev(self):
        n = self.current - 1
        if n < 0 :
            n += self.count
        return n
pager = Pager(len(table))

@app.route('/')
def hello_world():
    return 'Index'

@app.route('/<int:ind>/')
def image_view(ind=None):
    if ind >= len(table):
        return "invalid index"
    else:
        pager.current = ind
        return render_template(
                'imageview.html',
                ind=ind,
                imgdir=imgdir,
                profdir=profdir,
                iauname=table['IAUNAME'][ind],
                subdir=table['SUBDIR'][ind],
                pager=pager)

@app.route('/goto', methods=['POST', 'GET'])    
def goto():
    # error = None
    # if request.method == 'POST':
    return redirect('/' + request.form['index'])

if __name__ == '__main__':
    app.run(debug=True)
