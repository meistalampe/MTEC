import collections
import sys
from os import system

from dtreeplt import dtreeplt
import graphviz
import pydotplus
from graphviz import render, Source
import numpy as np
import pandas as pd
import openpyxl
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import sklearn
import mglearn
from sklearn.utils.multiclass import unique_labels

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
from sklearn.metrics import confusion_matrix, multilabel_confusion_matrix, f1_score, classification_report, \
    precision_recall_curve, average_precision_score, roc_auc_score, roc_curve
from empatica_data_extraction import*
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import LeaveOneOut
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

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
        d['X_train_gsr_ma'] = d['X_train'][:, 30:34]
        d['X_test_gsr_ma'] = d['X_test'][:, 30:34]
        # gsr zero filtered features [35:43]
        d['X_train_gsr_zf'] = d['X_train'][:, 39:43]
        d['X_test_gsr_zf'] = d['X_test'][:, 39:43]
        # temp moving average features [44:52]
        d['X_train_temp_ma'] = d['X_train'][:, 48:52]
        d['X_test_temp_ma'] = d['X_test'][:, 48:52]
        # temp zero filtered features [53:61]
        d['X_train_temp_zf'] = d['X_train'][:, 57:61]
        d['X_test_temp_zf'] = d['X_test'][:, 57:61]

        # feature selection
        bvp_test_selected = np.delete(d['X_test_bvp_time'], [5, 6, 8, 10, 11, 13, 14, 15], 1)
        bvp_train_selected = np.delete(d['X_train_bvp_time'], [5, 6, 8, 10, 11, 13, 14, 15], 1)

        gsr_test_selected = np.delete(d['X_test_gsr_zf'], [1], 1)
        gsr_test_selected[:, 0] = abs(d['X_test_gsr_zf'][:, 1] - d['X_test_gsr_zf'][:, 0])
        gsr_train_selected = np.delete(d['X_train_gsr_zf'], [1], 1)
        gsr_train_selected[:, 0] = abs(d['X_train_gsr_zf'][:, 1] - d['X_train_gsr_zf'][:, 0])

        temp_test_selected = np.delete(d['X_test_temp_zf'], [1], 1)
        temp_test_selected[:, 0] = abs(d['X_test_temp_zf'][:, 1] - d['X_test_temp_zf'][:, 0])
        temp_train_selected = np.delete(d['X_train_temp_zf'], [1], 1)
        temp_train_selected[:, 0] = abs(d['X_train_temp_zf'][:, 1] - d['X_train_temp_zf'][:, 0])
        # build feature sets
        # single sets
        # only bvp time
        d['X_test_bvp_time_only'] = bvp_test_selected
        d['X_train_bvp_time_only'] = bvp_train_selected
        # only bvp freq
        d['X_test_bvp_freq_only'] = d['X_test_bvp_freq']
        d['X_train_bvp_freq_only'] = d['X_train_bvp_freq']
        # only gsr
        d['X_test_gsr_only'] = gsr_test_selected
        d['X_train_gsr_only'] = gsr_train_selected
        # only temp
        d['X_test_temp_only'] = temp_test_selected
        d['X_train_temp_only'] = temp_train_selected

        # reduced sets
        # only contains statistical of bvp time, gsr, and temp
        d['X_test_red_time'] = np.concatenate((bvp_test_selected, gsr_test_selected, temp_test_selected), axis=1)
        d['X_train_red_time'] = np.concatenate((bvp_train_selected, gsr_train_selected, temp_train_selected)
                                               , axis=1)
        # only freq domain bvp
        # because task force suggest bvp freq domain only in short term analysis, gsr, and temp
        d['X_test_red_freq'] = np.concatenate((d['X_test_bvp_freq'], gsr_test_selected,  temp_test_selected)
                                              , axis=1)
        d['X_train_red_freq'] = np.concatenate((d['X_train_bvp_freq'], gsr_train_selected, temp_train_selected)
                                               , axis=1)
        # all features
        d['X_test_all'] = np.concatenate((bvp_test_selected, d['X_test_bvp_freq'], gsr_test_selected,
                                          temp_test_selected), axis=1)
        # print(len(d['X_test_all'][0]))
        d['X_train_all'] = np.concatenate((bvp_train_selected, d['X_train_bvp_freq'], gsr_train_selected,
                                           temp_train_selected), axis=1)

        # d['X_train_no_ma'] = np.concatenate((bvp_train_selected, d['X_train_bvp_freq'], d['X_train_bvp_nl'],
        #                                      d['X_train_gsr_zf'], d['X_train_temp_zf']), axis=1)
        # d['X_test_no_ma'] = np.concatenate((bvp_test_selected, d['X_test_bvp_freq'], d['X_test_bvp_nl'],
        #                                     d['X_test_gsr_zf'], d['X_test_temp_zf']), axis=1)
        # d['X_train_no_zf'] = np.concatenate((bvp_train_selected, d['X_train_bvp_freq'], d['X_train_bvp_nl'],
        #                                      d['X_train_gsr_ma'], d['X_train_temp_ma']), axis=1)
        # d['X_test_no_zf'] = np.concatenate((bvp_test_selected, d['X_test_bvp_freq'], d['X_test_bvp_nl'],
        #                                     d['X_test_gsr_ma'], d['X_test_temp_ma']), axis=1)
        # # only bvp features
        # d['X_test_bvp_only'] = np.concatenate((d['X_test_bvp_time'], d['X_test_bvp_freq'], d['X_test_bvp_nl']), axis=1)
        # d['X_train_bvp_only'] = np.concatenate((d['X_train_bvp_time'], d['X_train_bvp_freq'], d['X_train_bvp_nl']), axis=1)
        # only bvp, -cvsd, -cvnni, - geometrical features

        # d['X_test_bvp_sel_only'] = np.concatenate((bvp_test_selected, d['X_test_bvp_freq'], d['X_test_bvp_nl']), axis=1)
        # d['X_train_bvp_sel_only'] = np.concatenate((bvp_train_selected, d['X_train_bvp_freq'], d['X_train_bvp_nl']),
        #                                            axis=1)


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
    # mlp_results = list([])
    # appendix = ''
    # for d in dataset_dicts:
    #     train_data = d['X_train' + appendix]
    #     train_labels = d['y_train']
    #     test_data = d['X_test' + appendix]
    #     test_labels = d['y_test']
    #
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
    #     for n_hidden_layers in [1, 2, 3, 4]:
    #         for n_hidden_nodes in [2, 3, 5, 10, 15, 25, 50, 62, 75, 100]:
    #             for a in [0.00001, 0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1]:
    #                 set_scale = [n_hidden_nodes] * n_hidden_layers
    #                 mlp = MLPClassifier(solver='lbfgs', activation='tanh', alpha=a, random_state=0, hidden_layer_sizes=set_scale)
    #                 mlp.fit(train_data_min_max_scaled, train_labels)
    #                 # print('Score for Training Data: {:.3f}'.format(mlp.score(train_data_min_max_scaled, train_labels)))
    #                 # print('Score for Test Data: {:.3f}'.format(mlp.score(test_data_min_max_scaled, test_labels)))
    #                 mlp_results.append(
    #                     ['Dataset: {}'.format(d['name']),
    #                      'n_hidden_layers: {}'.format(n_hidden_layers),
    #                      'n_hidden_nodes: {}'.format(n_hidden_nodes),
    #                      'alpha: {}'.format(a),
    #                      'Score Train Data: {:.3f}'.format(mlp.score(train_data_min_max_scaled, train_labels)),
    #                      'Score Test Data: {:.3f}'.format(mlp.score(test_data_min_max_scaled, test_labels))])
    #
    #     mlp_results.append([])
    # write_to_text_file(file_name='mlp_Results_tanh', file_index=appendix, folder='MTEC\ClassificationRepository\Log',
    #                    data_list=mlp_results)
    # -------------------------------------------------------------- #
    # ------------------- Grid Search Validation ------------------- #
    # -------------------------------------------------------------- #

    # we split our data into a training and a test set
    # we reserve the test data for our final estimation and train and validate out models on the training data
    # using k-fold Cross Validation (S.250)
    # ------------------- LDA Classifier ------------------- #
    # param_grid = [{'solver': ['svd', 'lsqr', 'eigen']}]
    # appendices = ['_all', '_bvp_time_only', '_bvp_freq_only', '_gsr_only', '_temp_only', '_red_time', '_red_freq']
    # for k in [3, 5]:
    #     lda_appendices = list([])
    #     lda_datasets = list([])
    #     lda_cv = list([])
    #     lda_parameters = list([])
    #     lda_best_score_cv = list([])
    #     lda_test_accuracy = list([])
    #     lda_confusion_matrix = list([])
    #
    #     for a in appendices:
    #         appendix = a
    #         for d in dataset_dicts:
    #             train_data = d['X_train' + appendix]
    #             train_labels = d['y_train']
    #             test_data = d['X_test' + appendix]
    #             test_labels = d['y_test']
    #             # create model for rbf param grid
    #             lda_grid_search = GridSearchCV(LinearDiscriminantAnalysis(), param_grid, cv=k)
    #             # train model
    #             lda_grid_search.fit(train_data, train_labels)
    #             # transform results into a dataframe for plotting
    #             # results = pd.DataFrame(k_NN_grid_search.cv_results_)
    #
    #             # print('Best Parameters: {}'.format(k_NN_grid_search.best_params_))
    #             # print('Best Score Cross Validation: {:.3f}'.format(k_NN_grid_search.best_score_))
    #             # print('Accuracy Test Data: {:.3f}'.format(k_NN_grid_search.score(test_data, test_labels)))
    #             if len(d['target_names']) == 2:
    #                 # binary classifier
    #                 target_names = d['target_names']
    #                 # confusion matrix
    #                 cm = confusion_matrix(test_labels, lda_grid_search.predict(test_data))
    #                 cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
    #                                                  xticklabels=target_names, yticklabels=target_names,
    #                                                  cmap=plt.get_cmap("gray_r"), fmt="%d")
    #                 plt.title("Confusion Matrix: {}".format(d['name']))
    #                 plt.gca().invert_yaxis()
    #                 plt.colorbar(cm_image)
    #                 plt.savefig("lda_confusion_matrix_{}_{}_{}".format(d['name'], k, appendix))
    #                 plt.close()
    #                 # print("Confusion Matrix: \n{}".format(confusion))
    #                 # print('RightNegative: {}, FalseNegative: {}, RightPositive: {}, falsePositive: {}'.format(
    #                 #     confusion[0, 0], confusion[1, 0], confusion[1, 1], confusion[0, 1]))
    #
    #                 # f1 score
    #                 # f1 = f1_score(test_labels, k_NN_grid_search.predict(test_data))
    #                 # print('F1-Score: {:.2f}'.format(f1_score(test_labels, dt_grid_search.predict(test_data))))
    #                 # classification report
    #                 # cr = classification_report(test_labels, k_NN_grid_search.predict(test_data),
    #                 #                            target_names=target_names)
    #                 # print(classification_report(test_labels, k_NN_grid_search.predict(test_data),
    #                 #                             target_names=d['target_names']))
    #
    #                 # # precision recall curve
    #                 # precision, recall, thresholds = \
    #                 #     precision_recall_curve(test_labels, k_NN_grid_search.decision_function(test_data))
    #                 # # find threshold closest to 0
    #                 # close_zero = np.argmin(np.abs(thresholds))
    #                 # plt.plot(precision[close_zero], recall[close_zero], 'o', markersize=10, label="threshold zero",
    #                 #          fillstyle="none", c='k', mew=2)
    #                 # plt.plot(precision, recall, label="precision recall curve")
    #                 # plt.xlabel("Precision (Relevanz)")
    #                 # plt.ylabel("Recall (Sensitivität)")
    #                 # plt.legend(loc='best')
    #                 # plt.savefig("k_NN_prc_{}_{}".format(d['name'], k))
    #                 # plt.close()
    #                 # # average precision score
    #                 # avps = average_precision_score(test_labels, k_NN_grid_search.decision_function(test_data))
    #                 # # print("Average Precision (Relevanz): {}".format(avps))
    #                 # # ROC curve
    #                 # fpr, tpr, thresholds_roc = roc_curve(test_labels, k_NN_grid_search.decision_function(test_data))
    #                 # plt.plot(fpr, tpr, label="ROC Curve")
    #                 # plt.xlabel("FRR")
    #                 # plt.ylabel("RPR (Sensitivität)")
    #                 # close_zero_roc = np.argmin(np.abs(thresholds_roc))
    #                 # plt.plot(fpr[close_zero_roc], tpr[close_zero_roc], 'o', markersize=10, label="ROC threshold zero",
    #                 #          fillstyle="none", c='k', mew=2)
    #                 # plt.savefig("k_NN_ROC_curve_{}_{}".format(d['name'], k))
    #                 # plt.close()
    #                 # # ROC/AUC Score
    #                 # auc = roc_auc_score(test_labels, k_NN_grid_search.decision_function(test_data))
    #                 # # print("AUC: {:.3f}".format(auc))
    #                 #
    #                 # str_for_results = "F1-Score: {:.2f}, Average Precision (Relevanz): {:.3f}, AUC: {:.3f}".format(f1, avps, auc)
    #
    #             else:
    #                 # multiple category classifier
    #                 target_names = ['baseline', 'cd', 'emotion_one', 'emotion_two', 'stress_one',
    #                                 'stress_two']
    #                 cm = confusion_matrix(test_labels, lda_grid_search.predict(test_data))
    #                 cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
    #                                                  xticklabels=target_names, yticklabels=target_names,
    #                                                  cmap=plt.get_cmap("gray_r"), fmt="%d")
    #
    #                 plt.title("Confusion Matrix: {}".format(d['name']))
    #                 plt.gca().invert_yaxis()
    #                 plt.colorbar(cm_image)
    #                 plt.savefig("lda_confusion_matrix_{}_{}_{}".format(d['name'], k, appendix))
    #                 plt.close()
    #                 # cr = classification_report(test_labels, k_NN_grid_search.predict(test_data),
    #                 #                            target_names=target_names)
    #                 # f1_micro = f1_score(test_labels, k_NN_grid_search.predict(test_data), average="micro")
    #                 # f1_macro = f1_score(test_labels, k_NN_grid_search.predict(test_data), average="macro")
    #                 # str_for_results = 'F1-Score (micro): {:.3f}, F1-Score (macro): {:.3f}'.format(f1_micro, f1_macro)
    #
    #             lda_appendices.append(appendix)
    #             lda_datasets.append(d['name'])
    #             lda_cv.append(k)
    #             lda_parameters.append(lda_grid_search.best_params_)
    #             lda_best_score_cv.append(round(lda_grid_search.best_score_, 3) * 100)
    #             lda_test_accuracy.append(round(lda_grid_search.score(test_data, test_labels), 3) * 100)
    #             lda_confusion_matrix.append('RightNegative: {}, FalseNegative: {}, RightPositive: {},'
    #                                         'FalsePositive: {})'.format(cm[0, 0], cm[1, 0], cm[1, 1],
    #                                                                      cm[0, 1]), )
    #
    #     lda_df = pd.DataFrame({'Feature Selection': lda_appendices,
    #                             'Dataset': lda_datasets,
    #                             'CV [k_fold]': lda_cv,
    #                             'Best Parameters': lda_parameters,
    #                             'Best Accuracy CV [%]': lda_best_score_cv,
    #                             'Accuracy Test Data [%]': lda_test_accuracy,
    #                             'ConfusionMatrix': lda_confusion_matrix,
    #                             })
    #     lda_df.to_excel('lda_{}.xlsx'.format(k), sheet_name='sheet1', index=False)

    # ------------------- kNN Classifier ------------------- #
    # param_grid = [{'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}]
    # appendices = ['_all', '_bvp_time_only', '_bvp_freq_only', '_gsr_only', '_temp_only', '_red_time', '_red_freq']
    # my_cv = [3, 5]
    # for k in my_cv:
    #     k_NN_appendices = list([])
    #     k_NN_datasets = list([])
    #     k_NN_cv = list([])
    #     k_NN_parameters = list([])
    #     k_NN_best_score_cv = list([])
    #     k_NN_test_accuracy = list([])
    #     k_NN_confusion_matrix = list([])
    #
    #     for a in appendices:
    #         appendix = a
    #         for d in dataset_dicts:
    #             train_data = d['X_train' + appendix]
    #             train_labels = d['y_train']
    #             test_data = d['X_test' + appendix]
    #             test_labels = d['y_test']
    #             # create model for rbf param grid
    #             k_NN_grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=k)
    #             # train model
    #             k_NN_grid_search.fit(train_data, train_labels)
    #             # transform results into a dataframe for plotting
    #             # results = pd.DataFrame(k_NN_grid_search.cv_results_)
    #
    #             # print('Best Parameters: {}'.format(k_NN_grid_search.best_params_))
    #             # print('Best Score Cross Validation: {:.3f}'.format(k_NN_grid_search.best_score_))
    #             # print('Accuracy Test Data: {:.3f}'.format(k_NN_grid_search.score(test_data, test_labels)))
    #             if len(d['target_names']) == 2:
    #                 # binary classifier
    #                 target_names = d['target_names']
    #                 # confusion matrix
    #                 cm = confusion_matrix(test_labels, k_NN_grid_search.predict(test_data))
    #                 cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
    #                                                  xticklabels=target_names, yticklabels=target_names,
    #                                                  cmap=plt.get_cmap("gray_r"), fmt="%d")
    #                 plt.title("Confusion Matrix: {}".format(d['name']))
    #                 plt.gca().invert_yaxis()
    #                 plt.colorbar(cm_image)
    #                 plt.savefig("k_NN_confusion_matrix_{}_{}_{}".format(d['name'], k, appendix))
    #                 plt.close()
    #                 # print("Confusion Matrix: \n{}".format(confusion))
    #                 # print('RightNegative: {}, FalseNegative: {}, RightPositive: {}, falsePositive: {}'.format(
    #                 #     confusion[0, 0], confusion[1, 0], confusion[1, 1], confusion[0, 1]))
    #
    #                 # f1 score
    #                 # f1 = f1_score(test_labels, k_NN_grid_search.predict(test_data))
    #                 # print('F1-Score: {:.2f}'.format(f1_score(test_labels, dt_grid_search.predict(test_data))))
    #                 # classification report
    #                 # cr = classification_report(test_labels, k_NN_grid_search.predict(test_data),
    #                 #                            target_names=target_names)
    #                 # print(classification_report(test_labels, k_NN_grid_search.predict(test_data),
    #                 #                             target_names=d['target_names']))
    #
    #                 # # precision recall curve
    #                 # precision, recall, thresholds = \
    #                 #     precision_recall_curve(test_labels, k_NN_grid_search.decision_function(test_data))
    #                 # # find threshold closest to 0
    #                 # close_zero = np.argmin(np.abs(thresholds))
    #                 # plt.plot(precision[close_zero], recall[close_zero], 'o', markersize=10, label="threshold zero",
    #                 #          fillstyle="none", c='k', mew=2)
    #                 # plt.plot(precision, recall, label="precision recall curve")
    #                 # plt.xlabel("Precision (Relevanz)")
    #                 # plt.ylabel("Recall (Sensitivität)")
    #                 # plt.legend(loc='best')
    #                 # plt.savefig("k_NN_prc_{}_{}".format(d['name'], k))
    #                 # plt.close()
    #                 # # average precision score
    #                 # avps = average_precision_score(test_labels, k_NN_grid_search.decision_function(test_data))
    #                 # # print("Average Precision (Relevanz): {}".format(avps))
    #                 # # ROC curve
    #                 # fpr, tpr, thresholds_roc = roc_curve(test_labels, k_NN_grid_search.decision_function(test_data))
    #                 # plt.plot(fpr, tpr, label="ROC Curve")
    #                 # plt.xlabel("FRR")
    #                 # plt.ylabel("RPR (Sensitivität)")
    #                 # close_zero_roc = np.argmin(np.abs(thresholds_roc))
    #                 # plt.plot(fpr[close_zero_roc], tpr[close_zero_roc], 'o', markersize=10, label="ROC threshold zero",
    #                 #          fillstyle="none", c='k', mew=2)
    #                 # plt.savefig("k_NN_ROC_curve_{}_{}".format(d['name'], k))
    #                 # plt.close()
    #                 # # ROC/AUC Score
    #                 # auc = roc_auc_score(test_labels, k_NN_grid_search.decision_function(test_data))
    #                 # # print("AUC: {:.3f}".format(auc))
    #                 #
    #                 # str_for_results = "F1-Score: {:.2f}, Average Precision (Relevanz): {:.3f}, AUC: {:.3f}".format(f1, avps, auc)
    #
    #             else:
    #                 # multiple category classifier
    #                 if d['name'] == 'complete_no_cd_dict':
    #                     target_names = ['baseline', 'emotion_one', 'emotion_two', 'stress_one',
    #                                     'stress_two']
    #                 else:
    #                     target_names = ['baseline', 'cd', 'emotion_one', 'emotion_two', 'stress_one',
    #                                     'stress_two']
    #                 cm = confusion_matrix(test_labels, k_NN_grid_search.predict(test_data))
    #                 cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
    #                                                  xticklabels=target_names, yticklabels=target_names,
    #                                                  cmap=plt.get_cmap("gray_r"), fmt="%d")
    #
    #                 plt.title("Confusion Matrix: {}".format(d['name']))
    #                 plt.gca().invert_yaxis()
    #                 plt.colorbar(cm_image)
    #                 plt.savefig("k_NN_confusion_matrix_{}_{}_{}".format(d['name'], k, appendix))
    #                 plt.close()
    #                 # cr = classification_report(test_labels, k_NN_grid_search.predict(test_data),
    #                 #                            target_names=target_names)
    #                 # f1_micro = f1_score(test_labels, k_NN_grid_search.predict(test_data), average="micro")
    #                 # f1_macro = f1_score(test_labels, k_NN_grid_search.predict(test_data), average="macro")
    #                 # str_for_results = 'F1-Score (micro): {:.3f}, F1-Score (macro): {:.3f}'.format(f1_micro, f1_macro)
    #
    #             k_NN_appendices.append(appendix)
    #             k_NN_datasets.append(d['name'])
    #             k_NN_cv.append(k)
    #             k_NN_parameters.append(k_NN_grid_search.best_params_)
    #             k_NN_best_score_cv.append(round(k_NN_grid_search.best_score_, 3)*100)
    #             k_NN_test_accuracy.append(round(k_NN_grid_search.score(test_data, test_labels), 3)*100)
    #             k_NN_confusion_matrix.append(cm)
    #
    #     k_NN_df = pd.DataFrame({'Feature Selection': k_NN_appendices,
    #                             'Dataset': k_NN_datasets,
    #                             'CV [k_fold]': k_NN_cv,
    #                             'Best Parameters': k_NN_parameters,
    #                             'Best Accuracy CV [%]': k_NN_best_score_cv,
    #                             'Accuracy Test Data [%]': k_NN_test_accuracy,
    #                             'ConfusionMatrix': k_NN_confusion_matrix,
    #                             })
    #
    #     k_NN_df.to_excel('k_NN_{}.xlsx'.format(k), sheet_name='sheet1', index=False)
    #
    # # --- SVC --- #
    # # Set parameter grid for gridsearch
    # # use param_grids[0] for 'rbf' kernel use param_grids[1] for 'linear
    # #
    # param_grids = [{'kernel': ['rbf'],
    #                 'C': [0.001, 0.01, 0.1, 1, 10, 100, 150, 200],
    #                 'gamma': [0.0001, 0.001, 0.01, 0.1, 1, 10, 50, 100]},
    #                {'kernel': ['linear'],
    #                'C': [0.001, 0.01, 0.1, 1, 10, 100]},
    #                ]
    #
    # appendices = ['_all', '_bvp_time_only', '_bvp_freq_only', '_gsr_only', '_temp_only', '_red_time', '_red_freq']
    # my_cv = [3, 5]
    # for k in my_cv:
    #     svc_appendices = list([])
    #     svc_datasets = list([])
    #     svc_cv = list([])
    #     svc_parameters = list([])
    #     svc_best_score_cv = list([])
    #     svc_test_accuracy = list([])
    #     svc_confusion_matrix = list([])
    #     svc_eval = list([])
    #     for a in appendices:
    #         appendix = a
    #         for d in dataset_dicts:
    #             train_data = d['X_train' + appendix]
    #             train_labels = d['y_train']
    #             test_data = d['X_test' + appendix]
    #             test_labels = d['y_test']
    #             # Min Max Scaling
    #             scaler = MinMaxScaler()
    #             scaler.fit(train_data)
    #             # Transform Training Data
    #             train_data_min_max_scaled = scaler.transform(train_data)
    #             test_data_min_max_scaled = scaler.transform(test_data)
    #             # create model for rbf param grid
    #             svc_grid_search = GridSearchCV(SVC(), param_grids[0], cv=k)
    #             # train model
    #             svc_grid_search.fit(train_data_min_max_scaled, train_labels)
    #             # transform results into a dataframe for plotting
    #             results = pd.DataFrame(svc_grid_search.cv_results_)
    #             scores = np.array(results.mean_test_score).reshape(len(param_grids[0]['C']), len(param_grids[0]['gamma']))
    #             # scores_image = mglearn.tools.heatmap(scores, xlabel='gamma', xticklabels=param_grids[0]['gamma'], ylabel='C',
    #             #                                      yticklabels=param_grids[0]['C'], cmap='viridis')
    #             # plt.title('CV-Scores for Set: {} and k={}'.format(d['name'], k))
    #             # plt.colorbar(scores_image)
    #             # plt.savefig('svc_cv_scores_grid_search_{}_{}.png'.format(d['name'], k))
    #             # # plt.show()
    #             # plt.close()
    #
    #             # print('Best Parameters: {}'.format(svc_grid_search.best_params_))
    #             # print('Best Score Cross Validation: {:.3f}'.format(svc_grid_search.best_score_))
    #             # print('Accuracy Test Data: {:.3f}'.format(svc_grid_search.score(test_data_min_max_scaled, test_labels)))
    #             if len(d['target_names']) == 2:
    #                 # binary classifier
    #                 target_names = d['target_names']
    #                 # confusion matrix
    #                 cm = confusion_matrix(test_labels, svc_grid_search.predict(test_data_min_max_scaled))
    #                 cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
    #                                                  xticklabels=target_names, yticklabels=target_names,
    #                                                  cmap=plt.get_cmap("gray_r"), fmt="%d")
    #                 plt.title("Confusion Matrix: {}".format(d['name']))
    #                 plt.gca().invert_yaxis()
    #                 plt.colorbar(cm_image)
    #                 plt.savefig("svc_confusion_matrix_{}_{}".format(d['name'], k))
    #                 plt.close()
    #                 # print("Confusion Matrix: \n{}".format(confusion))
    #                 # print('RightNegative: {}, FalseNegative: {}, RightPositive: {}, falsePositive: {}'.format(
    #                 #     confusion[0, 0], confusion[1, 0], confusion[1, 1], confusion[0, 1]))
    #
    #                 # f1 score
    #                 f1 = f1_score(test_labels, svc_grid_search.predict(test_data))
    #                 # print('F1-Score: {:.2f}'.format(f1_score(test_labels, dt_grid_search.predict(test_data))))
    #                 # classification report
    #                 cr = classification_report(test_labels, svc_grid_search.predict(test_data_min_max_scaled),
    #                                            target_names=target_names)
    #                 # print(classification_report(test_labels, svc_grid_search.predict(test_data),
    #                 #                             target_names=d['target_names']))
    #
    #                 # precision recall curve
    #                 precision, recall, thresholds = \
    #                     precision_recall_curve(test_labels, svc_grid_search.decision_function(test_data_min_max_scaled))
    #                 # find threshold closest to 0
    #                 close_zero = np.argmin(np.abs(thresholds))
    #                 plt.plot(precision[close_zero], recall[close_zero], 'o', markersize=10, label="threshold zero",
    #                          fillstyle="none", c='k', mew=2)
    #                 plt.plot(precision, recall, label="precision recall curve")
    #                 plt.xlabel("Precision (Relevanz)")
    #                 plt.ylabel("Recall (Sensitivität)")
    #                 plt.legend(loc='best')
    #                 plt.savefig("svc_prc_{}_{}".format(d['name'], k))
    #                 plt.close()
    #                 # average precision score
    #                 avps = average_precision_score(test_labels, svc_grid_search.decision_function(test_data_min_max_scaled))
    #                 # print("Average Precision (Relevanz): {}".format(avps))
    #                 # ROC curve
    #                 fpr, tpr, thresholds_roc = roc_curve(test_labels, svc_grid_search.decision_function(test_data_min_max_scaled))
    #                 plt.plot(fpr, tpr, label="ROC Curve")
    #                 plt.xlabel("FRR")
    #                 plt.ylabel("RPR (Sensitivität)")
    #                 close_zero_roc = np.argmin(np.abs(thresholds_roc))
    #                 plt.plot(fpr[close_zero_roc], tpr[close_zero_roc], 'o', markersize=10, label="ROC threshold zero",
    #                          fillstyle="none", c='k', mew=2)
    #                 plt.savefig("svc_ROC_curve_{}_{}".format(d['name'], k))
    #                 plt.close()
    #                 # ROC/AUC Score
    #                 auc = roc_auc_score(test_labels, svc_grid_search.decision_function(test_data_min_max_scaled))
    #                 # print("AUC: {:.3f}".format(auc))
    #
    #                 str_for_results = "F1-Score: {:.2f}, Average Precision (Relevanz): {:.3f}, AUC: {:.3f}".format(f1, avps, auc)
    #
    #             else:
    #                 # multiple category classifier
    #                 if d['name'] == 'complete_no_cd_dict':
    #                     target_names = ['baseline', 'emotion_one', 'emotion_two', 'stress_one',
    #                                     'stress_two']
    #                 else:
    #                     target_names = ['baseline', 'cd', 'emotion_one', 'emotion_two', 'stress_one',
    #                                     'stress_two']
    #                 cm = confusion_matrix(test_labels, svc_grid_search.predict(test_data_min_max_scaled))
    #                 cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
    #                                                  xticklabels=target_names, yticklabels=target_names,
    #                                                  cmap=plt.get_cmap("gray_r"), fmt="%d")
    #
    #                 plt.title("Confusion Matrix: {}".format(d['name']))
    #                 plt.gca().invert_yaxis()
    #                 plt.colorbar(cm_image)
    #                 plt.savefig("svc_confusion_matrix_{}_{}".format(d['name'], k))
    #                 plt.close()
    #                 cr = classification_report(test_labels, svc_grid_search.predict(test_data_min_max_scaled),
    #                                            target_names=target_names)
    #                 f1_micro = f1_score(test_labels, svc_grid_search.predict(test_data_min_max_scaled), average="micro")
    #                 f1_macro = f1_score(test_labels, svc_grid_search.predict(test_data_min_max_scaled), average="macro")
    #                 str_for_results = 'F1-Score (micro): {:.3f}, F1-Score (macro): {:.3f}'.format(f1_micro, f1_macro)
    #
    #             svc_appendices.append(appendix)
    #             svc_datasets.append(d['name'])
    #             svc_cv.append(k)
    #             svc_parameters.append(svc_grid_search.best_params_)
    #             svc_best_score_cv.append(round(svc_grid_search.best_score_, 3) * 100)
    #             svc_test_accuracy.append(round(svc_grid_search.score(test_data_min_max_scaled, test_labels), 3) * 100)
    #             svc_confusion_matrix.append(cm)
    #             svc_eval.append(str_for_results)
    #
    #     svc_df = pd.DataFrame({'Feature Selection': svc_appendices,
    #                            'Dataset': svc_datasets,
    #                            'CV [k_fold]': svc_cv,
    #                            'Best Parameters': svc_parameters,
    #                            'Best Accuracy CV [%]': svc_best_score_cv,
    #                            'Accuracy Test Data [%]': svc_test_accuracy,
    #                            'ConfusionMatrix': svc_confusion_matrix,
    #                            'Evaluation Metrics': svc_eval,
    #                            })
    #     svc_df.to_excel('svc_poly_{}.xlsx'.format(k), sheet_name='sheet1', index=False)

    # --- Random Forest --- #
    # Set parameter grid for gridsearch

    param_grids = {'max_depth': [1, 2, 3, 4, 5],
                   'max_features': [0.10, 0.25, 0.5, 0.75, 1.0],
                   'n_estimators': [5, 25, 50, 100, 250, 500, 1000],
                   'random_state': [0]}

    appendices = ['_all', '_bvp_time_only', '_bvp_freq_only', '_gsr_only', '_temp_only', '_red_time', '_red_freq']
    my_cv = [3, 5]
    for k in my_cv:
        dt_appendices = list([])
        dt_datasets = list([])
        dt_cv = list([])
        dt_parameters = list([])
        dt_best_score_cv = list([])
        dt_test_accuracy = list([])
        dt_confusion_matrix = list([])
        dt_eval = list([])
        for a in appendices:
            appendix = a

            for d in dataset_dicts:
                train_data = d['X_train' + appendix]
                train_labels = d['y_train']
                test_data = d['X_test' + appendix]
                test_labels = d['y_test']

                # create model for rbf param grid
                dt_grid_search = GridSearchCV(RandomForestClassifier(), param_grids, cv=k)
                # train model
                dt_grid_search.fit(train_data, train_labels)
                # transform results into a dataframe for plotting
                results = pd.DataFrame(dt_grid_search.cv_results_)
                # print('Best Parameters: {}'.format(dt_grid_search.best_params_))
                # print('Best Score Cross Validation: {:.3f}'.format(dt_grid_search.best_score_))
                # print('Accuracy Test Data: {:.3f}'.format(dt_grid_search.score(test_data, test_labels)))
                # evaluation metrics
                if len(d['target_names']) == 2:
                    # binary classifier
                    target_names = d['target_names']
                    # confusion matrix
                    cm = confusion_matrix(test_labels, dt_grid_search.predict(test_data))
                    # cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
                    #                                  xticklabels=target_names, yticklabels=target_names,
                    #                                  cmap=plt.get_cmap("gray_r"), fmt="%d")
                    # plt.title("Confusion Matrix: {}".format(d['name']))
                    # plt.gca().invert_yaxis()
                    # plt.colorbar(cm_image)
                    # plt.savefig("dtrf_confusion_matrix_{}_{}".format(d['name'], k))
                    # plt.close()
                    # print("Confusion Matrix: \n{}".format(confusion))
                    # print('RightNegative: {}, FalseNegative: {}, RightPositive: {}, falsePositive: {}'.format(
                    #     confusion[0, 0], confusion[1, 0], confusion[1, 1], confusion[0, 1]))

                    # f1 score
                    f1 = f1_score(test_labels, dt_grid_search.predict(test_data))
                    # print('F1-Score: {:.2f}'.format(f1_score(test_labels, dt_grid_search.predict(test_data))))
                    # classification report
                    cr = classification_report(test_labels, dt_grid_search.predict(test_data),
                                               target_names=target_names)
                    # print(classification_report(test_labels, dt_grid_search.predict(test_data),
                    #                             target_names=d['target_names']))

                    # precision recall curve
                    # RandomForestClassifier has no predict_function -> use predict_proba_
                    precision, recall, thresholds = \
                        precision_recall_curve(test_labels, dt_grid_search.predict_proba(test_data)[:, 1])
                    # find threshold closest to 0
                    close_default = np.argmin(np.abs(thresholds - 0.5))
                    # plt.plot(precision[close_default], recall[close_default], 'o', markersize=10, label="threshold 0.5",
                    #          fillstyle="none", c='k', mew=2)
                    # plt.plot(precision, recall, label="precision recall curve")
                    # plt.xlabel("Precision (Relevanz)")
                    # plt.ylabel("Recall (Sensitivität)")
                    # plt.legend(loc='best')
                    # plt.savefig("dtrf_prc_{}_{}".format(d['name'], k))
                    # plt.close()
                    # average precision score
                    avps = average_precision_score(test_labels, dt_grid_search.predict_proba(test_data)[:, 1])
                    # print("Average Precision (Relevanz): {}".format(avps))
                    # ROC curve
                    fpr, tpr, thresholds_roc = roc_curve(test_labels, dt_grid_search.predict_proba(test_data)[:, 1])
                    # plt.plot(fpr, tpr, label="ROC Curve")
                    # plt.xlabel("FRR")
                    # plt.ylabel("RPR (Sensitivität)")
                    # close_default_roc = np.argmin(np.abs(thresholds_roc - 0.5))
                    # plt.plot(fpr[close_default_roc], tpr[close_default_roc], 'o', markersize=10, label="ROC threshold 0.5",
                    #          fillstyle="none", c='k', mew=2)
                    # plt.savefig("dtrf_ROC_curve_{}_{}".format(d['name'], k))
                    # plt.close()
                    # ROC/AUC Score
                    auc = roc_auc_score(test_labels, dt_grid_search.predict_proba(test_data)[:, 1])
                    # print("AUC: {:.3f}".format(auc))

                    str_for_results = "F1-Score: {:.2f}, Average Precision (Relevanz): {:.3f}, AUC: {:.3f}".format(f1, avps, auc)

                else:
                    # multiple category classifier
                    if d['name'] == 'complete_no_cd_dict':
                        target_names = ['baseline', 'emotion_one', 'emotion_two', 'stress_one',
                                        'stress_two']
                    else:
                        target_names = ['baseline', 'cd', 'emotion_one', 'emotion_two', 'stress_one',
                                        'stress_two']
                    cm = confusion_matrix(test_labels, dt_grid_search.predict(test_data))
                    # cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
                    #                                  xticklabels=target_names, yticklabels=target_names,
                    #                                  cmap=plt.get_cmap("gray_r"), fmt="%d")
                    # plt.title("Confusion Matrix: {}".format(d['name']))
                    # plt.gca().invert_yaxis()
                    # plt.colorbar(cm_image)
                    # plt.savefig("dtrf_confusion_matrix_{}_{}".format(d['name'], k))
                    # plt.close()

                    cr = classification_report(test_labels, dt_grid_search.predict(test_data),
                                               target_names=target_names)
                    f1_micro = f1_score(test_labels, dt_grid_search.predict(test_data), average="micro")
                    f1_macro = f1_score(test_labels, dt_grid_search.predict(test_data), average="macro")
                    str_for_results = 'F1-Score (micro): {:.3f}, F1-Score (macro): {:.3f}'.format(f1_micro, f1_macro)

                # best = dt_grid_search.best_estimator_
                # plot_feature_importance_random_forest(model=best, dataset=d, fold=k)

                dt_appendices.append(appendix)
                dt_datasets.append(d['name'])
                dt_cv.append(k)
                dt_parameters.append(dt_grid_search.best_params_)
                dt_best_score_cv.append(round(dt_grid_search.best_score_, 3) * 100)
                dt_test_accuracy.append(round(dt_grid_search.score(test_data, test_labels), 3) * 100)
                dt_confusion_matrix.append(cm)
                dt_eval.append(str_for_results)

        dt_df = pd.DataFrame({'Feature Selection': dt_appendices,
                              'Dataset': dt_datasets,
                              'CV [k_fold]': dt_cv,
                              'Best Parameters': dt_parameters,
                              'Best Accuracy CV [%]': dt_best_score_cv,
                              'Accuracy Test Data [%]': dt_test_accuracy,
                              'ConfusionMatrix': dt_confusion_matrix,
                              'Evaluation Metrics': dt_eval,
                              })
        dt_df.to_excel('dt_{}.xlsx'.format(k), sheet_name='sheet1', index=False)

    # # --- Gradient Boosting --- #
    # # Set parameter grid for gridsearch
    #
    # param_grids = {'max_depth': [1, 2, 3],
    #                'max_features': [5, 15, 31, 45, 62],
    #                'n_estimators': [5, 25, 50, 100, 250, 500, 1000],
    #                'learning_rate': [0.1, 0.05, 0.01, 0.005, 0.0025, 0.0015, 0.001],
    #                'random_state': [0]}
    #
    # for k in [3, 5]:
    #     dt_grid_results = list([])
    #     appendix = ''
    #     for d in dataset_dicts:
    #         train_data = d['X_train' + appendix]
    #         train_labels = d['y_train']
    #         test_data = d['X_test' + appendix]
    #         test_labels = d['y_test']
    #
    #         # create model for rbf param grid
    #         dt_grid_search = GridSearchCV(GradientBoostingClassifier(), param_grids, cv=k)
    #         # train model
    #         dt_grid_search.fit(train_data, train_labels)
    #         # transform results into a dataframe for plotting
    #         results = pd.DataFrame(dt_grid_search.cv_results_)
    #         # print('Best Parameters: {}'.format(dt_grid_search.best_params_))
    #         # print('Best Score Cross Validation: {:.3f}'.format(dt_grid_search.best_score_))
    #         # print('Accuracy Test Data: {:.3f}'.format(dt_grid_search.score(test_data, test_labels)))
    #
    #         if len(d['target_names']) == 2:
    #             # binary classifier
    #             target_names = d['target_names']
    #             # confusion matrix
    #             cm = confusion_matrix(test_labels, dt_grid_search.predict(test_data))
    #             cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
    #                                              xticklabels=target_names, yticklabels=target_names,
    #                                              cmap=plt.get_cmap("gray_r"), fmt="%d")
    #             plt.title("Confusion Matrix: {}".format(d['name']))
    #             plt.gca().invert_yaxis()
    #             plt.colorbar(cm_image)
    #             plt.savefig("dtgb_confusion_matrix_{}_{}".format(d['name'], k))
    #             plt.close()
    #             # print("Confusion Matrix: \n{}".format(confusion))
    #             # print('RightNegative: {}, FalseNegative: {}, RightPositive: {}, falsePositive: {}'.format(
    #             #     confusion[0, 0], confusion[1, 0], confusion[1, 1], confusion[0, 1]))
    #
    #             # f1 score
    #             f1 = f1_score(test_labels, dt_grid_search.predict(test_data))
    #             # print('F1-Score: {:.2f}'.format(f1_score(test_labels, dt_grid_search.predict(test_data))))
    #             # classification report
    #             cr = classification_report(test_labels, dt_grid_search.predict(test_data),
    #                                        target_names=target_names)
    #             # print(classification_report(test_labels, dt_grid_search.predict(test_data),
    #             #                             target_names=d['target_names']))
    #
    #             # precision recall curve
    #             precision, recall, thresholds = \
    #                 precision_recall_curve(test_labels, dt_grid_search.decision_function(test_data))
    #             # find threshold closest to 0
    #             close_zero = np.argmin(np.abs(thresholds))
    #             plt.plot(precision[close_zero], recall[close_zero], 'o', markersize=10, label="threshold zero",
    #                      fillstyle="none", c='k', mew=2)
    #             plt.plot(precision, recall, label="precision recall curve")
    #             plt.xlabel("Precision (Relevanz)")
    #             plt.ylabel("Recall (Sensitivität)")
    #             plt.legend(loc='best')
    #             plt.savefig("dtgb_prc_{}_{}".format(d['name'], k))
    #             plt.close()
    #             # average precision score
    #             avps = average_precision_score(test_labels, dt_grid_search.decision_function(test_data))
    #             # print("Average Precision (Relevanz): {}".format(avps))
    #             # ROC curve
    #             fpr, tpr, thresholds_roc = roc_curve(test_labels, dt_grid_search.decision_function(test_data))
    #             plt.plot(fpr, tpr, label="ROC Curve")
    #             plt.xlabel("FRR")
    #             plt.ylabel("RPR (Sensitivität)")
    #             close_zero_roc = np.argmin(np.abs(thresholds_roc))
    #             plt.plot(fpr[close_zero_roc], tpr[close_zero_roc], 'o', markersize=10, label="ROC threshold zero",
    #                      fillstyle="none", c='k', mew=2)
    #             plt.savefig("dtgb_ROC_curve_{}_{}".format(d['name'], k))
    #             plt.close()
    #             # ROC/AUC Score
    #             auc = roc_auc_score(test_labels, dt_grid_search.decision_function(test_data))
    #             # print("AUC: {:.3f}".format(auc))
    #
    #             str_for_results = "F1-Score: {:.2f}, Average Precision (Relevanz): {:.3f}, AUC: {:.3f}".format(f1, avps, auc)
    #
    #         else:
    #             # multiple category classifier
    #             if d['name'] == 'complete_no_cd_dict':
    #                 target_names = ['baseline', 'emotion_one', 'emotion_two', 'stress_one',
    #                                 'stress_two']
    #             else:
    #                 target_names = ['baseline', 'cd', 'emotion_one', 'emotion_two', 'stress_one',
    #                                 'stress_two']
    #             cm = confusion_matrix(test_labels, dt_grid_search.predict(test_data))
    #             cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
    #                                              xticklabels=target_names, yticklabels=target_names,
    #                                              cmap=plt.get_cmap("gray_r"), fmt="%d")
    #             plt.title("Confusion Matrix: {}".format(d['name']))
    #             plt.gca().invert_yaxis()
    #             plt.colorbar(cm_image)
    #             plt.savefig("dtgb_confusion_matrix_{}_{}".format(d['name'], k))
    #             plt.close()
    #             cr = classification_report(test_labels, dt_grid_search.predict(test_data),
    #                                        target_names=target_names)
    #             f1_micro = f1_score(test_labels, dt_grid_search.predict(test_data), average="micro")
    #             f1_macro = f1_score(test_labels, dt_grid_search.predict(test_data), average="macro")
    #             str_for_results = 'F1-Score (micro): {:.3f}, F1-Score (macro): {:.3f}'.format(f1_micro, f1_macro)
    #
    #         best = dt_grid_search.best_estimator_
    #         plot_feature_importance_gradient_boosting(model=best, dataset=d, fold=k)
    #         dt_grid_results.append(['Dataset: {}'.format(d['name']),
    #                                 'Best Parameters: {}'.format(dt_grid_search.best_params_),
    #                                 'Best Score Cross Validation: {:.3f}'.format(dt_grid_search.best_score_),
    #                                 'Accuracy Test Data: {:.3f}'.format(
    #                                     dt_grid_search.score(test_data, test_labels)),
    #                                 'ConfusionMatrix(RightNegative: {}, FalseNegative: {}, RightPositive: {}, '
    #                                 'FalsePositive: {})'.format(cm[0, 0], cm[1, 0], cm[1, 1],
    #                                                             cm[0, 1]),
    #                                 str_for_results
    #                                 ])
    #         dt_grid_results.append('Classification Report: \n {}'.format(cr))
    #         dt_grid_results.append([])
    #
    #     write_to_text_file(file_name='dtgb_grid_results_cv' + str(k), file_index=appendix,
    #                        folder='MTEC\ClassificationRepository\Log',
    #                        data_list=dt_grid_results)

    # # --- Neural Network --- #
    # # Set parameter grid for gridsearch

    param_grids = {'solver': ['lbfgs'],
                   'activation': ['tanh', 'relu'],
                   'alpha': [0.00001, 0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1],
                   'learning_rate_init': [0.001, 0.01, 0.1],
                   'random_state': [0]}
    appendices = ['_all', '_bvp_time_only', '_bvp_freq_only', '_gsr_only', '_temp_only', '_red_time', '_red_freq']
    my_cv = [3, 5]
    for k in my_cv:
        mlp_appendices = list([])
        mlp_datasets = list([])
        mlp_cv = list([])
        mlp_parameters = list([])
        mlp_best_score_cv = list([])
        mlp_test_accuracy = list([])
        mlp_confusion_matrix = list([])
        mlp_eval = list([])
        for a in appendices:
            appendix = a

            for d in dataset_dicts:
                train_data = d['X_train' + appendix]
                train_labels = d['y_train']
                test_data = d['X_test' + appendix]
                test_labels = d['y_test']
                dim = [len(d['X_test_all'][0])]
                param_grids['hidden_layer_sizes'] = [[int(dim/2)], [int(dim/2), int(dim/2)], [int(dim/2), int(dim/2), int(dim/2)],
                                                     [dim], [dim, dim], [dim, dim, dim],
                                                     [dim*2], [dim*2, dim*2], [dim*2, dim*2, dim*2],
                                                     [100], [100, 100], [100, 100, 100]]
                # Min Max Scaling
                scaler = MinMaxScaler()
                scaler.fit(train_data)
                # Transform Training Data
                train_data_min_max_scaled = scaler.transform(train_data)
                test_data_min_max_scaled = scaler.transform(test_data)
                # create model for rbf param grid
                mlp_grid_search = GridSearchCV(MLPClassifier(), param_grids, cv=k)
                # train model
                mlp_grid_search.fit(train_data_min_max_scaled, train_labels)
                # transform results into a dataframe for plotting
                results = pd.DataFrame(mlp_grid_search.cv_results_)
                # scores = np.array(results.mean_test_score).reshape(len(param_grids[0]['C']),
                #                                                   len(param_grids[0]['gamma']))
                # scores_image = mglearn.tools.heatmap(scores, xlabel='gamma', xticklabels=param_grids[0]['gamma'], ylabel='C',
                #                                      yticklabels=param_grids[0]['C'], cmap='viridis')
                # plt.title('CV-Scores for Set: {} and k={}'.format(d['name'], k))
                # plt.colorbar(scores_image)
                # plt.savefig('svc_cv_scores_grid_search_{}_{}.png'.format(d['name'], k))
                # # plt.show()
                # plt.close()

                # print('Best Parameters: {}'.format(svc_grid_search.best_params_))
                # print('Best Score Cross Validation: {:.3f}'.format(svc_grid_search.best_score_))
                # print('Accuracy Test Data: {:.3f}'.format(svc_grid_search.score(test_data_min_max_scaled, test_labels)))
                if len(d['target_names']) == 2:
                    # binary classifier
                    target_names = d['target_names']
                    # confusion matrix
                    cm = confusion_matrix(test_labels, mlp_grid_search.predict(test_data_min_max_scaled))
                    cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
                                                     xticklabels=target_names, yticklabels=target_names,
                                                     cmap=plt.get_cmap("gray_r"), fmt="%d")
                    plt.title("Confusion Matrix: {}".format(d['name']))
                    plt.gca().invert_yaxis()
                    plt.colorbar(cm_image)
                    plt.savefig("mlp_confusion_matrix_{}_{}".format(d['name'], k))
                    plt.close()
                    # print("Confusion Matrix: \n{}".format(confusion))
                    # print('RightNegative: {}, FalseNegative: {}, RightPositive: {}, falsePositive: {}'.format(
                    #     confusion[0, 0], confusion[1, 0], confusion[1, 1], confusion[0, 1]))

                    # f1 score
                    f1 = f1_score(test_labels, mlp_grid_search.predict(test_data))
                    # print('F1-Score: {:.2f}'.format(f1_score(test_labels, dt_grid_search.predict(test_data))))
                    # classification report
                    cr = classification_report(test_labels, mlp_grid_search.predict(test_data_min_max_scaled),
                                               target_names=target_names)
                    # print(classification_report(test_labels, svc_grid_search.predict(test_data),
                    #                             target_names=d['target_names']))

                    # precision recall curve
                    precision, recall, thresholds = \
                        precision_recall_curve(test_labels, mlp_grid_search.decision_function(test_data_min_max_scaled))
                    # find threshold closest to 0
                    close_zero = np.argmin(np.abs(thresholds))
                    plt.plot(precision[close_zero], recall[close_zero], 'o', markersize=10, label="threshold zero",
                             fillstyle="none", c='k', mew=2)
                    plt.plot(precision, recall, label="precision recall curve")
                    plt.xlabel("Precision (Relevanz)")
                    plt.ylabel("Recall (Sensitivität)")
                    plt.legend(loc='best')
                    plt.savefig("mlp_prc_{}_{}".format(d['name'], k))
                    plt.close()
                    # average precision score
                    avps = average_precision_score(test_labels,
                                                   mlp_grid_search.decision_function(test_data_min_max_scaled))
                    # print("Average Precision (Relevanz): {}".format(avps))
                    # ROC curve
                    fpr, tpr, thresholds_roc = roc_curve(test_labels,
                                                         mlp_grid_search.decision_function(test_data_min_max_scaled))
                    plt.plot(fpr, tpr, label="ROC Curve")
                    plt.xlabel("FRR")
                    plt.ylabel("RPR (Sensitivität)")
                    close_zero_roc = np.argmin(np.abs(thresholds_roc))
                    plt.plot(fpr[close_zero_roc], tpr[close_zero_roc], 'o', markersize=10, label="ROC threshold zero",
                             fillstyle="none", c='k', mew=2)
                    plt.savefig("mlp_ROC_curve_{}_{}".format(d['name'], k))
                    plt.close()
                    # ROC/AUC Score
                    auc = roc_auc_score(test_labels, mlp_grid_search.decision_function(test_data_min_max_scaled))
                    # print("AUC: {:.3f}".format(auc))

                    str_for_results = "F1-Score: {:.2f}, Average Precision (Relevanz): {:.3f}, AUC: {:.3f}".format(f1,
                                                                                                                   avps,
                                                                                                                   auc)

                else:
                    # multiple category classifier
                    if d['name'] == 'complete_no_cd_dict':
                        target_names = ['baseline', 'emotion_one', 'emotion_two', 'stress_one',
                                        'stress_two']
                    else:
                        target_names = ['baseline', 'cd', 'emotion_one', 'emotion_two', 'stress_one',
                                        'stress_two']
                    cm = confusion_matrix(test_labels, mlp_grid_search.predict(test_data_min_max_scaled))
                    cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
                                                     xticklabels=target_names, yticklabels=target_names,
                                                     cmap=plt.get_cmap("gray_r"), fmt="%d")

                    plt.title("Confusion Matrix: {}".format(d['name']))
                    plt.gca().invert_yaxis()
                    plt.colorbar(cm_image)
                    plt.savefig("mlp_confusion_matrix_{}_{}".format(d['name'], k))
                    plt.close()
                    cr = classification_report(test_labels, mlp_grid_search.predict(test_data_min_max_scaled),
                                               target_names=target_names)
                    f1_micro = f1_score(test_labels, mlp_grid_search.predict(test_data_min_max_scaled), average="micro")
                    f1_macro = f1_score(test_labels, mlp_grid_search.predict(test_data_min_max_scaled), average="macro")
                    str_for_results = 'F1-Score (micro): {:.3f}, F1-Score (macro): {:.3f}'.format(f1_micro, f1_macro)

                mlp_appendices.append(appendix)
                mlp_datasets.append(d['name'])
                mlp_cv.append(k)
                mlp_parameters.append(mlp_grid_search.best_params_)
                mlp_best_score_cv.append(round(mlp_grid_search.best_score_, 3) * 100)
                mlp_test_accuracy.append(round(mlp_grid_search.score(test_data_min_max_scaled, test_labels), 3) * 100)
                mlp_confusion_matrix.append(cm)
                mlp_eval.append(str_for_results)

            mlp_df = pd.DataFrame({'Feature Selection': mlp_appendices,
                                   'Dataset': mlp_datasets,
                                   'CV [k_fold]': mlp_cv,
                                   'Best Parameters': mlp_parameters,
                                   'Best Accuracy CV [%]': mlp_best_score_cv,
                                   'Accuracy Test Data [%]': mlp_test_accuracy,
                                   'ConfusionMatrix': mlp_confusion_matrix,
                                   'Evaluation Metrics': mlp_eval,
                                   })
            mlp_df.to_excel('mlp_{}.xlsx'.format(k), sheet_name='sheet1', index=False)
        #     scaler = MinMaxScaler()
        #     scaler.fit(train_data)
        #     # Transform Training Data
        #     train_data_min_max_scaled = scaler.transform(train_data)
        #     # Transform Training Data
        #     test_data_min_max_scaled = scaler.transform(test_data)
        #     # create model for rbf param grid
        #     mlp_grid_search = GridSearchCV(MLPClassifier(), param_grids, cv=k)
        #     # train model
        #     mlp_grid_search.fit(train_data_min_max_scaled, train_labels)
        #     # transform results into a dataframe for plotting
        #     results = pd.DataFrame(mlp_grid_search.cv_results_)
        #     # print('Best Parameters: {}'.format(mlp_grid_search.best_params_))
        #     # print('Best Score Cross Validation: {:.3f}'.format(mlp_grid_search.best_score_))
        #     # print('Accuracy Test Data: {:.3f}'.format(mlp_grid_search.score(test_data_min_max_scaled, test_labels)))
        #     if len(d['target_names']) == 2:
        #         # binary classifier
        #         target_names = d['target_names']
        #         # confusion matrix
        #         cm = confusion_matrix(test_labels, mlp_grid_search.predict(test_data))
        #         cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
        #                                          xticklabels=target_names, yticklabels=target_names,
        #                                          cmap=plt.get_cmap("gray_r"), fmt="%d")
        #         plt.title("Confusion Matrix: {}".format(d['name']))
        #         plt.gca().invert_yaxis()
        #         plt.colorbar(cm_image)
        #         plt.savefig("mlp_confusion_matrix_{}_{}".format(d['name'], k))
        #         plt.close()
        #         # print("Confusion Matrix: \n{}".format(confusion))
        #         # print('RightNegative: {}, FalseNegative: {}, RightPositive: {}, falsePositive: {}'.format(
        #         #     confusion[0, 0], confusion[1, 0], confusion[1, 1], confusion[0, 1]))
        #
        #         # f1 score
        #         f1 = f1_score(test_labels, mlp_grid_search.predict(test_data))
        #         # print('F1-Score: {:.2f}'.format(f1_score(test_labels, dt_grid_search.predict(test_data))))
        #         # classification report
        #         cr = classification_report(test_labels, mlp_grid_search.predict(test_data),
        #                                    target_names=target_names)
        #         # print(classification_report(test_labels, dt_grid_search.predict(test_data),
        #         #                             target_names=d['target_names']))
        #
        #         # precision recall curve
        #         # precision, recall, thresholds = \
        #         #     precision_recall_curve(test_labels, mlp_grid_search.decision_function(test_data))
        #         # find threshold closest to 0
        #         # close_zero = np.argmin(np.abs(thresholds))
        #         # plt.plot(precision[close_zero], recall[close_zero], 'o', markersize=10, label="threshold zero",
        #         #          fillstyle="none", c='k', mew=2)
        #         # plt.plot(precision, recall, label="precision recall curve")
        #         # plt.xlabel("Precision (Relevanz)")
        #         # plt.ylabel("Recall (Sensitivität)")
        #         # plt.legend(loc='best')
        #         # plt.savefig("mlp_prc_{}_{}".format(d['name'], k))
        #         # plt.close()
        #         # average precision score
        #         # avps = average_precision_score(test_labels, mlp_grid_search.decision_function(test_data)[:, 1])
        #         # print("Average Precision (Relevanz): {}".format(avps))
        #         # ROC curve
        #         # fpr, tpr, thresholds_roc = roc_curve(test_labels, mlp_grid_search.decision_function(test_data)[:, 1])
        #         # plt.plot(fpr, tpr, label="ROC Curve")
        #         # plt.xlabel("FRR")
        #         # plt.ylabel("RPR (Sensitivität)")
        #         # close_zero_roc = np.argmin(np.abs(thresholds_roc))
        #         # plt.plot(fpr[close_zero_roc], tpr[close_zero_roc], 'o', markersize=10, label="ROC threshold zero",
        #         #          fillstyle="none", c='k', mew=2)
        #         # plt.savefig("mlp_ROC_curve_{}_{}".format(d['name'], k))
        #         # plt.close()
        #         # ROC/AUC Score
        #         # auc = roc_auc_score(test_labels, mlp_grid_search.decision_function(test_data)[:, 1])
        #         # print("AUC: {:.3f}".format(auc))
        #
        #         str_for_results = "F1-Score: {:.2f}".format(f1)
        #
        #     else:
        #         # multiple category classifier
        #         if d['name'] == 'complete_no_cd_dict':
        #             target_names = ['baseline', 'emotion_one', 'emotion_two', 'stress_one',
        #                             'stress_two']
        #         else:
        #             target_names = ['baseline', 'cd', 'emotion_one', 'emotion_two', 'stress_one',
        #                             'stress_two']
        #         cm = confusion_matrix(test_labels, mlp_grid_search.predict(test_data))
        #         cm_image = mglearn.tools.heatmap(cm, xlabel="Predicted Label", ylabel="True Label",
        #                                          xticklabels=target_names, yticklabels=target_names,
        #                                          cmap=plt.get_cmap("gray_r"), fmt="%d")
        #         plt.title("Confusion Matrix: {}".format(d['name']))
        #         plt.gca().invert_yaxis()
        #         plt.colorbar(cm_image)
        #         plt.savefig("mlp_confusion_matrix_{}_{}".format(d['name'], k))
        #         plt.close()
        #         cr = classification_report(test_labels, mlp_grid_search.predict(test_data),
        #                                    target_names=target_names)
        #         f1_micro = f1_score(test_labels, mlp_grid_search.predict(test_data), average="micro")
        #         f1_macro = f1_score(test_labels, mlp_grid_search.predict(test_data), average="macro")
        #         str_for_results = 'F1-Score (micro): {:.3f}, F1-Score (macro): {:.3f}'.format(f1_micro, f1_macro)
        #
        #     mlp_grid_results.append(['Dataset: {}'.format(d['name']),
        #                              'Best Parameters: {}'.format(mlp_grid_search.best_params_),
        #                              'Best Score Cross Validation: {:.3f}'.format(mlp_grid_search.best_score_),
        #                              'Accuracy Test Data: {:.3f}'.format(
        #                                  mlp_grid_search.score(test_data, test_labels)),
        #                              'ConfusionMatrix(RightNegative: {}, FalseNegative: {}, RightPositive: {}, '
        #                              'FalsePositive: {})'.format(cm[0, 0], cm[1, 0], cm[1, 1],
        #                                                          cm[0, 1]),
        #                              str_for_results
        #                              ])
        #     mlp_grid_results.append('Classification Report: \n {}'.format(cr))
        #     mlp_grid_results.append([])
        #
        # write_to_text_file(file_name='mlp_grid_results_cv_sgd' + str(k), file_index=appendix,
        #                    folder='MTEC\ClassificationRepository\Log',
        #                    data_list=mlp_grid_results)


def plot_feature_importance_tree(model: DecisionTreeClassifier, dataset: dict):
    n_features = np.size(dataset['data'], 1)
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), dataset['feature_names'])
    plt.title("Dataset: {}, max_depth: {}".format(dataset['name'], model.max_depth))
    plt.xlabel("Feature Importance")
    plt.ylabel("Feature")
    plt.savefig("Tree_{}_{}.png".format(dataset['name'], model.max_depth))
    # plt.show()


def plot_feature_importance_random_forest(model: RandomForestClassifier, dataset: dict, fold: int):
    n_features = np.size(dataset['data'], 1)
    # small = 4
    # medium = 10
    # big = 12
    #
    # # plt.rc('font', size=medium)  # controls default text sizes
    # # plt.rc('axes', titlesize=medium)  # fontsize of the axes title
    # # plt.rc('axes', labelsize=medium)  # fontsize of the x and y labels
    # plt.rc('xtick', labelsize=small)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=4)  # fontsize of the tick labels
    # # plt.rc('legend', fontsize=small)  # legend fontsize
    plt.rc('figure', titlesize=8)  # fontsize of the figure title
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), dataset['feature_names'])
    plt.title("Dataset: {}, n_estimators: {}, max_depth: {}, max_features: {}".format(dataset['name'],
                                                                                      model.n_estimators,
                                                                                      model.max_depth,
                                                                                      model.max_features))
    plt.xlabel("Feature Importance")
    plt.ylabel("Feature")
    plt.savefig("dtrf_best_{}_{}.png".format(dataset['name'], fold), dpi=400)
    # plt.show()
    plt.close()


def plot_feature_importance_gradient_boosting(model: GradientBoostingClassifier, dataset: dict, fold: int):
    n_features = np.size(dataset['data'], 1)
    plt.barh(range(n_features), model.feature_importances_, align='center')
    # small = 4
    # medium = 10
    # big = 12
    #
    # # plt.rc('font', size=medium)  # controls default text sizes
    # # plt.rc('axes', titlesize=medium)  # fontsize of the axes title
    # # plt.rc('axes', labelsize=medium)  # fontsize of the x and y labels
    # plt.rc('xtick', labelsize=small)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=4)  # fontsize of the tick labels
    # # plt.rc('legend', fontsize=small)  # legend fontsize
    plt.rc('figure', titlesize=8)  # fontsize of the figure title
    # plt.yticks(np.arange(n_features), dataset['feature_names'])
    plt.title("Dataset: {}, n_estimators: {}, max_depth: {}, learning_rate: {}".format(dataset['name'],
                                                                                       model.n_estimators,
                                                                                       model.max_depth,
                                                                                       model.learning_rate))
    plt.xlabel("Feature Importance")
    plt.ylabel("Feature")
    plt.savefig("dtgb_best_{}_{}.png".format(dataset['name'], fold), dpi=400)
    # plt.show()
    plt.close()


if __name__ == '__main__':
    main()
