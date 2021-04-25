import pickle
import json
import numpy as np

region=None
data_cols=None
model=None

def load_saved_artifacts():
        print("loading saved artifacts...start")
        global  data_cols
        global region

        with open("columns1.json", "r") as f:
            data_cols = json.load(f)['data_columns']
            region = data_cols[5:]  

        global model
        if model is None:
            with open('models.pickle', 'rb') as f:
                model = pickle.load(f)

        print("loading saved artifacts...done")

def smoker_predict(age,sex,bmi,region,smoker):
    region_list=['northeast', 'northwest', 'southeast', 'southwest']
    if region in region_list :
        
        if smoker==1:
            return('yes the person is smoker')
        else:
            return("no the person is not a smoker")
    else: return("invalid region name")

def get_region_names():
    return region

def get_data_columns():
    return data_cols

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_region_names())
    print(smoker_predict(19,0,27.9,'southwest',1))
    