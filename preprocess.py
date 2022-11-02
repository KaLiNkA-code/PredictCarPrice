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
    dataset["doornumber"] = dataset["doornumber"].apply(lambda x: int(x == "two"))

    s_scaler = preprocessing.StandardScaler().fit(dataset)
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

    print()
    features = s_scaler.fit_transform(
        [
            dataset["horsepower"],
            dataset["doornumber"],
            dataset["peakrpm"],
            dataset["highwaympg"],
            dataset["citympg"],
            dataset["compressionratio"],
            dataset["stroke"],
            dataset["boreratio"],
            dataset["enginesize"],
            dataset["wheelbase"],
            dataset["price"],
        ]
    )
    features = pd.DataFrame(features.T)
    features.columns = col_names
    return features


def preprocess_v2(dataset) -> pd.DataFrame:
    s_scaler_horsepower = preprocessing.StandardScaler()
    s_scaler_doornumber = preprocessing.StandardScaler()
    s_scaler_peakrpm = preprocessing.StandardScaler()
    s_scaler_highwaympg = preprocessing.StandardScaler()
    s_scaler_citympg = preprocessing.StandardScaler()
    s_scaler_compressionratio = preprocessing.StandardScaler()
    s_scaler_stroke = preprocessing.StandardScaler()
    s_scaler_boreratio = preprocessing.StandardScaler()
    s_scaler_enginesize = preprocessing.StandardScaler()
    s_scaler_wheelbase = preprocessing.StandardScaler()

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

    doornumber_temp_list = []
    for i in dataset["doornumber"]:
        if i == "two":
            doornumber_temp_list.append(2)
        elif i == "four":
            doornumber_temp_list.append(4)
        elif i == "six":
            doornumber_temp_list.append(6)
        else:
            doornumber_temp_list.append(0)

    doornumber_temp_list_df = pd.DataFrame(doornumber_temp_list)
    dataset.insert(loc=0, column="doornumber_temp", value=doornumber_temp_list_df)

    feature_horsepower = s_scaler_horsepower.fit_transform(dataset[["horsepower"]])
    features_doornumber = s_scaler_doornumber.fit_transform(dataset[["doornumber_temp"]])
    features_peakrpm = s_scaler_peakrpm.fit_transform(dataset[["peakrpm"]])
    features_highwaympg = s_scaler_highwaympg.fit_transform(dataset[["highwaympg"]])
    features_citympg = s_scaler_citympg.fit_transform(dataset[["citympg"]])
    features_compressionratio = s_scaler_compressionratio.fit_transform(dataset[["compressionratio"]])
    features_stroke = s_scaler_stroke.fit_transform(dataset[["stroke"]])
    features_boreratio = s_scaler_boreratio.fit_transform(dataset[["boreratio"]])
    features_enginesize = s_scaler_enginesize.fit_transform(dataset[["enginesize"]])
    features_wheelbase = s_scaler_wheelbase.fit_transform(dataset[["wheelbase"]])

    features = pd.DataFrame()
    features.insert(loc=0, column=col_names[0], value=feature_horsepower)
    features.insert(loc=1, column=col_names[1], value=features_doornumber)
    features.insert(loc=2, column=col_names[2], value=features_peakrpm)
    features.insert(loc=3, column=col_names[3], value=features_highwaympg)
    features.insert(loc=4, column=col_names[4], value=features_citympg)
    features.insert(loc=5, column=col_names[5], value=features_compressionratio)
    features.insert(loc=6, column=col_names[6], value=features_stroke)
    features.insert(loc=7, column=col_names[7], value=features_boreratio)
    features.insert(loc=8, column=col_names[8], value=features_enginesize)
    features.insert(loc=9, column=col_names[9], value=features_wheelbase)

    features.insert(loc=10, column="price", value=dataset["price"])
    features.columns = col_names
    return features


def preprocess_v22(dataset) -> pd.DataFrame:
    s_scaler_horsepower = preprocessing.StandardScaler()
    s_scaler_doornumber = preprocessing.StandardScaler()
    s_scaler_peakrpm = preprocessing.StandardScaler()
    s_scaler_highwaympg = preprocessing.StandardScaler()
    s_scaler_citympg = preprocessing.StandardScaler()
    s_scaler_compressionratio = preprocessing.StandardScaler()
    s_scaler_stroke = preprocessing.StandardScaler()
    s_scaler_boreratio = preprocessing.StandardScaler()
    s_scaler_enginesize = preprocessing.StandardScaler()
    s_scaler_wheelbase = preprocessing.StandardScaler()

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

    # doornumber_temp_list = []
    # for i in dataset["doornumber"]:
    #     if i == 'two':
    #         doornumber_temp_list.append(2)
    #     elif i == 'four':
    #         doornumber_temp_list.append(4)
    #     elif i == 'six':
    #         doornumber_temp_list.append(6)
    #     else:
    #         doornumber_temp_list.append(0)

    dataset["is_two"] = dataset["doornumber"].apply(lambda x: int(x == "two"))

    feature_horsepower = s_scaler_horsepower.fit_transform(dataset[["horsepower"]])
    features_doornumber = s_scaler_doornumber.fit_transform(dataset[["is_two"]])
    features_peakrpm = s_scaler_peakrpm.fit_transform(dataset[["peakrpm"]])
    features_highwaympg = s_scaler_highwaympg.fit_transform(dataset[["highwaympg"]])
    features_citympg = s_scaler_citympg.fit_transform(dataset[["citympg"]])
    features_compressionratio = s_scaler_compressionratio.fit_transform(dataset[["compressionratio"]])
    features_stroke = s_scaler_stroke.fit_transform(dataset[["stroke"]])
    features_boreratio = s_scaler_boreratio.fit_transform(dataset[["boreratio"]])
    features_enginesize = s_scaler_enginesize.fit_transform(dataset[["enginesize"]])
    features_wheelbase = s_scaler_wheelbase.fit_transform(dataset[["wheelbase"]])
    print(feature_horsepower)

    features = pd.DataFrame(
        {
            col_names[0]: feature_horsepower[0],
            col_names[1]: features_doornumber[0],
            col_names[2]: features_peakrpm[0],
            col_names[3]: features_highwaympg[0],
            col_names[4]: features_citympg[0],
            col_names[5]: features_compressionratio[0],
            col_names[6]: features_stroke[0],
            col_names[7]: features_boreratio[0],
            col_names[8]: features_enginesize[0],
            col_names[9]: features_wheelbase[0],
            col_names[10]: dataset["price"],
        }
    )
    # print(2)
    # features.insert(loc=0, column=col_names[0], value=pd.DataFrame(feature_horsepower))
    # print(3)
    # features.insert(loc=1, column=col_names[1], value=features_doornumber)
    # features.insert(loc=1, column=col_names[2], value=features_peakrpm)
    # print(Feature)
    # features.insert(loc=2, column=col_names[3], value=features_highwaympg)
    # features.insert(loc=3, column=col_names[4], value=features_citympg)
    # print(Feature)
    # features.insert(loc=4, column=col_names[5], value=features_compressionratio)
    # features.insert(loc=5, column=col_names[6], value=features_stroke)
    # features.insert(loc=6, column=col_names[7], value=features_boreratio)
    # print(Feature
    # features.insert(loc=7, column=col_names[8], value=features_enginesize)
    # features.insert(loc=8, column=col_names[9], value=features_wheelbase)

    #  features.insert(loc=10, column="price", value=dataset["price"])
    # features.columns = col_names
    return features
