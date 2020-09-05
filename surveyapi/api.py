"""
api.py
- provides the API endpoints for consuming and producing 
  REST requests and responses
"""

from flask import Blueprint, request
from .models import db, Survey, Question, Choice

api = Blueprint('api', __name__)

@api.route('/surveys/')
def surveys():
  surveys = Survey.query.all()
  return { 'surveys': [s.to_dict() for s in surveys] }

@api.route('/surveys/<int:id>/')
def survey(id):
  survey = Survey.query.get(id)
  return { 'survey': survey.to_dict() }