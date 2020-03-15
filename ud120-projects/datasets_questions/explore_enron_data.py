#!/usr/bin/python3

"""
    starter code for exploring the Enron dataset (emails + finances)
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# print(len(enron_data))
count = 0
# for key, value in enron_data.items():
#     if value['poi'] == 1:
#         count += 1
#
# print(count)

# poi_list = list(enron_data.values())
#
# for i in range(len(poi_list)):
#     print(poi_list[i])
#

# print(enron_data['PRENTICE JAMES']['total_stock_value'])

# print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

# print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

# Skilling, Jeffrey
# Fastow, Andrew

# print(enron_data.keys())
#
#
# print(enron_data['SKILLING JEFFREY K']['total_payments'])
# print(enron_data['FASTOW ANDREW S']['total_payments'])
# print(enron_data['LAY KENNETH L']['total_payments'])

# salary and email_address
list_main = list(enron_data.values())

# salary_list = []
# email_list = []
#
# for i in range(len(list_main)):
#     salary_list.append(list_main[i]['salary'])
#     email_list.append(list_main[i]['email_address'])
#
# c1 = 0
# c2 = 0
#
# for i in salary_list:
#     if i != 'NaN':
#         c1 += 1
#
#
# for j in email_list:
#     if j != 'NaN':
#         c2 += 1
#
# print(c1)
# print(c2)

kol = 0
for item in list_main:
    kol += 1
    # if item['total_payments'] == 'NaN':
    if item['poi']:
        count += 1

print(kol, count)
