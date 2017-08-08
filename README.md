
## Dependencies

- TensoFlow-gpu (1.2.1)
- Keras (2.0.2)
- PyQt5 (5.9)

## 介绍（Introduction）
整个程序分为两个部分，一个模型训练部分，一个是界面部分。</br>


- 模型部分是通过Keras训练得来的，用了MLP和CNN两种方法。CNN的效果几乎达到100%，比MLP收敛的速度要快。调`ModelTraining.py`训练自己的模型。训练好，调`main.py` 运行主界面程序。

这是CNN训练的准确度趋势。
![](http://i.imgur.com/QGertZi.png)



- 界面部分是通过PyQt5写的， 
<div  align="center">
<img src="http://i.imgur.com/HUUMSo3.png"/>
</div>
<div  align="center">
<img src="http://i.imgur.com/9FpqeGR.png"/>
</div>
<div  align="center">
<img src="http://i.imgur.com/X7ByV3P.png"/>
</div>

当然一些例子也会识别错，

<div  align="center">
<img src="http://i.imgur.com/jjFefJR.png"/>
</div>

毕竟Mnist训练写的数字都很正规。估计是没有学到一些特征，影响了它的泛化程度。

