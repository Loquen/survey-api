"""
api.py
- provides the API endpoints for consuming and producing 
  REST requests and responses
"""

from flask import Blueprint, request
from .models import db, Survey, Question, Choice

api = Blueprint('api', __name__)

@api.route('/surveys/', methods=('GET', 'POST'))
def surveys():
  if request.method == 'GET':
    surveys = Survey.query.all()
    return { 'surveys': [s.to_dict() for s in surveys] }
  elif request.method == 'POST':
    data = request.get_json() # translate incoming JSON to a python dict
    survey = Survey(name=data['name'])
    questions = []
    for q in data['questions']:
      question = Question(text=q['text'])
      question.choices = [Choice(text=c['text']) for c in q['choices']]
      questions.append(question)
    survey.questions = questions
    db.session.add(survey)
    db.session.commit()
    return survey.to_dict(), 201

@api.route('/surveys/<int:id>/')
def survey(id):
  survey = Survey.query.get(id)
  return { 'survey': survey.to_dict() }

