

from skmultiflow.data import WaveformGenerator
from skmultiflow.lazy.knn import KNN
from skmultiflow.evaluation import EvaluatePrequential

n_neighbors     = 8
max_window_size = 2000
leaf_size       = 30
n_estimators    = 30
show_plot       = True
pretrain_size   = 100
max_samples     = 10000
metrics         = ['accuracy']

stream = WaveformGenerator()
stream.prepare_for_use()
mdl = KNN(n_neighbors=n_neighbors, max_window_size=max_window_size, leaf_size=leaf_size)
evaluator = EvaluatePrequential(show_plot=show_plot, pretrain_size=pretrain_size, max_samples=max_samples, metrics=metrics)
evaluator.evaluate(stream=stream, model=mdl)

