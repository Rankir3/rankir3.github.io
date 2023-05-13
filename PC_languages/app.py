from flask import Flask, render_template
from data import languages_list as data
app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        template_name_or_list='index.html',
        title='Programming languages',
        title_1='PowerCode-Academy',
        data=data
    )


@app.route("/lang/<int:pk>")
def language_detail(pk):
    for item in data:
        if item.get('id') == pk:
            object = item
            break
    return render_template(
        template_name_or_list='language.html',
        object=object,
    )



if __name__ == '__main__':
    app.run(debug=True)









