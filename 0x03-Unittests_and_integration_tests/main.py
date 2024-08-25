access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


data = get_json("https://jsonplaceholder.typicode.com/posts/2")

# Print the result
for key in data:
    print(f"Key : {key}, value : {data[key]}")