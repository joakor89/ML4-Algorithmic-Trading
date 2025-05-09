from sklearn.model_selection import (train_test_split,
                                     KFold,
                                     LeaveOneOut,
                                     LeavePOut,
                                     ShuffleSplit,
                                     TimeSeriesSplit)

data = list(range(1, 11))
print(data)

print(train_test_split(data, train_size=.8))

kf = KFold(n_splits=5)
for train, validate in kf.split(data):
    print(train, validate)

kf = KFold(n_splits=5, shuffle=True, random_state=42)
for train, validate in kf.split(data):
    print(train, validate)

loo = LeaveOneOut()
for train, validate in loo.split(data):
    print(train, validate)

lpo = LeavePOut(p=2)
for train, validate in lpo.split(data):
    print(train, validate)

ss = ShuffleSplit(n_splits=3, test_size=2, random_state=0)
for train, validate in ss.split(data):
    print(train, validate)

tscv = TimeSeriesSplit(n_splits=5)
for train, validate in tscv.split(data):
    print(train, validate)