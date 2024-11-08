def clean_empty_spaces(collection):
    # Find and clean documents
    for document in collection.find():
        update_fields = {}
        for field, value in document.items():
            if isinstance(value, str):
                # Strip leading and trailing spaces
                trimmed_value = value.strip()
                if trimmed_value != value:
                    update_fields[field] = trimmed_value
            elif isinstance(value, dict):
                # If it's a nested object, clean it recursively
                for sub_field, sub_value in value.items():
                    if isinstance(sub_value, str):
                        trimmed_sub_value = sub_value.strip()
                        if trimmed_sub_value != sub_value:
                            if field not in update_fields:
                                update_fields[field] = value.copy()
                            update_fields[field][sub_field] = trimmed_sub_value

        # Update the document if there are fields to clean
        if update_fields:
            collection.update_one({'_id': document['_id']}, {'$set': update_fields})
    print("Database cleaned successfully.")