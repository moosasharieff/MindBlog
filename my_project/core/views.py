# my_project/core/views.py

from flask import render_template, redirect, url_for, Blueprint
from my_project.core.forms import BlogForm
import boto3

###################################################
######### SETTING UP AWS DYNAMO DB (BOTO3) ########
###################################################

db = boto3.resource('dynamodb', region_name='us-east-1')
table = db.Table('MindBlog_Table')
print(f"Table Name: {table._name} has been initiated")


###################################################
######### SETTING UP VIEWS ########
###################################################

core = Blueprint('core', __name__)

@core.route('/', methods=['GET', 'POST'])
def home():

    response = table.scan()
    items = response['Items']

    return render_template('home.html', items=items)



@core.route('/addBlog', methods=['GET', 'POST'])
def addblog():

    form = BlogForm()

    if form.validate_on_submit():

        table.put_item(
            Item={
                'username': form.username.data,
                'title': form.title.data,
                'text': form.text.data
            }
        )

        return redirect(url_for('core.home'))

    return render_template('addblog.html', form=form)

