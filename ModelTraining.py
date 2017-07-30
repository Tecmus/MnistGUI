from keras.datasets import mnist
from keras.models import Sequential
from keras.models import load_model

import keras
from keras.layers import Dense,Activation,Dropout
from keras.layers import Conv2D, MaxPooling2D,Flatten

import numpy as np
import matplotlib.pyplot as plt


class MnistTraining:
    def __init__(self,model_type="cnn"):

        self.model_type=model_type
        self.model_path = "./models/"+model_type
        print(self.model_type)
        print(self.model_path)

    def processData(self,model_type='cnn'):

        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        if model_type=="cnn":
            model_path="./models/cnn"
            x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
            x_test = x_test.reshape(x_test.shape[0], x_train.shape[1], x_train.shape[2], 1)
            self.cnn_input_shape = (x_train.shape[1], x_train.shape[2], 1)

            # convert the data to the right type
            x_train = x_train.astype('float32')
            x_test = x_test.astype('float32')
            x_train /= 255
            x_test /= 255
            y_train = keras.utils.to_categorical(y_train, 10)
            y_test = keras.utils.to_categorical(y_test, 10)

        elif model_type=="mlp":
            model_path = "./models/mlp"
            x_train = x_train.reshape(x_train.shape[0], x_train.shape[1] * x_train.shape[2])
            x_test = x_test.reshape(x_test.shape[0], x_test.shape[1] * x_test.shape[2])
            y_train = (np.arange(10) == y_train[:, None]).astype(int)
            y_test = (np.arange(10) == y_test[:, None]).astype(int)

        return x_train,y_train,x_test,y_test

    def cnnTrain(self,epoch_num=10):
        x,y,x_,y_=self.processData("cnn")
        self.model = Sequential()

        self.model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
                         activation='relu',
                         input_shape=self.cnn_input_shape))

        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        self.model.add(Conv2D(64, (5, 5), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Flatten())

        # fully connect nn 
        self.model.add(Dense(1000, activation='relu'))
        self.model.add(Dense(10, activation='softmax'))

        self.model.compile(loss=keras.losses.categorical_crossentropy,
                      optimizer=keras.optimizers.Adam(),
                      metrics=['accuracy'])

        self.result=self.model.fit(x, y,
                  batch_size=32, epochs=epoch_num, verbose=1)

    def mlpTrain(self,epoch_num):
        x,y,x_,y_=self.processData('mlp')
        self.model=Sequential([
            Dense(units=500,input_shape=(784,)),
            Activation("relu"),
            Dense(units=100),
            Activation("sigmoid"),
            Dense(10),
            Activation("softmax")
        ])
        self.model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
        self.result=self.model.fit(x,y,epochs=epoch_num,batch_size=120,verbose=1) # 1 with log



    def train(self,epochs=10):

        if self.model_type=='cnn':
            self.processData('cnn')
            self.cnnTrain(epoch_num=epochs)
            pass
        elif self.model_type=='mlp':
            self.processData('mlp')
            self.mlpTrain(epoch_num=epochs)
            pass

        print(self.result.history)
        self.draw(self.result)
        self.model.save(self.model_path)

        pass

    def draw(self,res):
        x =range(len(res.history['acc']))
        plt.plot(x, res.history['acc'])
        plt.show()
        pass
if __name__=='__main__':

    mt=MnistTraining("cnn") #change 'cnn' to 'mlp' to use fully connect network
    mt.train(5)




