from ngboost.ngboost import NGBoost
import ngboost
from ngboost import NGBClassifier
from ngboost.distns import Bernoulli
from ngboost.learners import default_tree_learner
from ngboost.scores import MLE  # �����Ȼ����
from ngboost.distns import Normal
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV  # ����ʲô����ѧϰ������õ�


model1 = NGBClassifier(Base=default_tree_learner, Dist=Bernoulli, Score=MLE, verbose=True)

data1 = pd.read_csv(r'd:\\a-data.csv')

X = data1.drop('isFraud', axis=1)
Y = data1['isFraud']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
param_grid = {
    'n_estimators': [20, 50],
    'minibatch_frac': [1.0, 0.5],
}
# ngb = NGBoost(Base=default_tree_learner, Dist=Normal, Score=MLE(), natural_gradient=True, verbose=False)
## ���


# ���������� test Mean Squared Error
# test_MSE = mean_squared_error(Y_preds, Y_test)
# print('Test MSE', test_MSE)
# ���鸺������Ȼtest Negative Log Likelihood
# test_NLL = -Y_dists.logpdf(Y_test.flatten()).mean()
# print('Test NLL', test_NLL)
# learning_rate=[0.0001,0.001,0.01,0.1,0.2,0.3]
# param_grid=dict(learning_rate=learning_rate)
# kfold=StratifiedKFold(n_splits=10,shuffle=True,random_state=7)
# grid_seach=GridSearchCV(model1,param_grid,scoring="neg_log_loss",n_jobs=-1,cv=kfold)
# grid_result=grid_seach.fit(X,Y)

# summarize results
# print("BEST:%f using %s" %(grid_seach.best_score_,grid_result))   #best_params_û����?
# means=grid_result.cv_results_['mean_test_score']
# params=grid_result.cv_results_['params']
# for mean,param in zip(means,params):
# print("%f with: %r %(mean,param)")


# eval_set=[(X_test,Y_test)]#fit model no training data
model1.fit(X_train, Y_train)

# preds = model1.pred_dist(X_test)#�������ӻ�
y_train_pred = model1.predict(X_train.flatten()).mean()
y_test_pred = model1.predict(X_test.flatten()).mean()

# print("ROC:", roc_auc_score(Y_test, y_test_pred.prob))
# def cul_accuracy(y_true, y_pred, pos_label=1):
# return {"Accuracy": float("%.5f" % accuracy_score(Y_test=Y_test, y_test_pred=y_test_pred))

correct = np.sum(y_test_pred == Y_test)
print("%d out of %d prediction correct" % (correct, len(y_test_pred)))

# predictions = [round(value) for value in y_test_pred]
# y_pre = [round(item>0.8,2) for item in (y_test_pred)]

# accuracy = accuracy_score(Y_test,predictions)

print("Accuracy:%.2f%%" % (accuracy * 100))

grid_search = GridSearchCV(model1, param_grid=param_grid, cv=5)
grid_search.fit(X_train, Y_train)
print(grid_search.best_params_)
