# import hyper as hp 
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import load_model
# import pickle
# with open("variable.pkl", "rb") as f:
#     a_loaded = pickle.load(f)
#     b_loaded = pickle.load(f)
#     c_loaded = pickle.load(f)
#     d_loaded = pickle.load(f)
# print(f"a: {a_loaded}")
# print(f"b: {b_loaded}")
# print(f"c: {c_loaded}")
# print(f"d: {d_loaded}")
import csv
with open("data.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Lợi','OK'])
