from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
username = "root"
password = "3yGWpZ7jeS"
client = MongoClient(f'mongodb://{username}:{password}@34.78.116.136:27017/')
# client = MongoClient('mongodb://mongodb.db.svc.cluster.local:27017/') 
db = client['guy_data']
links_collection = db['guy_data']

# Define a custom filter to zip lists in the templateefaddav
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
