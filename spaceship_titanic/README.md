
## Космический корабль титаник (kaggle)
Соревнование по анализу данных космического Титаника. Идея та же, что и у стандартного - предсказать, добрался ли пассажир до места назначения.

![image](https://github.com/merae70/da_projects/assets/113853691/01af54d8-4f97-4b2d-a0fd-4477407a9ae8)
![image](https://github.com/merae70/da_projects/assets/113853691/10eb958b-89ea-4383-a021-252a6426b989)

#

```
cat = CatBoostClassifier(verbose = False)
rfc = RandomForestClassifier(max_depth = 5, random_state=42)
dtc = DecisionTreeClassifier(max_depth=5)
abc = AdaBoostClassifier(random_state=42)
bc = BaggingClassifier(random_state=42)
gbdt = GradientBoostingClassifier(learning_rate=0.05, max_depth=8, n_estimators=500,subsample=0.5213,random_state=42)
xgb = XGBClassifier('binary:logistic',colsample_bytree=0.4603, gamma=0.0468, 
                             learning_rate=0.05, max_depth=5, 
                             min_child_weight=1.7817, n_estimators=500,
                             reg_alpha=4.5, reg_lambda=8.5,
                             subsample=0.5213,
                             random_state=42)
lgb = LGBMClassifier()
```

```
for CBC, the cross_val_score is 
0.8111878520188881
------------------------------
for RF, the cross_val_score is 
0.7627278134358078
------------------------------
for DTC, the cross_val_score is 
0.7743744213830948
------------------------------
for ABC, the cross_val_score is 
0.7920619191203471
------------------------------
for BC, the cross_val_score is 
0.7802698746825689
------------------------------
for GBDT, the cross_val_score is 
0.7950822605754361
------------------------------
for xgb, the cross_val_score is 
0.8068723396552349
------------------------------
for LGB, the cross_val_score is
0.8047162385117067
```
