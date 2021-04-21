import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, redirect, send_from_directory

import os

from db_info import db_user, db_password, db_name

#################################################
# Database Setup
#################################################
connect_string = f"postgresql://{db_user}:{db_password}@localhost:5432/{db_name}"
engine = create_engine(connect_string)


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Supermarket = Base.classes.supermarket

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

ver_str = "/v1.0"


#################################################
# Flask Routes
#################################################

#
# Base route for index page
#

@app.route("/")
def welcome():
    return render_template("index.html")

#
# Show API routes
#

@app.route(f"{ver_str}")
def api_base():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"{ver_str}<br/>"
        f"{ver_str}/products<br/>"
    )
#
# Get a list of products
#

@app.route(f"{ver_str}/products")
def products():
    # Get the measure scores
    # Create session (link) from Python to the DB
    session = Session(engine)

    """Return a list of a dicionary for mortalites by state"""
    # Query all for mortality
    query = session.query(func.distinct(Supermarket.product_line))

    # debug query
    print(query.statement.compile())

    # Get all the results
    results = query.all()

    session.close()  

    products = []
    for product in results:
        products.append(product)

    return jsonify(products)

#
# Get count of invoices by gender
#

@app.route(f"{ver_str}/genderinvoices")
def gender_invoices():
    return jsonify({})


#
# Add favicon
#


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
# main program
if __name__ == '__main__':
    app.run(debug=True)