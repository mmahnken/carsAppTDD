from flask import Flask, request, render_template, jsonify
from model import db, connect_to_db, Model, Brand
from sqlalchemy import func

app = Flask(__name__)

COLORS = ["#1f77b4",
            "#aec7e8",
            "#ff7f0e",
            "#ffbb78",
            "#2ca02c",
            "#98df8a",
            "#d62728",
            "#ff9896",
            "#9467bd",
            "#c5b0d5",
            "#8c564b",
            "#c49c94",
            "#e377c2",
            "#f7b6d2",
            "#7f7f7f",
            "#c7c7c7",
            "#bcbd22",
            "#dbdb8d",
            "#17becf",
            "#9edae5"]

@app.route("/")
def show_homepage():
    return render_template("index.html")

@app.route("/cars")
def show_cars_index():
    all_cars = Model.query.all()
    return render_template("cars.html", cars=all_cars)

@app.route("/charts")
def show_charts():
    return render_template("charts.html")

@app.route("/chart-data.json")
def get_chart_data():
    brands_counts = db.session\
                       .query(Model.brand_name, func.count(Model.brand_name))\
                       .group_by(Model.brand_name)\
                       .all() #list of tuples (Brand, Count)

    # Another way to do the above query.
    # counts_list = []
    # all_brands = Brand.query.all()
    # for b in brands:
    #     current_count = Model.query.filter_by(brand_name=b.name).count()
    #     counts_list.append(current_count)

    # Time to make two separate lists, for our chart.js data format.
    labels = []
    data_points = []
    for pair in brands_counts:
        brand_name = pair[0]
        count = int(pair[1])
        labels.append(brand_name)
        data_points.append(count)

    #Alternative for the above for-loop
    # labels = [ pair[0] for pair in brands_counts ]
    # data_points = [ pair[1] for pair in brands_counts ]

    return jsonify({'data_points': data_points, 'labels': labels, 'colors': COLORS})

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")