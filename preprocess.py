import pandas as pd
from sklearn import preprocessing


def text_nums_to_int(text) -> int:
    print(text)
    if text == "two":
        return 2
    elif text == "four":
        return 4
    elif text == "six":
        return 6
    else:
        print(text)
        return 0


def preprocess(dataset) -> pd.DataFrame:
    s_scaler = preprocessing.StandardScaler()
    col_names = [
        "horsepower",
        "doornumber",
        "peakrpm",
        "highwaympg",
        "citympg",
        "compressionratio",
        "stroke",
        "boreratio",
        "enginesize",
        "wheelbase",
        "price",
    ]
    dataset["doornumber_temp"] = dataset["doornumber"].apply(lambda x: text_nums_to_int(x))
    print()
    features = s_scaler.fit_transform(
        [
            dataset["horsepower"],
            dataset["doornumber_temp"],
            dataset["peakrpm"],
            dataset["highwaympg"],
            dataset["citympg"],
            dataset["compressionratio"],
            dataset["stroke"],
            dataset["boreratio"],
            dataset["enginesize"],
            dataset["wheelbase"],
        ]
    )
    features = pd.DataFrame(features.T)
    features.insert(loc=10, column="price", value=dataset["price"])
    features.columns = col_names
    return features


print("test")
