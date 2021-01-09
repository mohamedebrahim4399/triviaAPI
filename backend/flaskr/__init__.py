import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]
    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # Set up CORS

    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization, true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, PUT, POST, DELETE, OPTIONS')
        return response

    # Create an categories requests

    @app.route('/categories')
    def return_categories():
        categories = {}
        for category in Category.query.order_by(Category.id).all():
            categories.update({category.id: category.type})
        return jsonify({
            'success': True,
            'categories': categories,
            'total_categoreis': len(Category.query.all())
        })

    # GET requests for questions

    @app.route('/questions')
    def return_questions():
        selections = Question.query.order_by(Question.id).all()
        total_questions = len(Question.query.all())
        current_question = paginate_questions(request, selections)
        current_category = [
            current_question[x]['category'] for x in range(len(current_question))]
        if len(current_question) == 0:
            abort(404)
        categories = {}
        for category in Category.query.order_by(Category.id).all():
            categories.update({category.id: category.type})
        return jsonify({
            'success': True,
            'questions': current_question,
            'total_questions': total_questions,
            'current_category': current_category,
            'categories': categories
        })

    # DELETE question

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_questions(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()
            question.delete()
            return jsonify({
                'success': True,
                'deleted': question_id,

            })
        except:
            abort(404)

    # Create new question,

    @app.route('/questions', methods=['POST'])
    def crate_questions():
        body = request.get_json()
        new_question = body.get('question')
        new_answer = body.get('answer')
        new_category = body.get('category')
        new_difficulty = body.get('difficulty')
        if (new_question or new_answer or new_category or new_difficulty) is None:
            abort(404)
        try:
            question = Question(question=new_question, answer=new_answer, category=new_category,
                                difficulty=new_difficulty)
            question.insert()
            total_questions = len(Question.query.all())
            current_questions = question.format()
            return jsonify({
                'success': True,
                'created': question.id,
                'current_questions': current_questions,
                'total_questions': total_questions

            })
        except:
            abort(422)

    # search questions

    @app.route('/questions/search', methods=['POST'])
    def questions_search():
        body = request.get_json()
        search_term = body.get('searchTerm')
        selections = Question.query.filter(
            Question.question.ilike(f'%{search_term}%')).all()
        if len(selections) == 0 or search_term == '':
            abort(404)
        current_questions = paginate_questions(request, selections)
        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
        })

    # questions based on category.

    @app.route('/categories/<int:category_id>/questions')
    def categories_questions(category_id):
        try:
            questions = Question.query.filter(Question.category == category_id).all()
            current_questions = [question.format() for question in questions]
            if len(questions) == 0:
                abort(404)
            return jsonify({
                'success': True,
                'category': category_id,
                'questions': current_questions,
                'total_categories_questions': len(current_questions),
            })

        except:
            abort(404)

    @app.route('/quizzes', methods=['POST'])
    def quizzes():

        body = request.get_json()

        category = body.get('quiz_category')
        previous = body.get('previous_questions')
        print('########################################')
        print(category,previous)

        current_question = None

        if category == {}:
            abort(404)

        if (category['id'] == 0):
            questions = Question.query.all()
        else:
            questions = Question.query.filter_by(category=category['id']).all()

        while len(previous) < len(questions):

            rand_num = random.randint(0, len(questions) - 1)

            random_question = questions[rand_num].format()

            if not (random_question['id'] in previous):
                current_question = random_question
                break

        return jsonify({
            'success': True,
            'question': current_question
        })

    # error handlers

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

        @app.errorhandler(422)
        def unprocessable(error):
            return jsonify({
                'success': False,
                'error': 422,
                'message': 'unprocessable'
            }), 422

    return app
