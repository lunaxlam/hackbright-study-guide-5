"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from shutil import which
from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

    # <flask_sqlalchemy.BaseQuery object at 0x1047f14c0>

# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

    # An Association Table is the "glue" between two tables. 
    # It is different from a Middle Table in that it does not have any unique field
    # of its own. It only consists of the primary keys of the related tables, which
    # function as the Association Table's foreign keys.TabError

    # It manages a "many to many" relationship.


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = db.session.query(Brand).filter(Brand.brand_id == 'ram').first()
q1_ = Brand.query.filter_by(brand_id = 'ram').all()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = db.session.query(Model).filter(Model.name == 'Corvette', Model.brand_id == 'che')

# Get all models that are older than 1960.
q3 = db.session.query(Model).filter(Model.year > 1960). all()

# Get all brands that were founded after 1920.
q4 = db.session.query(Brand).filter(Brand.founded > 1920). all()

# Get all models with names that begin with ``Cor``.
q5 = db.session.query(Model).filter(Model.name.like('Cor%')). all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = db.session.query(Brand).filter((Brand.founded < 1950) | (Brand.discontinued != None)).all()

# Get all models whose brand_id is not ``for``.
q8 = db.session.query(Model).filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    pass


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    pass


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    pass


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    pass

