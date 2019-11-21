import pandas as pd
import os
from sklearn import ensemble, model_selection

dir = 'E:/'
titanic_train = pd.read_csv(os.path.join(dir, 'train.csv'))
print(titanic_train.info())
print(titanic_train.columns)

X_train = titanic_train[ ['SibSp', 'Parch'] ]
y_train = titanic_train['Survived']
rf_estimator = ensemble.RandomForestClassifier()
rf_estimator.fit(X_train, y_train)
model_selection.cross_val_score(rf_estimator, X_train, y_train, scoring="accuracy", cv=5).mean()

titanic_test = pd.read_csv(os.path.join(dir, 'test.csv'))
print(titanic_test.info())
X_test = titanic_test[ ['SibSp', 'Parch'] ]
titanic_test['Survived'] = rf_estimator.predict(X_test)
titanic_test.to_csv(os.path.join(dir, 'submission.csv'), columns=['PassengerId', 'Survived'], index=False)
