from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

key = "f8a479ff06b7be92d7bd9d6644a35e82"
token = "4aa46c18e2349cba537fa7169eb9a7733aa16917a12b69d86f44758d8c3faeb2"
url = "https://api.trello.com/1/"

@app.route('/tasks')
def list_tasks():
    items = session.get_items()
    return render_template("index.html", items=items)

@app.route('/tasks', methods=['POST'])
def post_item():
    
    form = request.form
    complete = False
    remove = False
    id = 0

    for key in form:
        print(key)
        if key.startswith('Done_'):
            complete = True
            id = key.partition('_')[-1]
            
        if key.startswith('Remove_'):
            remove = True
            id = key.partition('_')[-1]
            
    if "addtask" in form:
         tasktitle = request.form['addtask']
         if(tasktitle != ''):
            session.add_item(tasktitle)
         items = session.get_items()

    if complete:
        print("Raj Done " + str(id))
        print(id)
        items = session.get_items()

    if remove:  
        print("Raj Remove " + str(id))
        session.remove_item(id)
        items = session.get_items()

    else:
        items = session.get_items()
    
    

    return render_template("index.html", items=items)
    #return render_template("index.html")

@app.route('/tasks/<id>', methods=['GET'])
def get_item(id):
    singleitem = session.get_item(id)
    print(singleitem)
    return render_template("index.html", singleitem=singleitem)



if __name__ == '__main__':
    app.run()

