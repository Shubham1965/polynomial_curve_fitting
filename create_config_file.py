import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {}
config['Dataset'] = {'DatasetType': 'toy',  #toy
                     'nPoints': '1000', #Visualize the actual data
                     'nTrain' : '20', #For creating training data
                     'nTest': '100', #For creating test data
                     'noise' : '0.1', #For creating training and test data
                     }

config['Model'] = {'ModelType': 'poly',  # {FCNN, CNN, LSTM, poly, RNN}
                   'degree' : '9', #Model parameter
                   'degrees' : '[1,2,3,4,5,6,7,8,9]', #For validation against different models
                   'Loss': 'RMS', #For validation against the training and test errors, MAE, MAPE, R2, etc.. 
                   'Prediction': '0.5', #index for prediction from the trained model
                   }

if config['Model']['ModelType'] == 'poly':
  config['poly'] = {'ModelType': 'poly',  # {FCNN, CNN, LSTM, poly, RNN}
                   'degree' : '9', #Model parameter
                   'degrees' : '[1,2,3,4,5,6,7,8,9]', #For validation against different models
                   'Loss': 'RMS', #For validation against the training and test errors, MAE, MAPE, R2, etc.. 
                   'Prediction': '0.5', #index for prediction from the trained model
                   }
elif config['Model']['ModelType'] == 'LSTM':
  config['LSTM'] = {'ModelType': 'poly',  # {FCNN, CNN, LSTM, poly, RNN}
                  'degree' : '9', #Model parameter
                  'degrees' : '[1,2,3,4,5,6,7,8,9]', #For validation against different models
                  'Loss': 'RMS', #For validation against the training and test errors, MAE, MAPE, R2, etc.. 
                  'Prediction': '0.5', #index for prediction from the trained model
                  }

config['XAI'] = {}

config['HPO'] = {
                'Status': False
}

with open('config.ini', 'w') as configfile:
  config.write(configfile)