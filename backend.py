#imports
from sklearn.neural_network import MLPClassifier

def run_neural(df, df_target):
    data = df.values
    target = df_target.values
    
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(X, y)