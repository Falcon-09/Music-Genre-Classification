from flask import Flask,url_for

def predict_gen(meta):
    import pickle
    import os
    import numpy as np
    path = os.path.join('D:\Music Genre\model', 'models.pickle')
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    svmo = data['svmo']
    scale = data['scale']
    lgn = data['lgn']
    meta = np.array(meta)
    x = scale.transform([meta])
    pred = svmo.predict(x)
    return(lgn[pred[0]])

