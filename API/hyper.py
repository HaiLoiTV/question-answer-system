import pickle
with open("variable.pkl", "rb") as f:
    tokenizer = pickle.load(f)
    le = pickle.load(f)
    responses = pickle.load(f)
    input_shape = pickle.load(f) 
    vocabulary = pickle.load(f) 
    output_length = pickle.load(f) 

