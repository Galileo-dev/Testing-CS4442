import supabase
import os
import json

class SupabaseDB:

    key = os.environ.get('supabase_key')

    # Initialize the client
    client = supabase.create_client("https://vbttpsyzcnwxfneipfrx.supabase.co", key)

    def add_object(object, table_name: str):
        result = SupabaseDB.client.from_(table_name).insert(json.dumps(object.__dict__)).execute()
        return result
    
    def get_table(table_name: str):
        result = SupabaseDB.client.from_(table_name).select("*").execute()
        return result

    def delete_object(object, table_name: str):
        result = SupabaseDB.client.from_(table_name).delete().match(object).execute()
        return result
    
