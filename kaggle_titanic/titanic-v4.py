import pandas as pd
import os
from sklearn import neighbors, model_selection, preprocessing

dir = 'E:/'
titanic_train = pd.read_csv(os.path.join(dir, 'train.csv'))
print(titanic_train.info())
print(titanic_train.columns)

lencoder = preprocessing.LabelEncoder()
lencoder.fit(titanic_train['Sex'])
print(lencoder.classes_)
titanic_train['Sex_encoded'] = lencoder.transform(titanic_train['Sex'])

imputer = preprocessing.Imputer()
imputer.fit(titanic_train[['Age']])
print(imputer.statistics_)
titanic_train['Age_imputed'] = imputer.transform(titanic_train[['Age']])

features = ['SibSp', 'Parch', 'Pclass', 'Sex_encoded', 'Age_imputed']
X = titanic_train[ features ]
y = titanic_train['Survived']

X_train, X_eval, y_train, y_eval = model_selection.train_test_split(X, y, test_size=0.1, random_state=1)

#grid search based model building
knn_estimator = neighbors.KNeighborsClassifier()
knn_grid = {'n_neighbors': list(range(2,10)) }
knn_grid_estimator = model_selection.GridSearchCV(knn_estimator, knn_grid, scoring='accuracy', cv=10)
knn_grid_estimator.fit(X_train, y_train)
print(knn_grid_estimator.best_params_)
print(knn_grid_estimator.best_score_)
print(knn_grid_estimator.score(X_train, y_train))

print(knn_grid_estimator.score(X_eval, y_eval))

#visualize the deciion tree
dot_data = io.StringIO() 
tree.export_graphviz(dt_grid_estimator.best_estimator_, out_file = dot_data, feature_names = X_train.columns)
graph = pydot.graph_from_dot_data(dot_data.getvalue())[0] 
dir = 'E:/'
graph.write_pdf(os.path.join(dir, "tree4.pdf"))

titanic_test = pd.read_csv(os.path.join(dir, 'test.csv'))
print(titanic_test.info())

titanic_test['Sex_encoded'] = lencoder.transform(titanic_test['Sex'])
titanic_test['Age_imputed'] = imputer.transform(titanic_test[['Age']])

X_test = titanic_test[features]
titanic_test['Survived'] = dt_grid_estimator.best_estimator_.predict(X_test)
titanic_test.to_csv(os.path.join(dir, 'submission.csv'), columns=['PassengerId', 'Survived'], index=False)
