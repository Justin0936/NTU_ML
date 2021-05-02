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



接下來就是在要開始啟動虛擬環境。您可以在CMD模式下進入Scripts目錄(在env01中)，接著CMD裡輸入activate就好了
activate

這時候CMD模式C:\mypython3\env01\Scripts>前面會有一個(env01)，表示您目前是處於此虛擬環境中。這時候您就可以在此虛擬環境中，開始安裝您所需要的各種package。

Step 4:離開虛擬環境
若要離開虛擬環境，只要輸入deactivate就可以離開目前虛擬環境，並且發現最前面已經沒有(env01)

https://medium.com/python4u/python-virtualenv%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83%E5%AE%89%E8%A3%9D-9d6be2d45db9


使用 pip 安裝 TensorFlow
https://www.tensorflow.org/install/pip?hl=zh-tw#virtual-environment-install

NTU HY Lee機器學習作業
https://github.com/GitYCC/NTU_HYLee_MachineLearning_Homework

大魚AI🐟 ：李宏毅機器學習(台灣大學)
https://github.com/dafish-ai/NTU-Machine-learning


