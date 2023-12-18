from pymongo import MongoClient

def connect_to_mongodb():
    #connect
    client = MongoClient('localhost', 27017)
    db = client.RideSnowboards
    return db.Snowboards

def search_collection(collection):
    #input our query as a Python dictionary. For example: {"camber": "Twin Extra"}
    query = input("Enter your query (in Python dictionary format): ")
    try:
        query_dict = eval(query)
    except Exception as e:
        print(f"Error in query format: {e}")
        return []
    try:
        results = list(collection.find(query_dict))
        return results
    except Exception as e:
        print(f"Error in executing query: {e}")
        return []
    
def main():
    collection = connect_to_mongodb()
    results = search_collection(collection)
    if results:
        print("Search Results:")
        for result in results:
            print(result)
    else:
        print("No results found or error in query.")

if __name__ == "__main__":
    main()