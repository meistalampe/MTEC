import collections
import sys
from os import system

from dtreeplt import dtreeplt
import graphviz
import pydotplus
from graphviz import render, Source
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import sklearn
import mglearn
from create_data_samples import *
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import MinMaxScaler, RobustScaler
from sklearn.neural_network import MLPClassifier

from empatica_data_extraction import*

# plt.style.use('ggplot')


def main():
    # ------------------- Create Datasets ------------------- #
    dataset_dicts = create_data_samples(repository_name='ClassificationRepository', folder_name='Datapoints')

    # divide each dataset in train and test sets
    for d in dataset_dicts:
        d['X_train'], d['X_test'], d['y_train'], d['y_test'] = \
            train_test_split(d['data'], d['target'], random_state=0, stratify=d['target'])

    # create sparse datasets
    for d in dataset_dicts:
        # bvp time features [0:15]
        d['X_train_bvp_time'] = d['X_train'][:, 0:16]
        d['X_test_bvp_time'] = d['X_test'][:, 0:16]
        # bvp frequency features [16:22]
        d['X_train_bvp_freq'] = d['X_train'][:, 16:23]
        d['X_test_bvp_freq'] = d['X_test'][:, 16:23]
        # bvp non linear features [23:25]
        d['X_train_bvp_nl'] = d['X_train'][:, 23:26]
        d['X_test_bvp_nl'] = d['X_test'][:, 23:26]
        # gsr moving average features [26:34]
        d['X_train_gsr_ma'] = d['X_train'][:, 26:35]
        d['X_test_gsr_ma'] = d['X_test'][:, 26:35]
        # gsr zero filtered features [35:43]
        d['X_train_gsr_zf'] = d['X_train'][:, 35:44]
        d['X_test_gsr_zf'] = d['X_test'][:, 35:44]
        # temp moving average features [44:52]
        d['X_train_temp_ma'] = d['X_train'][:, 44:53]
        d['X_test_temp_ma'] = d['X_test'][:, 44:53]
        # temp zero filtered features [53:61]
        d['X_train_temp_zf'] = d['X_train'][:, 53:62]
        d['X_test_temp_zf'] = d['X_test'][:, 53:62]

        d['X_train_no_ma'] = np.concatenate((d['X_train_bvp_time'], d['X_train_bvp_freq'], d['X_train_bvp_nl'],
                                             d['X_train_gsr_zf'], d['X_train_temp_zf']), axis=1)
        d['X_test_no_ma'] = np.concatenate((d['X_test_bvp_time'], d['X_test_bvp_freq'], d['X_test_bvp_nl'],
                                            d['X_test_gsr_zf'], d['X_test_temp_zf']), axis=1)
        d['X_train_no_zf'] = np.concatenate((d['X_train_bvp_time'], d['X_train_bvp_freq'], d['X_train_bvp_nl'],
                                             d['X_train_gsr_ma'], d['X_train_temp_ma']), axis=1)
        d['X_test_no_zf'] = np.concatenate((d['X_test_bvp_time'], d['X_test_bvp_freq'], d['X_test_bvp_nl'],
                                            d['X_test_gsr_ma'], d['X_test_temp_ma']), axis=1)

    # ------------------- Data Visualisation ------------------- #

    # # create a DataFrame of x_train
    # # use feature names as column headlines
    # dataframe = pd.DataFrame(x_train, columns=dataset_default['feature_names'])
    # dataframe['species'] = y_train
    # # create a matrix for scatter plots of the DataFrame
    # # color according to y_train
    # # grr = scatter_matrix(dataframe, alpha=0.8)
    # # iris = datasets.load_iris()
    # # iris_df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
    # # iris_df['species'] = iris['target']
    #
    # grr = pd.plotting.scatter_matrix(dataframe, c=y_train, alpha=0.8, figsize=(15, 15), marker='0',
    #                                  hist_kwds={'bins': 20}, s=60, cmap=mglearn.cm3)
    # plt.show()

    # 2-feature scatter plot
    # feature_one = x_train[:, 0]
    # feature_two = x_train[:, 1]
    # y = y_train_bin
    # mglearn.discrete_scatter(feature_one, feature_two, y)
    # # for bin
    # plt.legend(["Category 0", "Category 1"], loc=4)
    # # for all
    # # plt.legend(["Category 0", "Category 1", "Category 2", "Category 3"], loc=4)
    # plt.xlabel("First Feature")
    # plt.ylabel("Second Feature")
    # plt.show()

    # ------------------- kNN Classifier ------------------- #
    # kNN_results = list([])
    # appendix = ''
    # for d in dataset_dicts:
    #     train_data = d['X_train' + appendix]
    #     train_labels = d['y_train']
    #     test_data = d['X_test' + appendix]
    #     test_labels = d['y_test']
    #
    #     for i in range(len(train_data)):
    #         if i > 0:
    #             knn = KNeighborsClassifier(n_neighbors=i)
    #             knn.fit(train_data, train_labels)
    #             y_pred = knn.predict(test_data)
    #             # print('Dataset: {}'.format(d['name']))
    #             # print('kNN with {} Neighbors.'.format(i))
    #             # print('Prediction Test Data:\n {}'.format(y_pred))
    #             # print('Accuracy Test Data: {:.2f}'.format(np.mean(y_pred == test_labels)))
    #             # print()
    #             kNN_results.append(['Dataset: {}'.format(d['name']), 'Number of Neighbors: {}'.format(i),
    #                                 'Accuracy Test Data: {:.2f}'.format(np.mean(y_pred == test_labels)),
    #                                 'Prediction Test Data: {}'.format(y_pred)])
    #     kNN_results.append(['Test Data: {}'.format(test_labels)])
    #     kNN_results.append([])
    #
    # write_to_text_file(file_name='kNN Results', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=kNN_results)

    # Visual representation of decision boundaries in 2-dim X_train
    # # set number of neighbors
    # n_neighbors = 2
    # # slice by using a two-dim dataset_default
    # X = x_train[:, :2]
    # X_test = x_test[:, :2]
    # y = y_train_bin
    # # set step size for mesh
    # h = 1
    # # create color maps
    # cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    # cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    #
    # for weights in ['uniform', 'distance']:
    #     # we create an instance of Neighbours Classifier and fit the data.
    #     clf = KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights)
    #     clf.fit(X, y)
    #
    #     # predict
    #     y_pred = clf.predict(X_test)
    #     print('kNN mit {} Nachbarn und Gewichtstyp: {}.'.format(n_neighbors, weights))
    #     print('Vorhersagen für den Testdatensatz:\n {}'.format(y_pred))
    #     print('Genauigkeit für den Testdatensatz: {:.2f}'.format(np.mean(y_pred == y_test_bin)))
    #     print()
    #     # Plot the decision boundary. For that, we will assign a color to each
    #     # point in the mesh [x_min, x_max]x[y_min, y_max].
    #     x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    #     y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    #     xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
    #                          np.arange(y_min, y_max, h))
    #     Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    #
    #     # Put the result into a color plot
    #     Z = Z.reshape(xx.shape)
    #     plt.figure()
    #     plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    #
    #     # Plot also the training points
    #     plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
    #                 edgecolor='k', s=20)
    #     plt.xlim(xx.min(), xx.max())
    #     plt.ylim(yy.min(), yy.max())
    #     plt.title(str(len(np.unique(y))) + "-Class classification (k = %i, weights = '%s')"
    #               % (n_neighbors, weights))
    #
    # plt.show()

    # show training and test accuracy for different n_neighbor settings

    # neighbors_settings = range(1, 11)
    # for i in range(5, x_train.shape[1] - 1):
    #     x_train_i = x_train[:, i:i + 2]
    #     x_test_i = x_test[:, i:i + 2]
    #     training_accuracy = []
    #     training_accuracy_bin = []
    #     test_accuracy = []
    #     test_accuracy_bin = []
    #     for n_neighbors in neighbors_settings:
    #         clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    #         clf.fit(x_train_i, y_train)
    #         training_accuracy.append(clf.score(x_train_i, y_train))
    #         training_accuracy_bin.append(clf.score(x_train_i, y_train_bin))
    #         test_accuracy.append(clf.score(x_test_i, y_test))
    #         test_accuracy_bin.append(clf.score(x_test_i, y_test_bin))
    #
    #     plt.plot(neighbors_settings, training_accuracy, label="Accuracy Training Data")
    #     plt.plot(neighbors_settings, training_accuracy_bin, label="Accuracy Training Data (bin)")
    #     plt.plot(neighbors_settings, test_accuracy, label="Accuracy Test Data")
    #     plt.plot(neighbors_settings, test_accuracy_bin, label="Accuracy Test Data (bin)")
    #     plt.ylabel("Accuracy")
    #     plt.xlabel("n_neighbors")
    #     plt.legend()
    #     plt.show()

    # ------------------- linear Classifier ------------------- #

    # logreg_results = list([])
    # linear_svc_results = list([])
    # sgdc_results = list([])
    # appendix = ''
    # for d in dataset_dicts:
    #     train_data = d['X_train' + appendix]
    #     train_labels = d['y_train']
    #     test_data = d['X_test' + appendix]
    #     test_labels = d['y_test']
    #     for i in [0.001, 0.01, 0.1, 1, 10, 100, 1000]:
    #         # logistic regression
    #         logreg = LogisticRegression(C=i, penalty='l1').fit(train_data, train_labels)
    #         # print('C={}'.format(i))
    #         # print('Score for Training Data: {:.2f}'.format(logreg.score(train_data, train_labels)))
    #         # print('Score for Test Data: {:.2f}'.format(logreg.score(test_data, test_labels)))
    #         logreg_results.append(['Dataset: {}'.format(d['name']), 'alpha: {}'.format(i),
    #                                'Score Train Data: {:.2f}'.format(logreg.score(train_data, train_labels)),
    #                                'Score Test Data: {:.2f}'.format(logreg.score(test_data, test_labels))])
    #         # linear SVC, SGDC
    #         linear_svc = LinearSVC(penalty="l1", C=i, dual=False).fit(train_data, train_labels)
    #         # print('C={}'.format(i))
    #         # print('Score for Training Data: {:.2f}'.format(linear_svc.score(train_data, train_labels)))
    #         # print('Score for Test Data: {:.2f}'.format(linear_svc.score(test_data, test_labels)))
    #         linear_svc_results.append(['Dataset: {}'.format(d['name']), 'C: {}'.format(i),
    #                                    'Score Train Data: {:.2f}'.format(linear_svc.score(train_data, train_labels)),
    #                                    'Score Test Data: {:.2f}'.format(linear_svc.score(test_data, test_labels))])
    #
    #         linear_sgdc = SGDClassifier(alpha=i).fit(train_data, train_labels)
    #         # print('alpha={}'.format(i))
    #         # print('Score for Training Data: {:.2f}'.format(linear_sgdc.score(train_data, train_labels)))
    #         # print('Score for Test Data: {:.2f}'.format(linear_sgdc.score(test_data, test_labels)))
    #         sgdc_results.append(['Dataset: {}'.format(d['name']), 'alpha: {}'.format(i),
    #                              'Score Train Data: {:.2f}'.format(linear_sgdc.score(train_data, train_labels)),
    #                              'Score Test Data: {:.2f}'.format(linear_sgdc.score(test_data, test_labels))])
    #     logreg_results.append([])
    #     linear_svc_results.append([])
    #     sgdc_results.append([])
    #
    # write_to_text_file(file_name='logregResults_l1', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=logreg_results)
    # write_to_text_file(file_name='linearSVCResults_l1', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=linear_svc_results)
    # write_to_text_file(file_name='SGDCResults', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=sgdc_results)

    # ------------------- Gaussian Naive Bayes ------------------- #
    # gnb_results = list([])
    # appendix = ''
    # for d in dataset_dicts:
    #     train_data = d['X_train' + appendix]
    #     train_labels = d['y_train']
    #     test_data = d['X_test' + appendix]
    #     test_labels = d['y_test']
    #
    #     gnb = GaussianNB().fit(train_data, train_labels)
    #     # print('Score for Training Data: {:.2f}'.format(gnb.score(train_data, train_labels)))
    #     # print('Score for Test Data: {:.2f}'.format(gnb.score(test_data, test_labels)))
    #     gnb_results.append(['Dataset: {}'.format(d['name']),
    #                         'Score Train Data: {:.2f}'.format(gnb.score(train_data, train_labels)),
    #                         'Score Test Data: {:.2f}'.format(gnb.score(test_data, test_labels))])
    #     gnb_results.append([])
    #
    # write_to_text_file(file_name='gnbResults', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=gnb_results)

    # ------------------- Decision Trees ------------------- #

    # single decision tree

    # dt_results = list([])
    # appendix = ''
    # for d in dataset_dicts:
    #     train_data = d['X_train' + appendix]
    #     train_labels = d['y_train']
    #     test_data = d['X_test' + appendix]
    #     test_labels = d['y_test']
    #
    #     for md in range(10):
    #         if md > 0:
    #             dt = DecisionTreeClassifier(max_depth=md, random_state=0)
    #             dt.fit(train_data, train_labels)
    #
    #             # print('Score for Training Data: {:.2f}'.format(dt.score(train_data, train_labels)))
    #             # print('Score for Test Data: {:.2f}'.format(dt.score(test_data, test_labels)))
    #             dt_results.append(['Dataset: {}'.format(d['name']), 'Max_depth: {}'.format(md),
    #                                'Score Train Data: {:.2f}'.format(dt.score(train_data, train_labels)),
    #                                'Score Test Data: {:.2f}'.format(dt.score(test_data, test_labels))])
    #             # visualize trees
    #             # dtree = dtreeplt(
    #             #     model=dt,
    #             #     feature_names=d['feature_names'],
    #             #     target_names=d['target_names']
    #             # )
    #             # fig = dtree.view()
    #             # # if you want save figure, use savefig method in returned figure object.
    #             # fig.savefig('dt_{}_{}.png'.format(d['name'], str(md)))
    #
    #             # plot feature importance
    #             plot_feature_importance(dt, d)
    #     dt_results.append([])
    #
    # write_to_text_file(file_name='dtResults', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=dt_results)

    # random forest
    # dtrf_results = list([])
    # dtrf_mf_results = list([])
    # dtrf_md_results = list([])
    # dtrf_mf_md_results = list([])
    # appendix = ''
    # for d in dataset_dicts:
    #     train_data = d['X_train' + appendix]
    #     train_labels = d['y_train']
    #     test_data = d['X_test' + appendix]
    #     test_labels = d['y_test']
    #
    #     # influence number of estimators
    #     for e in [5, 25, 50, 100, 250, 500, 1000]:
    #         random_forest = RandomForestClassifier(n_estimators=e, random_state=0)
    #         random_forest.fit(train_data, train_labels)
    #         # print('Score for Training Data: {:.2f}'.format(random_forest.score(train_data, train_labels)))
    #         # print('Score for Test Data: {:.2f}'.format(random_forest.score(test_data, test_labels)))
    #         dtrf_results.append(['Dataset: {}'.format(d['name']), 'NumberOfEstimators: {}'.format(e),
    #                              'MaxDepth: {}'.format(random_forest.max_depth),
    #                              'Score Train Data: {:.2f}'.format(random_forest.score(train_data, train_labels)),
    #                              'Score Test Data: {:.2f}'.format(random_forest.score(test_data, test_labels))])
    #
    #         # show feature importance
    #         # plot_feature_importance_random_forest(random_forest, d)
    #
    #     # influence max features
    #     for e in [5, 25, 50, 100, 250, 500, 1000]:
    #         for mf in [15, 30, len(d['feature_names'])]:
    #             # random_forest = RandomForestClassifier(n_estimators=e, max_depth=md, random_state=0)
    #             random_forest = RandomForestClassifier(n_estimators=e, max_features=mf, random_state=0)
    #             random_forest.fit(train_data, train_labels)
    #             # print('Score for Training Data: {:.2f}'.format(random_forest.score(train_data, train_labels)))
    #             # print('Score for Test Data: {:.2f}'.format(random_forest.score(test_data, test_labels)))
    #             dtrf_mf_results.append(['Dataset: {}'.format(d['name']), 'NumberOfEstimators: {}'.format(e),
    #                                     'MaxFeatures: {}'.format(mf),
    #                                     'Score Train Data: {:.2f}'.format(random_forest.score(train_data, train_labels)),
    #                                     'Score Test Data: {:.2f}'.format(random_forest.score(test_data, test_labels))])
    #
    #         # show feature importance
    #         # plot_feature_importance_random_forest(random_forest, d)
    #     # influence max depth
    #     for e in [5, 25, 50, 100, 250, 500, 1000]:
    #         for md in range(6):
    #             if md > 0:
    #                 # random_forest = RandomForestClassifier(n_estimators=e, max_depth=md, random_state=0)
    #                 random_forest = RandomForestClassifier(n_estimators=e, max_depth=md, random_state=0)
    #                 random_forest.fit(train_data, train_labels)
    #                 # print('Score for Training Data: {:.2f}'.format(random_forest.score(train_data, train_labels)))
    #                 # print('Score for Test Data: {:.2f}'.format(random_forest.score(test_data, test_labels)))
    #                 dtrf_md_results.append(['Dataset: {}'.format(d['name']), 'NumberOfEstimators: {}'.format(e),
    #                                         'MaxDepth: {}'.format(md),
    #                                         'Score Train Data: {:.2f}'.format(random_forest.score(train_data, train_labels)),
    #                                         'Score Test Data: {:.2f}'.format(random_forest.score(test_data, test_labels))])
    #
    #                 # show feature importance
    #                 # plot_feature_importance_random_forest(random_forest, d)
    #
    #     dtrf_results.append([])
    #     dtrf_mf_results.append([])
    #     dtrf_md_results.append([])
    #
    # write_to_text_file(file_name='dtrfResults', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=dtrf_results)
    # write_to_text_file(file_name='dtrf_mf_Results', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=dtrf_mf_results)
    # write_to_text_file(file_name='dtrf_md_Results', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=dtrf_md_results)

    # gradient boosting
    # gbrt_results = list([])
    # gbrt_1000_results = list([])
    # gbrt_2000_results = list([])
    # gbrt_10000_results = list([])
    # appendix = ''
    # for d in dataset_dicts:
    #     train_data = d['X_train' + appendix]
    #     train_labels = d['y_train']
    #     test_data = d['X_test' + appendix]
    #     test_labels = d['y_test']
    #     for md in range(5):
    #         if md > 0:
    #             for lr in [0.1, 0.05, 0.01, 0.005, 0.0025, 0.0015, 0.001]:
    #                 gbrt = GradientBoostingClassifier(random_state=0, max_depth=md, learning_rate=lr)
    #                 # gbrt = GradientBoostingClassifier(n_estimators=1000, random_state=0, max_depth=md, learning_rate=lr)
    #                 # gbrt = GradientBoostingClassifier(n_estimators=2000, random_state=0, max_depth=md, learning_rate=lr)
    #                 # gbrt = GradientBoostingClassifier(n_estimators=10000, random_state=0, max_depth=md, learning_rate=lr)
    #                 gbrt.fit(train_data, train_labels)
    #                 # print('Score for Training Data: {:.2f}'.format(gbrt.score(train_data, train_labels)))
    #                 # print('Score for Test Data: {:.2f}'.format(gbrt.score(test_data, test_labels)))
    #                 gbrt_results.append(
    #                     ['Dataset: {}'.format(d['name']), 'NumberOfEstimators: {}'.format(gbrt.n_estimators),
    #                      'MaxDepth: {}'.format(gbrt.max_depth),
    #                      'LearningRate: {}'.format(gbrt.learning_rate),
    #                      'Score Train Data: {:.3f}'.format(gbrt.score(train_data, train_labels)),
    #                      'Score Test Data: {:.3f}'.format(gbrt.score(test_data, test_labels))])
    #                 # gbrt_1000_results.append(
    #                 #     ['Dataset: {}'.format(d['name']), 'NumberOfEstimators: {}'.format(gbrt.n_estimators),
    #                 #      'MaxDepth: {}'.format(gbrt.max_depth),
    #                 #      'LearningRate: {}'.format(gbrt.learning_rate),
    #                 #      'Score Train Data: {:.3f}'.format(gbrt.score(train_data, train_labels)),
    #                 #      'Score Test Data: {:.3f}'.format(gbrt.score(test_data, test_labels))])
    #                 # gbrt_2000_results.append(
    #                 #     ['Dataset: {}'.format(d['name']), 'NumberOfEstimators: {}'.format(gbrt.n_estimators),
    #                 #      'MaxDepth: {}'.format(gbrt.max_depth),
    #                 #      'LearningRate: {}'.format(gbrt.learning_rate),
    #                 #      'Score Train Data: {:.3f}'.format(gbrt.score(train_data, train_labels)),
    #                 #      'Score Test Data: {:.3f}'.format(gbrt.score(test_data, test_labels))])
    #                 # gbrt_10000_results.append(
    #                 #     ['Dataset: {}'.format(d['name']), 'NumberOfEstimators: {}'.format(gbrt.n_estimators),
    #                 #      'MaxDepth: {}'.format(gbrt.max_depth),
    #                 #      'LearningRate: {}'.format(gbrt.learning_rate),
    #                 #      'Score Train Data: {:.3f}'.format(gbrt.score(train_data, train_labels)),
    #                 #      'Score Test Data: {:.3f}'.format(gbrt.score(test_data, test_labels))])
    #
    #         # show feature importance
    #         # plot_feature_importance_gradient_boosting(gbrt, d)
    #     gbrt_results.append([])
    #     # gbrt_1000_results.append([])
    #     # gbrt_2000_results.append([])
    #     # gbrt_10000_results.append([])
    #
    # write_to_text_file(file_name='gbrtResults', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=gbrt_results)
    # # write_to_text_file(file_name='gbrt_1000_Results', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    # #                    data_list=gbrt_1000_results)
    # # write_to_text_file(file_name='gbrt_2000_Results', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    # #                    data_list=gbrt_2000_results)
    # # write_to_text_file(file_name='gbrt_10000_Results', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    # #                    data_list=gbrt_10000_results)

    # ------------------- SVM ------------------- #
    # svm_results = list([])
    # appendix = ''
    # for d in dataset_dicts:
    #     train_data = d['X_train' + appendix]
    #     train_labels = d['y_train']
    #     test_data = d['X_test' + appendix]
    #     test_labels = d['y_test']
    #     # Min Max Scaling
    #     scaler = MinMaxScaler()
    #     scaler.fit(train_data)
    #     # Transform Training Data
    #     train_data_min_max_scaled = scaler.transform(train_data)
    #     # Compare before after
    #     # print("Training Data:")
    #     # print("Minimum per Feature (prescaling): \n {}".format(train_data.min(axis=0)))
    #     # print("Maximum per Feature (prescaling): \n {}".format(train_data.max(axis=0)))
    #     # print("Minimum per Feature (postscaling): \n {}".format(train_data_min_max_scaled.min(axis=0)))
    #     # print("Maximum per Feature (postscaling): \n {}".format(train_data_min_max_scaled.max(axis=0)))
    #     # Transform Training Data
    #     test_data_min_max_scaled = scaler.transform(test_data)
    #     # Compare before after
    #     # print("Test Data:")
    #     # print("Minimum per Feature (prescaling): \n {}".format(test_data.min(axis=0)))
    #     # print("Maximum per Feature (prescaling): \n {}".format(test_data.max(axis=0)))
    #     # print("Minimum per Feature (postscaling): \n {}".format(test_data_min_max_scaled.min(axis=0)))
    #     # print("Maximum per Feature (postscaling): \n {}".format(test_data_min_max_scaled.max(axis=0)))
    #     for c in [1000, 750, 500, 250, 100, 50, 25, 10, 5, 3, 1, 0.1, 0.01, 0.001]:
    #         for y in [0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]:
    #             svc = SVC(kernel='rbf', C=c, gamma=y, random_state=0)
    #             svc.fit(train_data_min_max_scaled, train_labels)
    #             print('Score for Training Data: {:.3f}'.format(svc.score(train_data_min_max_scaled, train_labels)))
    #             print('Score for Test Data: {:.3f}'.format(svc.score(test_data_min_max_scaled, test_labels)))
    #             svm_results.append(
    #                 ['Dataset: {}'.format(d['name']),
    #                  'C: {}'.format(c),
    #                  'Gamma: {}'.format(y),
    #                  'Score Train Data: {:.3f}'.format(svc.score(train_data_min_max_scaled, train_labels)),
    #                  'Score Test Data: {:.3f}'.format(svc.score(test_data_min_max_scaled, test_labels))])
    #     svm_results.append([])
    #
    # write_to_text_file(file_name='svm_Results', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=svm_results)

    # ------------------- Neural Networks ------------------- #
    mlp_results = list([])
    appendix = ''
    for d in dataset_dicts:
        train_data = d['X_train' + appendix]
        train_labels = d['y_train']
        test_data = d['X_test' + appendix]
        test_labels = d['y_test']

        scaler = MinMaxScaler()
        scaler.fit(train_data)
        # Transform Training Data
        train_data_min_max_scaled = scaler.transform(train_data)
        # Compare before after
        # print("Training Data:")
        # print("Minimum per Feature (prescaling): \n {}".format(train_data.min(axis=0)))
        # print("Maximum per Feature (prescaling): \n {}".format(train_data.max(axis=0)))
        # print("Minimum per Feature (postscaling): \n {}".format(train_data_min_max_scaled.min(axis=0)))
        # print("Maximum per Feature (postscaling): \n {}".format(train_data_min_max_scaled.max(axis=0)))
        # Transform Training Data
        test_data_min_max_scaled = scaler.transform(test_data)
        # Compare before after
        # print("Test Data:")
        # print("Minimum per Feature (prescaling): \n {}".format(test_data.min(axis=0)))
        # print("Maximum per Feature (prescaling): \n {}".format(test_data.max(axis=0)))
        # print("Minimum per Feature (postscaling): \n {}".format(test_data_min_max_scaled.min(axis=0)))
        # print("Maximum per Feature (postscaling): \n {}".format(test_data_min_max_scaled.max(axis=0)))
        for n_hidden_layers in [1, 2, 3, 4]:
            for n_hidden_nodes in [2, 3, 5, 10, 15, 25, 50, 62, 75, 100]:
                for a in [0.00001, 0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1]:
                    set_scale = [n_hidden_nodes] * n_hidden_layers
                    mlp = MLPClassifier(solver='lbfgs', activation='tanh', alpha=a, random_state=0, hidden_layer_sizes=set_scale)
                    mlp.fit(train_data_min_max_scaled, train_labels)
                    # print('Score for Training Data: {:.3f}'.format(mlp.score(train_data_min_max_scaled, train_labels)))
                    # print('Score for Test Data: {:.3f}'.format(mlp.score(test_data_min_max_scaled, test_labels)))
                    mlp_results.append(
                        ['Dataset: {}'.format(d['name']),
                         'n_hidden_layers: {}'.format(n_hidden_layers),
                         'n_hidden_nodes: {}'.format(n_hidden_nodes),
                         'alpha: {}'.format(a),
                         'Score Train Data: {:.3f}'.format(mlp.score(train_data_min_max_scaled, train_labels)),
                         'Score Test Data: {:.3f}'.format(mlp.score(test_data_min_max_scaled, test_labels))])

        mlp_results.append([])
    write_to_text_file(file_name='mlp_Results_tanh', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
                       data_list=mlp_results)


def plot_feature_importance_tree(model: DecisionTreeClassifier, dataset: dict):
    n_features = np.size(dataset['data'], 1)
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), dataset['feature_names'])
    plt.title("Dataset: {}, max_depth: {}".format(dataset['name'], model.max_depth))
    plt.xlabel("Feature Importance")
    plt.ylabel("Feature")
    plt.savefig("Tree_{}_{}.png".format(dataset['name'], model.max_depth))
    # plt.show()


def plot_feature_importance_random_forest(model: RandomForestClassifier, dataset: dict):
    n_features = np.size(dataset['data'], 1)
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), dataset['feature_names'])
    plt.title("Dataset: {}, n_estimators: {}, max_depth: {}, max_features: {}".format(dataset['name'],
                                                                                      model.n_estimators,
                                                                                      model.max_depth,
                                                                                      model.max_features))
    plt.xlabel("Feature Importance")
    plt.ylabel("Feature")
    plt.savefig("Tree_{}_n{}_md{}_mf{}.png".format(dataset['name'], model.n_estimators, model.max_depth,
                                                   model.max_features))
    # plt.show()


def plot_feature_importance_gradient_boosting(model: GradientBoostingClassifier, dataset: dict):
    n_features = np.size(dataset['data'], 1)
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), dataset['feature_names'])
    plt.title("Dataset: {}, n_estimators: {}, max_depth: {}, learning_rate: {}".format(dataset['name'],
                                                                                       model.n_estimators,
                                                                                       model.max_depth,
                                                                                       model.learning_rate))
    plt.xlabel("Feature Importance")
    plt.ylabel("Feature")
    plt.savefig("Tree_{}_n{}_md{}_lr{}.png".format(dataset['name'], model.n_estimators, model.max_depth,
                                                   model.learning_rate))
    plt.show()


if __name__ == '__main__':
    main()
