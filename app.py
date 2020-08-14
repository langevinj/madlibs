from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story
app = Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )


@app.route('/')
def home_page():
    """Shows home page"""
    
    return render_template('home.html', prompts=story.prompts)

@app.route('/story')
def story_page():
    """Shows filled in MadLib"""
    answers = {}
    for prompt in story.prompts:
        answers[prompt] = request.args[prompt]  
    my_story = story.generate(answers)
    return render_template('story.html', your_story=my_story)
