import numpy as np

def normalized_array(data):
    new_array=np.array(data)
    new_array = (new_array - np.min(new_array)) / (np.max(new_array) - np.min(new_array))
    return new_array

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
