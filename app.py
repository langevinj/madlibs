from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story
app = Flask(__name__)

story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )

story2 = Story(
    ["noun", "verb", "place", "plural_noun"],
    """I used to care a lot about my {noun}, but since I {verb}
       to {place}. I stopped worrying about all the {plural_noun}."""
    )

story3 = Story(
    ["place", "adjective", "noun"],
    """It all seemed so easier back in {place}. The only thing I cared about was my {adjective} {noun}."""
    )

all_stories = {"story1" : story1, "story2" : story2, "story3": story3}


@app.route('/')
def home_page():
    """Shows home page"""
    
    return render_template('home.html', prompts=story.prompts)

@app.route('/fillin')
def fillin_page():
    """Shows page in which responses are filled in"""
    chosen_story = request.args['stories']
    selected = all_stories[chosen_story]
    return render_template('fillin.html', prompts=selected.prompts, story_choice=chosen_story)

@app.route('/story')
def story_page():
    """Shows filled in MadLib"""
    answers = {}
    chosenstory = request.args['chosenstory']
    selected = all_stories[chosenstory]
    print(selected.prompts)
    for prompt in selected.prompts:
        answers[prompt] = request.args[prompt]  
    my_story = selected.generate(answers)
    return render_template('story.html', your_story=my_story)
