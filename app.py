from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)




@app.route('/')
def home_form():
    """Create form"""
    return render_template('base.html', list=story.prompts)


@app.route('/madlib')
def populate_lib():
    word_results = []
    # for item in story.prompts:
    #     word_results.append(request.args[item])

    # """" Convert to dictionary """
    # list1 = word_results
    # list2 = story.prompts

    # zip_obj = zip(list2, list1)
    # results = dict(zip_obj)

    # result = story.generate(results)

    result = story.generate(request.args)
    return render_template('madlib.html', text=result)
