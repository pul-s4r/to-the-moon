# https://towardsdatascience.com/getting-rich-quick-with-machine-learning-and-stock-market-predictions-696802da94fe
# Simple prediction model
# LSTM used
# API + key from https://www.alphavantage.co/
# API Key: 1PRBO66RYM7SV7B9

from alpha_vantage.timeseries import TimeSeries
import numpy as np
np.random.seed(4)
import pandas as pd
from sklearn import preprocessing
import keras
import tensorflow as tf
from keras.models import Model
from keras.layers import Dense, Dropout, LSTM, Input, Activation, concatenate
from keras import optimizers


api_key = '1PRBO66RYM7SV7B9'
history_points = 30

def save_dataset(company):
    '''
    Implemented because Alpha Vantage doesn't let you save datasets that often
    Return: path to .csv file
    '''
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily_adjusted(company, outputsize='full')
    data.to_csv(f'./{company}_daily.csv')
    return f'./{company}_daily.csv'


def csv_to_dataset(csv_path):
    '''
    Convert all .csv data into a pandas dataset
    Return:
    ohlcv_histories
    next_day_open_values
    next_day_open_values_unscaled
    y_normaliser
    '''
    data = pd.read_csv(csv_path)
    # actual date is unnecessary
    data.drop('date', axis=1, inplace=True)
    # first day is unnecessarily inflated
    data.drop(0, axis=0, inplace=True)
    # put all data on a scale from 0-1
    normaliser = preprocessing.MinMaxScaler()
    data_normalised = normaliser.fit_transform(data)
    ohlcv_histories_normalised = np.array([data_normalised[i  : i + history_points].copy() for i in range(len(data_normalised) - history_points)])
    next_day_open_values_normalised = np.array([data_normalised[:,0][i + history_points].copy() for i in range(len(data_normalised) - history_points)])
    print(f'next_day_open_values_normalised.shape = {next_day_open_values_normalised.shape}')
    next_day_open_values_normalised = np.expand_dims(next_day_open_values_normalised, -1)
    print(f'next_day_open_values_normalised.shape = {next_day_open_values_normalised.shape}')

    next_day_open_values = np.array([data.iloc[:,0][i + history_points].copy() for i in range(len(data) - history_points)])
    next_day_open_values = np.expand_dims(next_day_open_values_normalised, -1)

    y_normaliser = preprocessing.MinMaxScaler()
    y_normaliser.fit(np.expand_dims(next_day_open_values, -1))

    assert ohlcv_histories_normalised.shape[0] == next_day_open_values_normalised.shape[0]
    return ohlcv_histories_normalised, next_day_open_values_normalised, next_day_open_values, y_normaliser


def split_data(array, train):
    n = int(array.shape[0] * train)
    return array[:n], array[n:]


x, y, y_unscaled, y_normaliser = csv_to_dataset('AMZN_daily.csv')

train_split = 0.9
x_train, x_test = split_data(x, train_split)
y_train, y_test = split_data(y, train_split)
_, y_unscaled_test = split_data(y_unscaled, train_split)

lstm_input = Input(shape=(history_points, 5))
x = LSTM(50)(lstm_input)
x = Dropout(0.2)(x)
x = Dense(64)(x)
x = Activation('sigmoid')(x)
x = Dense(1)(x)
output = Activation('linear')(x)
model = Model(inputs=lstm_input, outputs=output)

adam = optimizers.Adam(lr=0.005)
model.compile(optimizer=adam, loss='mse')

model.fit(x=x_train, y=y_train, batch_size=32, epochs=50, shuffle=True, validation_split=0.1)
print(model.evaluate(x_test, y_test))
