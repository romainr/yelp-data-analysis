Yelp Data Analysis with Hue
===========================

Hue (http://cloudera.github.com/hue) can be used for quickly starting up with Hadoop and anlysing data.
Here the Yelp Dataset challenge provides small sets ideal for starting up.

Watch the video on this blog post!


Getting Started
===============
Get the dataset from Yelp: https://www.yelp.com/dataset_challenge/

Normalize data
==============
Clean the data with https://github.com/romainr/yelp-data-analysis/blob/master/convert.py

1. Retrieve the data and extract it.
<pre>
tar -xvf yelp_phoenix_academic_dataset.tar
</pre>
<pre>
cd yelp_phoenix_academic_dataset
wget https://raw.github.com/romainr/yelp-data-analysis/master/convert.py
</pre>
<pre>
yelp_phoenix_academic_dataset$ ls
convert.py notes.txt READ_FIRST-Phoenix_Academic_Dataset_Agreement-3-11-13.pdf yelp_academic_dataset_business.json yelp_academic_dataset_checkin.json yelp_academic_dataset_review.json yelp_academic_dataset_user.json
</pre>

2. Convert it to TSV.
<pre>
chmod +x convert.py
./convert.py
</pre>

3. The column headers will be printed by the above script.
<pre>
["city", "review_count", "name", "neighborhoods", "type", "business_id", "full_address", "state", "longitude", "stars", "latitude", "open", "categories"]
["funny", "useful", "cool", "user_id", "review_id", "text", "business_id", "stars", "date", "type"]
</pre>

Create Table
==============
Create the Hive tables with the 'Create a new table from a file' in the Catalog app or Beeswax 'Tables' tab.

Upload the data files `yelp_academic_dataset_business_clean.json` and `yelp_academic_dataset_review_clean.json`. Hue will then guess the tab separator and then lets you name each column of the tables (use above column headers and paste them directly if you use Hue 2.3).

Queries
=======

Open up Hue's Hive editor named Beeswax and run:

1. **Top 25: business with most of the reviews**
<pre>
SELECT name, review_count
FROM business
ORDER BY review_count DESC
LIMIT 25
</pre>

2. **Top 25: coolest restaurants**
<pre>
SELECT r.business_id, name, SUM(cool) AS coolness
FROM review r JOIN business b
ON (r.business_id = b.business_id)
WHERE categories LIKE '%Restaurants%'
GROUP BY r.business_id, name
ORDER BY coolness DESC
LIMIT 25
</pre>

Let your imagination goes!

