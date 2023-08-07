# SOURCE

import os
from dotenv import load_dotenv
import mysql.connector
import csv

from test.zip_code_ingester import unit_tests

# Load environment variables from .env file
load_dotenv()


# TODO migrate this to postgresql
# TODO create mysqldb P_06_DB, connected to .env file
# TODO move protocols to .env
# MySQL connection details
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')


# Create database connection
# TODO change db to project specific name
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)


def create_table():
    """
    Create a table in the mysql database
    :param:
    :return:
    :TODO: write test if db is active in tests
    :TODO: move table values to .yaml
    :TODO: discover how many data points NWMLS has
    :FIXME:
    """
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS real_estate (
            period_begin DATE,
            period_end DATE,
            period_duration INT,
            region_type VARCHAR(100),
            region_type_id INT,
            table_id INT,
            is_seasonally_adjusted VARCHAR(1),
            region VARCHAR(100),
            city VARCHAR(100),
            state VARCHAR(100),
            state_code VARCHAR(2),
            property_type VARCHAR(100),
            property_type_id INT,
            median_sale_price DECIMAL(18, 6),
            median_sale_price_mom DECIMAL(18, 6),
            median_sale_price_yoy DECIMAL(18, 6),
            median_list_price DECIMAL(18, 6),
            median_list_price_mom DECIMAL(18, 6),
            median_list_price_yoy DECIMAL(18, 6),
            median_ppsf DECIMAL(18, 6),
            median_ppsf_mom DECIMAL(18, 6),
            median_ppsf_yoy DECIMAL(18, 6),
            median_list_ppsf DECIMAL(18, 6),
            median_list_ppsf_mom DECIMAL(18, 6),
            median_list_ppsf_yoy DECIMAL(18, 6),
            homes_sold INT,
            homes_sold_mom INT,
            homes_sold_yoy INT,
            pending_sales INT,
            pending_sales_mom INT,
            pending_sales_yoy INT,
            new_listings INT,
            new_listings_mom INT,
            new_listings_yoy INT,
            inventory INT,
            inventory_mom INT,
            inventory_yoy INT,
            months_of_supply DECIMAL(18, 6),
            months_of_supply_mom DECIMAL(18, 6),
            months_of_supply_yoy DECIMAL(18, 6),
            median_dom DECIMAL(18, 6),
            median_dom_mom DECIMAL(18, 6),
            median_dom_yoy DECIMAL(18, 6),
            avg_sale_to_list DECIMAL(18, 6),
            avg_sale_to_list_mom DECIMAL(18, 6),
            avg_sale_to_list_yoy DECIMAL(18, 6),
            sold_above_list DECIMAL(18, 6),
            sold_above_list_mom DECIMAL(18, 6),
            sold_above_list_yoy DECIMAL(18, 6),
            price_drops DECIMAL(18, 6),
            price_drops_mom DECIMAL(18, 6),
            price_drops_yoy DECIMAL(18, 6),
            off_market_in_two_weeks DECIMAL(18, 6),
            off_market_in_two_weeks_mom DECIMAL(18, 6),
            off_market_in_two_weeks_yoy DECIMAL(18, 6),
            parent_metro_region VARCHAR(100),
            parent_metro_region_metro_code INT,
            last_updated DATETIME
        )
    """)
    db.commit()


def import_data(file_path):
    """
    Import data from a TSV file into the database
    :param:
    :return:
    """
    cursor = db.cursor()
    with open(file_path, 'r') as tsv_file:
        reader = csv.reader(tsv_file, delimiter='\t')
        next(reader)  # Skip header row
        for row in reader:
            cursor.execute("""
                INSERT INTO real_estate (
                    period_begin, period_end, period_duration, region_type, region_type_id, table_id,
                    is_seasonally_adjusted, region, city, state, state_code, property_type, property_type_id,
                    median_sale_price, median_sale_price_mom, median_sale_price_yoy, median_list_price,
                    median_list_price_mom, median_list_price_yoy, median_ppsf, median_ppsf_mom, median_ppsf_yoy,
                    median_list_ppsf, median_list_ppsf_mom, median_list_ppsf_yoy, homes_sold, homes_sold_mom,
                    homes_sold_yoy, pending_sales, pending_sales_mom, pending_sales_yoy, new_listings,
                    new_listings_mom, new_listings_yoy, inventory, inventory_mom, inventory_yoy, months_of_supply,
                    months_of_supply_mom, months_of_supply_yoy, median_dom, median_dom_mom, median_dom_yoy,
                    avg_sale_to_list, avg_sale_to_list_mom, avg_sale_to_list_yoy, sold_above_list,
                    sold_above_list_mom, sold_above_list_yoy, price_drops, price_drops_mom, price_drops_yoy,
                    off_market_in_two_weeks, off_market_in_two_weeks_mom, off_market_in_two_weeks_yoy,
                    parent_metro_region, parent_metro_region_metro_code, last_updated
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, row)
    db.commit()


if __name__ == '__main__':
    unit_tests()
