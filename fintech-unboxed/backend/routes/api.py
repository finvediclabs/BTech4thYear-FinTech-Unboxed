from flask import Blueprint, request, jsonify
from ..models.finance import Income, Expense, Goal

api = Blueprint('api', __name__)

@api.route('/income', methods=['GET', 'POST'])
def handle_income():
    if request.method == 'POST':
        data = request.json
        income = Income(**data)
        income.save()
        return jsonify(income.to_dict()), 201
    else:
        incomes = Income.get_all()
        return jsonify([income.to_dict() for income in incomes]), 200

@api.route('/expenses', methods=['GET', 'POST'])
def handle_expenses():
    if request.method == 'POST':
        data = request.json
        expense = Expense(**data)
        expense.save()
        return jsonify(expense.to_dict()), 201
    else:
        expenses = Expense.get_all()
        return jsonify([expense.to_dict() for expense in expenses]), 200

@api.route('/goals', methods=['GET', 'POST'])
def handle_goals():
    if request.method == 'POST':
        data = request.json
        goal = Goal(**data)
        goal.save()
        return jsonify(goal.to_dict()), 201
    else:
        goals = Goal.get_all()
        return jsonify([goal.to_dict() for goal in goals]), 200

@api.route('/income/<id>', methods=['PUT', 'DELETE'])
def modify_income(id):
    if request.method == 'PUT':
        data = request.json
        income = Income.update(id, **data)
        return jsonify(income.to_dict()), 200
    else:
        Income.delete(id)
        return jsonify({'message': 'Income deleted'}), 204

@api.route('/expenses/<id>', methods=['PUT', 'DELETE'])
def modify_expense(id):
    if request.method == 'PUT':
        data = request.json
        expense = Expense.update(id, **data)
        return jsonify(expense.to_dict()), 200
    else:
        Expense.delete(id)
        return jsonify({'message': 'Expense deleted'}), 204

@api.route('/goals/<id>', methods=['PUT', 'DELETE'])
def modify_goal(id):
    if request.method == 'PUT':
        data = request.json
        goal = Goal.update(id, **data)
        return jsonify(goal.to_dict()), 200
    else:
        Goal.delete(id)
        return jsonify({'message': 'Goal deleted'}), 204