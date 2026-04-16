import numpy as np

def normalized_array(input_array):
  new_array=np.array(input_array)
  min_val = np.min(new_array)
  max_val = np.max(new_array)
  if max_val == min_val:
        return np.zeros_like(new_array)

  new_array = (new_array - np.min(new_array)) / (np.max(new_array) - np.min(new_array))

  return new_array
if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
