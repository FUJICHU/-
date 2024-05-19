import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split,GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.preprocessing import LabelEncoder
from joblib import dump, load
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib
matplotlib.use('tkagg')
# 读取数据集
data = pd.read_csv("clean.csv")
# 选择特征列和目标变量列
features = ["建造时间", "朝向", "大小", "房间数", "区域"]
data['单价'] = data['单价'].astype(float)
salary_bins = [5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, float('inf')]
salary_labels = ['5000-10000', '10000-20000', '20000-30000', '30000-40000', '40000-50000', '50000-60000', '60000-70000', '70000-80000', '80000+']
data['price_range'] = pd.cut(data['单价'], bins=salary_bins, labels=salary_labels, right=False)
# 进行标签编码
label_encoders = {}
needfit = ["建造时间", "朝向","区域"]
for feature in needfit:
    label_encoders[feature] = LabelEncoder()
    data[feature] = label_encoders[feature].fit_transform(data[feature])
label_encoders['price_range'] = LabelEncoder()
data['price_range'] = label_encoders['price_range'].fit_transform(data['price_range'])
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(data[features], data['price_range'], test_size=0.2, random_state=42)

# 随机森林模型
rf_model = RandomForestClassifier()
params = {'n_estimators': [50, 100, 200], 'max_depth': [None, 5, 10], 'min_samples_split': [2, 4, 6]}
grid_search_rf = GridSearchCV(rf_model, params, cv=5)
grid_search_rf.fit(X_train, y_train)
rf_model = grid_search_rf.best_estimator_
# 保存随机森林模型和数据处理规则
dump(rf_model, "rf_model.joblib")
dump(label_encoders, "label_encoders.joblib")
# 评估随机森林模型
rf_predictions = rf_model.predict(X_test)
rf_rmse = mean_squared_error(y_test, rf_predictions, squared=False)
print("随机森林模型的均方根误差（RMSE）：", rf_rmse)
# 交叉验证评估随机森林模型
cv_scores_rf = cross_val_score(rf_model, X_train, y_train, cv=5)
print("随机森林模型的交叉验证准确率：", cv_scores_rf.mean())
# 生成预测结果和真实标签
y_true = y_test
# 绘制混淆矩阵
cm = confusion_matrix(y_true, rf_predictions)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('rf_Confusion Matrix')
plt.show()


# 朴素贝叶斯模型
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
# 保存朴素贝叶斯模型和数据处理规则
dump(nb_model, "nb_model.joblib")
dump(label_encoders, "label_encoders.joblib")
# 评估朴素贝叶斯模型
nb_predictions = nb_model.predict(X_test)
nb_accuracy = accuracy_score(y_test, nb_predictions)
print("朴素贝叶斯模型的准确率：", nb_accuracy)
# 交叉验证评估朴素贝叶斯模型
cv_scores_nb = cross_val_score(nb_model, X_train, y_train, cv=5)
print("朴素贝叶斯模型的交叉验证准确率：", cv_scores_nb.mean())
# 生成预测结果和真实标签
y_true = y_test
# 绘制混淆矩阵
cm = confusion_matrix(y_true, nb_predictions)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('bys_Confusion Matrix')
plt.show()
