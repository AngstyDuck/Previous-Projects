import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

bunchobject = datasets.load_breast_cancer()


"""
def five_number_summary(x):
    def one_list(x):
        max = np.max(x)
        min = np.min(x)
        per25 = np.percentile(x,25)
        per75 = np.percentile(x,75)
        per50 = np.percentile(x,50)
        return {'minimum':min, 'first quartile': per25,'median': per50, 'third quartile': per75, 'maximum': max}

    list_len = len(x[0])
    output_list = []
    for i in range(list_len):
        sublist = []
        for j in x:
            sublist.append(j[i])
        output_list.append(one_list(sublist))
    return output_list



def normalize_minmax(x):

#takes in a nested list and returns a normalised list of the same format

    def one_list(x):
        output_list = []
        max_list = max(x)
        min_list = min(x)
        max_min_diff = max_list - min_list

        #minus all elements by min_list
        for i in x:
            output_list.append((i-min_list)/max_min_diff)

        return output_list

    list_len = len(x[0])
    output_list = []

    for i in range(len(x)):
        output_list.append([])

    for i in range(list_len):
        sublist = []
        for j in x:
            sublist.append(j[i])

        pre_output_list = one_list(sublist)

        for k in range(len(pre_output_list)):
            output_list[k].append(pre_output_list[k])


    return np.array(output_list)


def get_metrics(actual_targets, predicted_targets, labels):
    c_matrix = confusion_matrix(actual_targets,predicted_targets,labels)
    total_records = sum(c_matrix[1]) + sum(c_matrix[0])
    accuracy = (c_matrix[0][0] + c_matrix[1][1]) / total_records
    sensitivity = (c_matrix[1][1])/(c_matrix[1][1] + c_matrix[1][0])
    false_positive_rate = (c_matrix[0][1]) / (c_matrix[0][1] + c_matrix[0][0])
    outputDict = {'confusion matrix':c_matrix, 'total records':round(total_records,3), 'accuracy':round(accuracy,3), 'sensitivity':round(sensitivity,3), 'false positive rate':round(false_positive_rate,3)}
    return outputDict


def knn_classifier(bunchobject, feature_list, size, seed, k):
    data = bunchobject.data[:, feature_list]
    normalized_list = normalize_minmax(data)
    data_train, data_test, target_train, target_test = train_test_split(normalized_list, bunchobject.target,
                                                                        test_size=size, random_state=seed)

    clf = neighbors.KNeighborsClassifier(n_neighbors = k, )
    clf.fit(data_train, target_train)
    target_predicted = clf.predict(data_test)

    labels = [0, 1]
    results = get_metrics(target_test, target_predicted, labels)

    return results




def linear_regression(bunchobject, x_index, y_index, size, seed):

    data_x = bunchobject.data[:, x_index]
    data_y = bunchobject.data[:, y_index]

    data_x = np.reshape(data_x, (-1,1))
    data_y = np.reshape(data_y, (-1,1))

    data_train, data_test, target_train, target_test = train_test_split(data_x, data_y,
                                                                        test_size=size, random_state=seed)
    regr = linear_model.LinearRegression()
    regr.fit(data_train, target_train)
    y_pred = regr.predict(data_test)

    #returns a list of the coeff of x^^[-i]

    output_polyfit = np.polyfit(np.reshape(data_test,(1,-1))[0], np.reshape(y_pred,(1,-1))[0],1)
    coeff_x0 = np.array([output_polyfit[-1]])
    coeff_x1 = np.array([[output_polyfit[:-2]]])

    #to find mean squared error
    output_mean_squared_error = mean_squared_error(target_test, y_pred)

    #to find out r^^2
    output_r_squared_score = r2_score(target_test, y_pred)

    output_result = {'coefficients':coeff_x1, 'intercept':coeff_x0, 'mean squared error':output_mean_squared_error, 'r2 score':output_r_squared_score}

    return data_train, target_train, data_test, y_pred, output_result



def multiple_linear_regression(bunchobject, x_index, y_index, order, size, seed):
    data_x = bunchobject.data[:, x_index]
    data_y = bunchobject.data[:, y_index]
    data_x = np.reshape(data_x, (-1,1))
    data_y = np.reshape(data_y, (-1,1))

    poly = PolynomialFeatures(degree=order, include_bias=False)
    c_data = poly.fit_transform(data_x)
    data_train, data_test, target_train, target_test = train_test_split(c_data, data_y,
                                                                        test_size=size, random_state=seed)

    regr = linear_model.LinearRegression()
    regr.fit(data_train, target_train)
    y_pred = regr.predict(data_test)
    coeff = regr.coef_
    y_inter = regr.intercept_

    #to find mean squared error
    output_mean_squared_error = mean_squared_error(target_test, y_pred)

    #to find out r^^2
    output_r_squared_score = r2_score(target_test, y_pred)

    output_result = {'coefficients':coeff, 'intercept':y_inter, 'mean squared error':output_mean_squared_error, 'r2 score':output_r_squared_score}

    #note: i didnt get full marks because i submitted data_train instead of data_train[:,0]
    return data_train[:,0], target_train, data_test[:,0], y_pred, output_result

x_train, y_train, x_test, y_pred, results = multiple_linear_regression(bunchobject,0,3,4,0.4,2752)
print('x_train: {0}, x_test: {1}'.format(x_train,x_test))
"""


def normalize_minmax(x):

#takes in a nested list and returns a normalised list of the same format

    def one_list(x):
        output_list = []
        max_list = max(x)
        min_list = min(x)
        max_min_diff = max_list - min_list

        #minus all elements by min_list
        for i in x:
            output_list.append((i-min_list)/max_min_diff)

        return output_list

    list_len = len(x[0])
    output_list = []

    for i in range(len(x)):
        output_list.append([])

    for i in range(list_len):
        sublist = []
        for j in x:
            sublist.append(j[i])

        pre_output_list = one_list(sublist)

        for k in range(len(pre_output_list)):
            output_list[k].append(pre_output_list[k])


    return np.array(output_list)


def get_metrics(actual_targets, predicted_targets, labels):
    c_matrix = confusion_matrix(actual_targets,predicted_targets,labels)
    total_records = sum(c_matrix[1]) + sum(c_matrix[0])
    accuracy = (c_matrix[0][0] + c_matrix[1][1]) / total_records
    sensitivity = (c_matrix[1][1])/(c_matrix[1][1] + c_matrix[1][0])
    false_positive_rate = (c_matrix[0][1]) / (c_matrix[0][1] + c_matrix[0][0])
    outputDict = {'confusion matrix':c_matrix, 'total records':round(total_records,3), 'accuracy':round(accuracy,3), 'sensitivity':round(sensitivity,3), 'false positive rate':round(false_positive_rate,3)}
    return outputDict


def knn_classifier_full(bunchobject, feature_list, size, seed):
    data = bunchobject.data[:, feature_list]
    normalized_list = normalize_minmax(data)
    data_train, data_test_, target_train, target_test_ = train_test_split(normalized_list, bunchobject.target,
                                                                        test_size=size, random_state=seed)
    data_validate, data_test, target_validate, target_test = train_test_split(data_test_, target_test_,
                                                                        test_size=0.5, random_state=seed)

    #create list of all possible results for k = range(1,20)
    acc = []
    dict_list = []
    for k in range(1,20):
        clf = neighbors.KNeighborsClassifier(n_neighbors = k, )
        clf.fit(data_train, target_train)
        target_predicted = clf.predict(data_validate)

        labels = [0, 1]
        results = get_metrics(target_validate, target_predicted, labels)

        dict_list.append(results)
        acc.append(results['accuracy'])

    #find out best k
    max_acc = max(acc)
    max_acc_index = acc.index(max_acc)
    k_value = max_acc_index + 1

    #find out validation set
    validation_set = dict_list[max_acc_index]

    #find out test set
    clf = neighbors.KNeighborsClassifier(n_neighbors=k_value, )
    clf.fit(data_train, target_train)
    target_predicted = clf.predict(data_test)

    labels = [0, 1]
    results = get_metrics(target_test, target_predicted, labels)

    test_set = results

    #construct output
    output = {'best k':k_value, 'validation set':validation_set, 'test set':test_set}
    return output

features = range(20)
results = knn_classifier_full(bunchobject, features, 0.4, 2752)
print(results)


























