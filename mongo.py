from pymongo import MongoClient
from pprint import pprint



#db = client['Personagens']
#db.Personagens.insert_one({ "_id": 1, "name": "John", "address": "Highway 37"})

#pprint(list(db.Personagens.find({}, {'Idade' :1})))


def check_mongo(client: object = None, db: str = None , collection: str = None, verbose: bool = True) -> tuple:
    client_check = False
    db_check = False
    collection_check = False
    
    if client:
        if isinstance(client, MongoClient):
            if verbose:
                print(f'[TRUE ]  Client EXISTE!')
            client_check = True
            if db:
                if db in client.list_database_names():
                    if verbose:
                        print(f'[TRUE ]  Banco de dados "{db}" EXISTE no Host/Client"')
                    db_check = True
                else:
                    if verbose:
                        print('[FALSE]  Bd NÃO existe no Host/Client')
                    
                if collection:
                    if collection in client[db].list_collection_names():
                        if verbose:
                            print(f'[TRUE]  Collection/Tabela "{collection}" existe em no Banco de Dados')
                        collection_check = True
                    else:
                        if verbose:
                            print(f'[FALSE]  Collection/Tabela "{collection}" NÃO encontrada em BD')
                else:
                    pass    
            else:
                pass
        else:
            if verbose:
                print('Client não uma instância de MongoClient')
            
    return (client_check, db_check, collection_check)


client = MongoClient("mongodb+srv://hirios:fendadobiquini@iniciante.myuv7.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = 'Personagens'

if check_mongo(client, 'Personagens', 'Avatar', verbose=False)[2]:
    pprint(list(client.Personagens.Avatar.find({"Idade": {"$gt": 1}})))

client.Personagens.Avatar.delete_many({"Idade": {"$gt": 15}})
#client.local.foda.update_one({'bofff': {'$exists':1 }}, {'$set': {'Eitaa': 'Yes', 'Nova': 'No'}})
