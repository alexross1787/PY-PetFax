from flask import ( Blueprint, render_template, request, redirect) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')

@bp.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')
        
    return render_template('facts/index.html') #this should be indented at the same place as the if statement