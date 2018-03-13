import pandas as pd
import urllib.request as request
from sklearn.preprocessing import LabelEncoder

def download():
    request.urlretrieve("https://chronicdata.cdc.gov/api/views/dxpw-cm5u/rows.csv?accessType=DOWNLOAD",
                        "data/dataset.csv")

    pd.read_csv("data/dataset.csv").to_csv("data/dataset.csv", index=False, columns=["StateAbbr",
                                                                                     # "PlaceName",
                                                                                     "BPHIGH_CrudePrev",
                                                                                     "CANCER_CrudePrev",
                                                                                     "CHD_CrudePrev",
                                                                                     "CSMOKING_CrudePrev",
                                                                                     "DIABETES_CrudePrev",
                                                                                     "HIGHCHOL_CrudePrev",
                                                                                     "OBESITY_CrudePrev",
                                                                                     "SLEEP_CrudePrev",
                                                                                     "TEETHLOST_CrudePrev"])

# def fill_nan():
#     dataset = pd.read_csv("data/dataset.csv")
#     cols = ["BPHIGH_CrudePrev",
#                 "CANCER_CrudePrev",
#                 "CHD_CrudePrev",
#                 "CSMOKING_CrudePrev",
#                 "DIABETES_CrudePrev",
#                 "HIGHCHOL_CrudePrev",
#                 "OBESITY_CrudePrev",
#                 "SLEEP_CrudePrev",
#                 "TEETHLOST_CrudePrev"]
#     for col in cols:
#         dataset[col] = dataset[col].fillna(dataset[col].mean())
#     dataset.to_csv("data/dataset.csv", index=False)

# def label_encode():
#     dataset = pd.read_csv("data/dataset.csv")
#     cols = ["StateAbbr",
#             "PlaceName"]
#     for col in cols:
#         dataset[col] = pd.DataFrame(LabelEncoder().fit_transform(dataset[col]))
#     dataset.to_csv("data/dataset.csv", index=False)

if __name__ == "__main__":
    download()