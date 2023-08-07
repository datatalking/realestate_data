# SOURCE https://dev.socrata.com/foundry/data.kingcounty.gov/4854-i48r
# SOURCE https://kingcounty.gov/search.aspx?utf8=✓&q=data

#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy


import pandas as pd
from sodapy import Socrata


# :TODO: move api keys to .env file
# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.kingcounty.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.kingcounty.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("4854-i48r", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# TODO sodapy depricated sort of. https://dev.socrata.com/docs/endpoints.html
# TODO how to access valuation
# TODO create index of all properties maximium, start with king county, then pierce, snohomish etc
# empty property search
# commercial and residentaial
# TODO EXTR_ValueHistory_V.csv at Users/wadewilson/sbox/Value History/
# TODO https://www.warse.org/IJATCSE/static/pdf/file/ijatcse235932020.pdf



