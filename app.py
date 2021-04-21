import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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


#################################################
# Flask Routes
#################################################

#
# Base route, API specs
#


@app.route("/v1.0")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/v1.0/<br/>"
        f"/v1.0/products<br/>"
    )

@app.route("/v1.0/products")
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

# main program
if __name__ == '__main__':
    app.run(debug=True)