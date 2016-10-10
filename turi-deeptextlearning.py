# Kaggle Question

import graphlab as gl
gl.canvas.set_target('ipynb')

training_sframe = gl.SFrame.read_csv('/Users/kelinchristi/Documents/turi-data/train.csv', verbose=False)

features = ['datetime', 'season', 'holiday', 'workingday', 'weather',
            'temp', 'atemp', 'humidity', 'windspeed']

m = gl.boosted_trees_regression.create(training_sframe,
                                       features=features,
                                       target='count')

test_sframe = gl.SFrame.read_csv('/Users/kelinchristi/Documents/turi-data/test.csv', verbose=False)
prediction = m.predict(test_sframe)

def make_submission(prediction, filename='submission.txt'):
    with open(filename, 'w') as f:
        f.write('datetime,count\n')
        submission_strings = test_sframe['datetime'] + ',' + prediction.astype(str)
        for row in submission_strings:
            f.write(row + '\n')

make_submission(prediction, 'submission1.txt')

training_sframe.show()

date_format_str = '%Y-%m-%d %H:%M:%S'

def process_date_column(data_sframe):
    """Split the 'datetime' column of a given sframe"""
    datetime_col = data_sframe['datetime']
    parsed_datetime = datetime_col.str_to_datetime(date_format_str)
    parsed_datetime_sf = parsed_datetime.split_datetime(column_name_prefix='', limit=['year', 'month', 'day', 'hour'])
    for col in ['year', 'month', 'day', 'hour']:
        data_sframe[col] = parsed_datetime_sf[col]
    data_sframe['weekday'] = parsed_datetime.apply(lambda x: x.weekday())

process_date_column(training_sframe)
process_date_column(test_sframe)
import math

# Create three new columns: log-casual, log-registered, and log-count
for col in ['casual', 'registered', 'count']:
    training_sframe['log-' + col] = training_sframe[col].apply(lambda x: math.log(1 + x))
new_features = features + ['year', 'month', 'hour', 'weekday']
new_features.remove('datetime')

m1 = gl.boosted_trees_regression.create(training_sframe,
                                        features=new_features,
                                        target='log-casual')

m2 = gl.boosted_trees_regression.create(training_sframe,
                                        features=new_features,
                                        target='log-registered')

def fused_predict(m1, m2, test_sframe):
    """
    Fused the prediction of two separately trained models.
    The input models are trained in the log domain.
    Return the combine predictions in the original domain.
    """
    p1 = m1.predict(test_sframe).apply(lambda x: math.exp(x)-1)
    p2 = m2.predict(test_sframe).apply(lambda x: math.exp(x)-1)
    return (p1 + p2).apply(lambda x: x if x > 0 else 0)

prediction = fused_predict(m1, m2, test_sframe)
