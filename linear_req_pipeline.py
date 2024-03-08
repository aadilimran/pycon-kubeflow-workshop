import kfp
from kfp.v2.dsl import component, Output, Input, Artifact, Dataset, Model



def download_data(input_url: str, output_csv: Output[Dataset]):
    import pandas as pd
    data = pd.read_csv(input_url)  # Read csv file
    print(data.head())
    print(data.info())
    data.to_csv(output_csv.path, index=False)



def data_preparation(test_size: float, random_state: int, data_path: Input[Artifact], output_X_train: Output[Artifact], output_X_test: Output[Artifact], output_y_train: Output[Artifact],output_y_test: Output[Artifact]):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    import numpy as np
    data = pd.read_csv(data_path.path)  # Read csv file
    print(data.head())

    # dropping unnecesary features.
    data.drop(["Date", "Location", "WindGustDir", "WindDir9am", "WindDir3pm", "RainTomorrow", "RISK_MM"], axis=1,
              inplace=True)

    # fill NaN values with his feature's median value
    data.fillna(data.median(), inplace=True)

    # convert Rain Today feature yo to binary values ( 0 or 1 )
    data.RainToday = [1 if i == 'Yes' else 0 for i in data.RainToday]

    # normalize data
    x = data.drop("RainToday", axis=1).values
    x = (x - np.min(x)) / (np.max(x) - np.min(x))
    y = data.RainToday.values

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)

    print(f"""
    x_train's shape is {X_train.shape} 
    x_test's shape is {X_test.shape}
    y_train's shape is {y_train.shape}
    y_test's shape is  {y_test.shape}
    """)
    np.savetxt(output_X_train.path, X_train, delimiter=",")
    np.savetxt(output_X_test.path, X_test, delimiter=",")
    np.savetxt(output_y_train.path, y_train, delimiter=",")
    np.savetxt(output_y_test.path, y_test, delimiter=",")



def training(input_X_train: Input[Artifact], input_y_train: Input[Artifact], model_output: Output[Model]):
    # import pandas as pd
    import numpy as np
    from sklearn.linear_model import LogisticRegression
    import pickle

    X_train = np.loadtxt(input_X_train.path, delimiter=",")
    y_train = np.loadtxt(input_y_train.path, delimiter=",")

    # X_train = pd.read_csv(input_X_train.path)
    # y_train = pd.read_csv(input_y_train.path)
    print(f"X_train shape: {X_train.shape}")
    print(f"y_train shape: {y_train.shape}")

    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)
    pickle.dump(lr_model, open((model_output.path), 'wb'))



def testing(input_X_test: Input[Artifact], input_y_test: Input[Artifact], model_output: Input[Model]):
    import pandas as pd
    import numpy as np
    import pickle

    X_test = np.loadtxt(input_X_test.path, delimiter=",")
    y_test = np.loadtxt(input_y_test.path, delimiter=",")
    print(f"X_test shape: {X_test.shape}")
    print(f"y_test shape: {y_test.shape}")

    model = pickle.load(open(model_output.path, 'rb'))
    print("Our model's score is ", model.score(X_test, y_test))


def LR_model_train_test_pipeline(dataset_url: str, test_size: float, random_state: int):
    # Create pipeline Graph here.
