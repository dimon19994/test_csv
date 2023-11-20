from datetime import datetime

from dateutil.relativedelta import relativedelta
from flask import Response, render_template
from flask_paginate import Pagination

from controllers import _Controller

from models import db
from models.tables import Data


FILTERS = ["category", "gender", "birth_date", "age", "age_range"]
PER_PAGE = 20


class BaseData(_Controller):
    def _filter_data(self):
        conditions = True

        for k, f in self.request.args.items():
            if k == "category":
                conditions &= Data.category == f
            if k == "gender":
                conditions &= Data.gender == f
            if k == "age":
                start_date, end_date = self.get_date_range(f)
                conditions &= Data.birth_date.between(start_date, end_date)
            if k == "age_range":
                start_date, end_date = self.get_date_range(f.split("-")[1], 5)
                conditions &= Data.birth_date.between(start_date, end_date)
            if k == "birth_date":
                conditions &= Data.birth_date == datetime.strptime(f, "%Y-%m-%d")

        return conditions

    def get_date_range(self, age, yeats=1):
        delta = int(age)
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        start_date = today - relativedelta(years=delta)
        end_date = today - relativedelta(years=delta - yeats, microseconds=1)

        return start_date, end_date

    def _get_query(self):
        where_conditions = self._filter_data()
        data = list(Data.select().where(where_conditions).order_by(Data.id))

        return data


class ViewData(BaseData):
    def _get(self, page):
        select_filters = self._get_select_filters()

        data = self._get_query()

        pagination = Pagination(
            page=page,
            per_page=PER_PAGE,
            total=len(data),
            css_framework="bootstrap5",
        )

        return render_template(
            "view_data.html",
            data=data[PER_PAGE * (page - 1) : PER_PAGE * page],
            select_filters=select_filters,
            headers=FILTERS,
            pagination=pagination,
            selected=dict(self.request.args),
        )

    def _get_select_filters(self):
        filters = {
            "category": [
                c.category
                for c in Data.select(Data.category).order_by(Data.category).distinct()
            ],
            "gender": [
                d.gender
                for d in Data.select(Data.gender).order_by(Data.gender).distinct()
            ],
            "age": list(map(str, range(101))),
            "age_range": [f"{a}-{a + 4}" for a in range(0, 101, 5)],
        }

        return filters


class LoadData(_Controller):
    def _get(self):
        with open("dataset.txt") as file:
            text = file.read()
            data = [row.split(",") for row in text.split("\n") if row != ""][1:]
            for i in range(0, len(data), 200):
                with db.atomic():
                    Data.insert_many(data[i : i + 200]).execute()

        return "Data inserted"


class SaveData(BaseData):
    def _get(self):
        data = self._get_query()

        rows = "category,firstname,lastname,email,gender,birthDate"

        for r in data:
            rows += f"\n{r.category},{r.first_name},{r.last_name},{r.email},{r.gender},{r.birth_date}"

        return Response(
            rows,
            mimetype="text/csv",
            headers={"Content-disposition": "attachment; filename=filtered_data.csv"},
        )
