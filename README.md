#NTU_ML

![image](https://user-images.githubusercontent.com/69530706/116800891-8eaa2b80-ab37-11eb-8a4d-b8a04706552e.png)

虛擬環境和依賴項

virtual environment and dependencies

**method 1: virtualenv**

create virtual environment

  Step 1:安裝virtualenv
  
    pip3 install — upgrade pip   
    
    有時會發生需要.
    
    python -m pip install --upgrade pip  
    
   這時候我們就要開始安裝virtualenv套件
   pip install virtualenv
   
   Please refe: https://medium.com/python4u/python-virtualenv%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83%E5%AE%89%E8%A3%9D-9d6be2d45db9
   
$ virtualenv ./ENV
enter virtual environment

$ source ./ENV/bin/activate
if you want to exit virual environment,

$ deactivate
install dependencies under virtual environment

$ pip2.7 install -r requirements.txt

https://github.com/GitYCC/NTU_HYLee_MachineLearning_Homework


