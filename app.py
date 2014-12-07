from flask import Flask, render_template, request, redirect
import requests
import csv
from pager import Pager

app = Flask(__name__)

def read_table(url):
    """Return a list of dict"""
    r = requests.get(url)
    lines = r.text.splitlines()
    return [row for row in csv.DictReader(lines)]

BASEURL = 'http://www.astro.princeton.edu/~semyeong/etgpublic'
TABLEURL = BASEURL+'/db.csv'
imgdir = BASEURL+'/image/'
profdir = BASEURL+'/profile/'


@app.route('/')
def index():
    return redirect('/0')

@app.route('/<int:ind>/')
def image_view(ind=None):
    d = read_table(TABLEURL)
    pager = Pager(len(d))
    if ind >= pager.count:
        return "invalid index", 404
    else:
        pager.current = ind
        return render_template(
                'imageview.html',
                ind=ind,
                imgdir=imgdir,
                profdir=profdir,
                pager=pager, **d[ind])

@app.route('/goto', methods=['POST', 'GET'])    
def goto():
    # error = None
    # if request.method == 'POST':
    return redirect('/' + request.form['index'])

if __name__ == '__main__':
    app.run(debug=True)
