# financialdata_GroupH
Financial Analytics Big Data Project


## Financial Data Package

This code runs 5 basic data tasks in order to make your data ready for modelling and also helps you choose among different models.
* Automated Data Cleaning
* Human-Assisted Data Cleaning
* Automated Dummy Creation with Automated Supervised Binning
* Automated Model Selection and Comparison
* Human-Assisted Model Selection

### Automated Data Cleaning

This function identifies invalid values, NAs, missing values, outliers, unreliable and out of range values. First it will check the type of data if it's numeric or not.
First step is importing a dataset and check all the values of the columns.
If it's not numeric it will replace missing values with the mode. For numeric it will replace NAs and unreliable values with the mean, outliers with min or max depending on the case.

```shell
autodataclean(trainingdataset)
autodataclean(trainingdataset,testdataset)
```

### Human-Assisted Data Cleaning

This function follows the same methodology than the automated version but allows the user to interact by allowing the selection of the value that will replace the non correct values.
For all the cases it will ask the user to select between mean, median or other value the user wants to use. 

```shell
manudataclean(trainingdataset)
manudataclean(trainingdataset,testdataset)
```

### Automated Dummy Creation with Automated Supervised Binning

This function creates bins based on the entropy with respect to the target variable, and then proceeds to create dummies for the bins.

```shell
autobindummy(trainingdataset,testdataset,targetvariable)
```

### Automated Model Selection and Comparison

This program takes as an input a file with multiple variables, selects a target variable and applies different classification models to later on show the most accurate one.
First step is selecting the target variable, then it uses K-Fold method to partition training data and testing data. The number of folds that are selected is 5.
It will first train each of the models within the partitions and finally give a result of the accuracy of that given model.
Once each model is tested, a data frame is created with the result of all the models sorted by the one with the highest accuracy.

```shell
automodel(trainingdataset,testdataset,targetvariable)
```

### Human-Assisted Model Selection

This program follows the same methodology than the previous one, the only difference is that the program interacts with the user by asking which model the user wants to select.
As a result there isn't a comparison between models but just the result of a single one.


```shell
manumodel(trainingdataset,testdataset,targetvariable)
```

## Contribution

This project has been completed by:
* Christabelle Santos
* Javier Lameda
* Michail Pintchiouk
* Mounir
* Natalia Hernandez
* Sergio Salas
* Tran Nyugen
* Vamsee Krishna

## Licensing

This project is licensed under the MIT License.

