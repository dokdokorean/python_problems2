from flask import Flask
app=Flask(__name__)
@app.route('/user/<userName>')
def get_uriName(userName):
    return"userName"+userName
if __name__=='__main__':
    app.run()
