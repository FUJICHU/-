import pandas as pd
from sklearn.preprocessing import LabelEncoder
from joblib import load


def Speculate(data):
    # 加载模型和标签编码器
    rf_model = load("rf_model.joblib")
    label_encoders = load("label_encoders.joblib")
    #data=
    # 创建新数据
    new_data = pd.DataFrame({"区域": [data[0]],
                             "房间数": [data[1]],
                             "大小": [data[2]],
                             "朝向": [data[3]],
                             "建造时间": [data[4]]})
    # 特征选择和预处理
    needfit = ["建造时间", "朝向", "区域"]
    features = ["建造时间", "朝向", "大小", "房间数", "区域"]
    new_data_encoded = new_data.copy()
    for feature in needfit:
        new_data_encoded[feature] = label_encoders[feature].transform(new_data[feature])
    # 进行预测
    prediction = rf_model.predict(new_data_encoded[features])
    # 将预测结果映射回薪资区间
    predicted_salary_range = label_encoders['price_range'].inverse_transform(prediction)
    # 打印预测结果
    print("预测的价格区间：", predicted_salary_range)
    return predicted_salary_range
Speculate(["六合", "3", "96.37", "南", "2015"])
Speculate(["鼓楼", "2", "83", "南北", "2011"])
Speculate(["栖霞", "4", "137.61", "南", "2019"])
Speculate(["江宁", "3", "114.49", "南北", "2018"])
#["区域", "房间数", "大小", "朝向","建造时间"]
