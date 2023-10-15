def get_root_property(obj, number_to_find):
    for key, value in obj.items():
        if isinstance(value, dict):
            result = get_root_property(value, number_to_find)
            if result is not None:
                return f"{key}.{result}".split('.')[0]
        elif isinstance(value, list) and number_to_find in value:
            return key.split('.')[0]

object = {
 "one": {
 "nest1": {
 "val1": [9, 34, 92, 100]
 }
 },
 "2f7": {
 "n1": [10, 92, 53, 71],
 "n2": [82, 34, 6, 19]
 }
}
num = 9

print(get_root_property(object, num))