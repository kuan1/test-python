from flask import Flask,url_for,request,render_template,redirect
import os

app = Flask(__name__)

@app.route("/")
def index():
    data = [
        {
          "url": url_for('index'),
          "name": "首页"
        },
        {
          "url": url_for('detail', id=1),
          "name": "详情1"
        },
        {
          "url": url_for('detail', id=2),
          "name": "详情2"
        },
        {
          "url": url_for('api_test'),
          "name": "api/test"
        },
        {
          "url": url_for('static', filename="test.html"),
          "name": "test.html"
        },
        {
          "url": url_for('about'),
          "name": "关于"
        },
    ]
    return render_template('home.html',data=data)

@app.route("/about")
def about():
    return "<p>Hello, About You!</p>"

@app.route("/detail/<int:id>")
def detail(id):
    return f"<p>detail: {id}</p>"

@app.route('/api/test', methods=["GET", "POST"])
def api_test():
    return {"data": {"name": "kuan"}, "success": True} if request.method == 'GET' else {'data': 'post', "success": True}

@app.errorhandler(404)
def page_not_found(error):
  return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)