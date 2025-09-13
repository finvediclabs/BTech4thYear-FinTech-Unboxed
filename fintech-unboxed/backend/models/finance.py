from flask import MongoEngine

db = MongoEngine()

class Income(db.Document):
    amount = db.FloatField(required=True)
    source = db.StringField(required=True)
    date = db.DateTimeField(required=True)

    def create_income(self, amount, source, date):
        self.amount = amount
        self.source = source
        self.date = date
        self.save()

    @classmethod
    def get_all_incomes(cls):
        return cls.objects()

    def update_income(self, amount=None, source=None, date=None):
        if amount is not None:
            self.amount = amount
        if source is not None:
            self.source = source
        if date is not None:
            self.date = date
        self.save()

    def delete_income(self):
        self.delete()


class Expense(db.Document):
    amount = db.FloatField(required=True)
    category = db.StringField(required=True)
    date = db.DateTimeField(required=True)

    def create_expense(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date
        self.save()

    @classmethod
    def get_all_expenses(cls):
        return cls.objects()

    def update_expense(self, amount=None, category=None, date=None):
        if amount is not None:
            self.amount = amount
        if category is not None:
            self.category = category
        if date is not None:
            self.date = date
        self.save()

    def delete_expense(self):
        self.delete()


class Goal(db.Document):
    target_amount = db.FloatField(required=True)
    description = db.StringField(required=True)
    deadline = db.DateTimeField(required=True)

    def create_goal(self, target_amount, description, deadline):
        self.target_amount = target_amount
        self.description = description
        self.deadline = deadline
        self.save()

    @classmethod
    def get_all_goals(cls):
        return cls.objects()

    def update_goal(self, target_amount=None, description=None, deadline=None):
        if target_amount is not None:
            self.target_amount = target_amount
        if description is not None:
            self.description = description
        if deadline is not None:
            self.deadline = deadline
        self.save()

    def delete_goal(self):
        self.delete()