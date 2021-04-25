import pickle
import json
import numpy as np
file_path = 'models.pickle'
model = pickle.load(open(file_path,'rb'))

def get_region_names():
        with open("columns1.json", "r") as f:
            region_list_1 = json.load(f)['data_columns']
        return region_list_1[5:]

def get_smoker_predict(age,sex,bmi,region,smoker):
    region_list=['northeast', 'northwest', 'southeast', 'southwest']
    if region in region_list :
        
        if smoker==1:
            return('yes the person is smoker')
        else:
            return("no the person is not a smoker")
    else: return("invalid region name")

    
if __name__ == "__main__":
    
    smoker  = get_smoker_predict(19,0,27.9,'southwest',1)
    print("smoker or not:",smoker)