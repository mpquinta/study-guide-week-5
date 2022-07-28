"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?
# Object



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?
# An association table's main function is to marry two tables that have a 
# many-to-many relationship. An association table's fields are not meaningful
# and cannot stand alone.


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter_by(brand_id="ram").all()
q1_key = Brand.query.get("ram")

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter_by(name = "Corvette", brand_id="che").all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year<1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded>1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.startswith("Cor")).all()
q5_key = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded==1903, Brand.discontinued==None).all()
q6 = Brand.query.filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued!=None) | (Brand.founded<1950)).all()
q7_key = Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded<1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != "for").all()


# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""
    model_facts = Model.query.filter_by(year=year).all()
    for model in model_facts:
        print("Model name: ", model.name)
        print("Brand name: ", model.brands.name)
        print("Brand headsquarters: ", model.brands.headquarters)
    


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""
    brand_ids = Brand.query.all()
    for id in brand_ids:
        print("Brand: ", id.name)
        for model in id.models:
            print(model.name, model.year)
    
def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""
    brands = Brand.query.filter(Brand.name.like(f'%{mystr}%')).all()
    print(brands)
    


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""
    results = Model.query.filter(db.and_(Model.year>=start_year, Model.year<end_year)).all()
    print(results)

