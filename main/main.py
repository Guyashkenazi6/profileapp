from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongodb:27017/') # Replace with your MongoDB URI
db = client['data']
links_collection = db['data']

# Define a custom filter to zip lists in the template
@app.template_filter('zip_lists')
def zip_lists(a, b):
    return zip(a, b)

@app.route('/')
def index():
    # Retrieve links from MongoDB
    links = links_collection.find_one()['links']
    
    # Define labels for the links
    labels = ['LinkedIn', 'GitHub', 'GitLab']

    return render_template('links.html', links=links, labels=labels)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
