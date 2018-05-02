import numpy as np
from sklearn import neighbors, datasets, linear_model
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

bunchobject = datasets.load_breast_cancer()

def get_metrics(actual_targets, predicted_targets, labels):
    c_matrix = confusion_matrix(actual_targets, predicted_targets,
                                labels)
    # Settle total records
    total_rcs = 0
    for l in c_matrix:
        for entry in l:
            total_rcs += entry

    # Settle Accuracy
    correct = 0
    for i in range(len(c_matrix)):
        correct += c_matrix[i][i]
    accuracy = correct / total_rcs

    # Settle Sensitivity
    positives = 0
    x = len(c_matrix) - 1
    for i in range(len(c_matrix)):
        positives += c_matrix[x][i]
    p_correct = c_matrix[x][x]
    sens = p_correct / positives

    # Settle False Positive Rate
    negs = total_rcs - positives
    f_p = c_matrix[0][x]
    fpr = (f_p / negs)

    # Build Dictionary
    metrics_d = {}
    metrics_d["confusion matrix"] = c_matrix
    metrics_d["total records"] = total_rcs
    metrics_d["accuracy"] = round(accuracy, 3)
    metrics_d["sensitivity"] = round(sens, 3)
    metrics_d["false positive rate"] = round(fpr, 3)
    return metrics_d


def normalize_minmax(data):
    norm = []
    x = np.transpose(data)
    for i in range(len(x)):
        col = x[i]
        diff_a = np.max(col) - np.min(col)
        min_a = np.min(col)
        for j in range(len(col)):
            k = col[j]
            col[j] = (k - min_a) / diff_a
        norm.append(col)
    norm = np.array(norm)
    norm = np.transpose(norm)
    return norm


def knn_classifier_full(bunchobject, feature_list, size, seed):
    # Step 1-3: Acquire Data, and produce Normalisation
    data = bunchobject.data[:, feature_list]
    x = normalize_minmax(data)
    y = bunchobject["target"]

    # Step 4: Divide Model into 3 sets for training, validation, test
    x_train, x_split, y_train, y_split = train_test_split(x, y,
                                                          test_size=size, random_state=seed)
    x_v, x_t, y_v, y_t = train_test_split(x_split, y_split,
                                          test_size=0.5, random_state=seed)

    # Steps 5-6: Iterate N, build knn classifier, find lowest k
    acc = []
    res_dict = {}
    for k in range(1, 20):
        knn = neighbors.KNeighborsClassifier(n_neighbors=k)
        knn.fit(x_train, y_train)
        pred_v = knn.predict(x_v)
        pred_v.reshape(-1, 1)
        labels = [0, 1]
        v_results = get_metrics(y_v, pred_v, labels)
        res_dict[k] = v_results
        acc.append(v_results["accuracy"])
    max_acc = max(acc)
    real_k = acc.index(max_acc) + 1


    # Step 7: Predict Real Results
    knn = neighbors.KNeighborsClassifier(n_neighbors=real_k)
    knn.fit(x_train, y_train)
    pred_t = knn.predict(x_t)
    pred_t.reshape(-1, 1)
    labels = [0, 1]
    r_results = get_metrics(y_t, pred_t, labels)

    # Step 8: Build output
    out = {}
    out["best k"] = real_k
    out["validation set"] = res_dict[real_k]
    out["test set"] = r_results
    return out


features = range(20)  # select features in cols 0 to 19
results = knn_classifier_full(bunchobject, features, 0.40, 2752)
print(results)
