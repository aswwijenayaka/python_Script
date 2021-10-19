import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import plot_confusion_matrix

df = pd.read_csv('new3.csv')
loanmodel = model = KNeighborsClassifier(n_neighbors=15)

X = df[['emp_length_int', 'home_ownership_cat', 'annual_inc', 'loan_amount',
        'term_cat', 'application_type_cat', 'purpose_cat', 'interest_payment_cat', 'interest_rate',
        'grade_cat', 'dti', 'total_pymnt', 'total_rec_prncp', 'installment']]  # Features
y = df['loan_condition_cat']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7)

print("Training in Process.....")
loanmodel.fit(X_train, y_train)  # training the model
y_pred = loanmodel.predict(X_test)

# evaluation
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))


from sklearn.metrics import plot_precision_recall_curve
import matplotlib.pyplot as plt

from sklearn.metrics import average_precision_score

average_precision = average_precision_score(y_test, y_pred)

print('Average precision-recall score: {0:0.2f}'.format(
    average_precision))

disp = plot_precision_recall_curve(loanmodel, X_test, y_test)
disp.ax_.set_title('2-class Precision-Recall curve: '
                   'AP={0:0.2f}'.format(average_precision))
plt.show()



