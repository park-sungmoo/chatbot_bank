import pymongo
import intent_office

def get_entity(line, entity_list, num):
    connection = pymongo.MongoClient("localhost", 27017)
    db = connection.testDB
    collection_name = "Slot" + str(num)
    co = db[collection_name]
    for entity in co.distinct("EntityName"):
        if entity in line:
            entity_class = co.distinct("EntityClass", {"EntityName": entity})
            line = line.replace(entity, entity_class[0])
            entity_list.append(entity)
    return line, entity_list


def get_location(line):
    connection = pymongo.MongoClient("localhost", 27017)
    db = connection.testDB
    answer = line
    for it in ["Dong", "Ro", "Gu", "Si"]:
        co = db[it].find({})
        for address in co:
            for name in address.keys():
                if name == '_id':
                    continue
                else:
                    if answer.find(name) != -1:
                        answer = answer.replace(name, '지점')

    return answer


#print(get_location("광진구 금고 수유동 위치"))

