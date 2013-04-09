#!/usr/bin/env python
"""
Convert to TSV format and un-nest fields. Print headers at the end.

tar -xvf yelp_phoenix_academic_dataset.tar

cd yelp_phoenix_academic_dataset
wget convert.py

yelp_phoenix_academic_dataset$ ls
convert.py  notes.txt  READ_FIRST-Phoenix_Academic_Dataset_Agreement-3-11-13.pdf  yelp_academic_dataset_business.json  yelp_academic_dataset_checkin.json  yelp_academic_dataset_review.json  yelp_academic_dataset_user.json

chmod +x convert.py
./convert.py

[u'city', u'review_count', u'name', u'neighborhoods', u'type', u'business_id', u'full_address', u'state', u'longitude', u'stars', u'latitude', u'open', u'categories']
[u'funny', u'useful', u'cool', u'user_id', u'review_id', u'text', u'business_id', u'stars', u'date', u'type']

yelp_phoenix_academic_dataset$ ls
convert.py  READ_FIRST-Phoenix_Academic_Dataset_Agreement-3-11-13.pdf  yelp_academic_dataset_business.json       yelp_academic_dataset_checkin.json  yelp_academic_dataset_user.json
notes.txt   yelp_academic_dataset_business_clean.json                  yelp_academic_dataset_review_clean.json  yelp_academic_dataset_review.json
"""

import json


business_clean = open('yelp_academic_dataset_business_clean.json', 'w+')

for line in open('yelp_academic_dataset_business.json'):
  business_json = json.loads(line)
  business = map(unicode, business_json.values())
  business_clean.write(u'\t'.join(business).replace('\n', ' ').encode('utf-8') + '\n')

print json.dumps(business_json.keys())


review_clean = open('yelp_academic_dataset_review_clean.json', 'w+')

for line in open('yelp_academic_dataset_review.json'):
  review_json = json.loads(line)
  review_json_votes = review_json['votes']
  review_json['votes'] = '\t'.join(map(unicode, review_json_votes.values()))  
  review = map(unicode, review_json.values())  
  review_clean.write(u'\t'.join(review).replace('\n', ' ').encode('utf-8') + '\n')

print json.dumps(review_json_votes.keys() + review_json.keys()[1:])
