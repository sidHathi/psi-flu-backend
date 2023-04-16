from pymongo import MongoClient
from datetime import datetime

def increment_user_count(mongo_uri, db_name):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    old_count = db["current_aggregates"].find_one({})["number_of_users"]
    db["current_aggregates"].update_one({}, { "$set": { 'number_of_users': old_count + 1 } })
    db["current_aggregates"].update_one({}, { "$set": { 'timestamp': datetime.now()} })

def decrement_user_count(mongo_uri, db_name):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    old_count = db["current_aggregates"].find_one({})["number_of_users"]
    db["current_aggregates"].update_one({}, { "$set": { 'number_of_users': max(0, old_count - 1) } })
    db["current_aggregates"].update_one({}, { "$set": { 'timestamp': datetime.now()} })

def increment_new_infections_in_last_week(mongo_uri, db_name):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    old_count = db["current_aggregates"].find_one({})["new_infections_in_last_week"]
    db["current_aggregates"].update_one({}, { "$set": { 'new_infections_in_last_week': old_count + 1 } })
    db["current_aggregates"].update_one({}, { "$set": { 'timestamp': datetime.now()} })

def increment_number_of_infections(mongo_uri, db_name):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    old_count = db["current_aggregates"].find_one({})["current_number_of_infections"]
    db["current_aggregates"].update_one({}, { "$set": { 'current_number_of_infections': old_count + 1 } })
    db["current_aggregates"].update_one({}, { "$set": { 'timestamp': datetime.now()} })

def decrement_number_of_infections(mongo_uri, db_name):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    old_count = db["current_aggregates"].find_one({})["current_number_of_infections"]
    db["current_aggregates"].update_one({}, { "$set": { 'current_number_of_infections': max(0, old_count - 1) } })
    db["current_aggregates"].update_one({}, { "$set": { 'timestamp': datetime.now()} })


def increment_symptom_count(mongo_uri, db_name, symptom):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    old_count = db["current_aggregates"].find_one({})["symptom_counts"][symptom]
    new_count = old_count + 1
    
    symptoms_list = db["current_aggregates"].find_one({})["symptoms_sorted_by_count_desc"]
    symptoms_list.remove(symptom)

    for i in range(len(symptoms_list)):
        if new_count >= db["current_aggregates"].find_one({})["symptom_counts"][symptoms_list[i]]:
            symptoms_list.insert(i, symptom)
            break
    
    db["current_aggregates"].update_one({}, { "$set": { f'symptom_counts.{symptom}': new_count, 'symptoms_sorted_by_count_desc': symptoms_list } })
    db["current_aggregates"].update_one({}, { "$set": { 'timestamp': datetime.now()} })



def decrement_symptom_count(mongo_uri, db_name, symptom):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    old_count = db["current_aggregates"].find_one({})["symptom_counts"][symptom]
    new_count = old_count - 1
    
    symptoms_list = db["current_aggregates"].find_one({})["symptoms_sorted_by_count_desc"]
    symptoms_list.remove(symptom)

    for i in range(len(symptoms_list)):
        if new_count >= db["current_aggregates"].find_one({})["symptom_counts"][symptoms_list[i]]:
            symptoms_list.insert(i, symptom)
            break
    
    db["current_aggregates"].update_one({}, { "$set": { f'symptom_counts.{symptom}': new_count, 'symptoms_sorted_by_count_desc': symptoms_list } })
    db["current_aggregates"].update_one({}, { "$set": { 'timestamp': datetime.now()} })

