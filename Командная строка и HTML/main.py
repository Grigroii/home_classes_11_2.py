from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:uid>')
def page_of_candidate(uid):
    candidate = get_candidate(uid)
    if not candidate:
        return "Кандидат не найден"
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def page_of_name(candidate_name):
    ''' Поиск по совпадению имён'''
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/skill/<skill_name>')
def page_of_skill(skill_name):
    ''' Поиск по навыкам'''
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, skill=skill_name)


app.run()
