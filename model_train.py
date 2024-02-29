from polynomial_fitting.Polynomial_curve_fitting import Polynomial_curve_fitting
import configparser
import os

config = configparser.ConfigParser()
path = os.getcwd()
file_name = "config.ini"
config.read(os.path.join(path, file_name))

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
input_index = prediction_index*n

model = Polynomial_curve_fitting(n, n_train, noise, degree, input_index)

x_train, y_train = model.create_dataset(n_train, noise)
x, y = model.original_sin_curve(n)
model.plot_before_train(x,y,x_train,y_train)

regression_mat, coeffs = model.poly_fit(x_train,y_train,degree)

model.plot_after_train(x,y,x_train,y_train,coeffs)