
# Polynomial Curve Fitting Model Explanation

This is a pet project designed particularly to understand the brains behind hyperparameter tuning using configparser. This project performs a polynomial curve fitting on a custom generated sin curve dataset. Here's a detailed breakdown of its components and processes:

## Importing Libraries

```python
from model.Polynomial_curve_fitting_model import Polynomial_curve_fitting_model
import configparser
import os
```

- `Polynomial_curve_fitting_model`: A custom model class, defined in another file, responsible for the polynomial curve fitting.
- `configparser`: A module used for handling configuration files, allowing the script to read settings from an `ini` file.
- `os`: A module for interacting with the operating system, used here to construct file paths.

## Configuration File Reading

```python
config = configparser.ConfigParser()
path = os.getcwd()
file_name = "config.ini"
config.read(os.path.join(path, file_name))
```

This section reads settings from a `config.ini` file located in the current working directory. The settings include dataset parameters and model configurations.

## Extracting Configuration Settings

```python
dataset_type = config['Dataset']['DatasetType']
n = int(config['Dataset']['nPoints'])
n_train = int(config['Dataset']['nTrain'])
n_test = int(config['Dataset']['nTest'])
noise = float(config['Dataset']['noise'])

model_type = config['Model']['ModelType']
degree = int(config['Model']['degree'])
degrees = config['Model']['degrees']
loss = config['Model']['loss']
prediction_index = float(config['Model']['Prediction'])
input_index = prediction_index * n
```

This part extracts various configuration settings:

- Dataset parameters such as type, number of points, number of training and test points, and noise level.
- Model parameters including the type, polynomial degree for fitting, a list of degrees for validation, the loss function, and indices for prediction and input.

## Initializing the Model

```python
model = Polynomial_curve_fitting_model(degree, n, n_train, noise)
```

An instance of `Polynomial_curve_fitting_model` is created with specified degree, total number of points, number of training points, and noise level.

## Data Preparation

```python
x_train, y_train = model.create(n_train, noise)
x, y = model.original(n)
```

Two datasets are prepared:

- A training dataset with noise added.
- The original dataset without noise.

## Pre-Training Plot

```python
model.plot_before_train(x, y, x_train, y_train)
```

A visualization of the dataset before training, showing both the noisy training data and the original data.

## Model Training

```python
regression_mat, coeffs = model.fit(x_train, y_train, degree)
```

The model is trained using the noisy training data, fitting it to a polynomial of the specified degree.

## Post-Training Plot

```python
model.plot_after_train(x, y, x_train, y_train, coeffs, degree)
```

After training, the fitted polynomial curve is visualized alongside the original and noisy datasets.

## Model Validation

```python
d, train_errors, test_errors = model.validate(degrees, x, y, x_train, y_train, n, n_train, n_test, noise)
```

The model undergoes validation to assess its performance across different polynomial degrees. It calculates training and test errors for each degree.

## Validation Results Plot

```python
model.plot_validation_metrics(d, train_errors, test_errors)
```

Finally, the script visualizes the validation results, plotting the training and test errors to help in assessing the model's performance and selecting the optimal polynomial degree.
