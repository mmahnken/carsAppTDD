from flask import Flask, request, render_template, jsonify
from model import db, connect_to_db, Model, Brand
from sqlalchemy import func

app = Flask(__name__)

@app.route("/")
def show_homepage():
    return render_template("index.html")

@app.route("/cars")
def show_cars_index():
    all_cars = Model.query.all()
    return render_template("cars.html", cars=all_cars)

@app.route("/chart-data")
def scrub_data_for_charts():
    # get count of cars by brand
    counts = db.session\
                 .query(Model.brand_name, func.count(Model.brand_name))\
                 .group_by(Model.brand_name)\
                 .all()    # list of tuples (Name, Count)


    list_of_counts = [ int(c[1]) for c in counts ]
    list_of_names = [ c[0] for c in counts ]

    data_dict = {
        "labels": list_of_names,
        "datasets": [
            {
                "data": list_of_counts,
                "backgroundColor": [
                "#1f77b4",
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
                "#9edae5",
                ]

            }
        ]
    }


    # data_dict = {
    #             "labels": [
    #                 "Christmas Melon",
    #                 "Crenshaw",
    #                 "Yellow Watermelon"
    #             ],
    #             "datasets": [
    #                 {
    #                     "data": [300, 50, 100],
    #                     "backgroundColor": [
    #                         "#FF6384",
    #                         "#36A2EB",
    #                         "#FFCE56"
    #                     ],
    #                     "hoverBackgroundColor": [
    #                         "#FF6384",
    #                         "#36A2EB",
    #                         "#FFCE56"
    #                     ]
    #                 }]
    #         }


    return jsonify(data_dict)

@app.route('/charts')
def show_charts():
    return render_template("charts.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")