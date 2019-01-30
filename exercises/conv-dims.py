from keras.models import Sequential
from keras.layers import Conv2D

K=1
F=2
S=1
H_in=200
W_in=200


def	SetupModel(Filters,Kernel,Strides,H_in,W_in):
	print("Filters: ",Filters, " kernel_size= ",Kernel," strides=",Strides," H_in/W_in: ",H_in,"/", W_in)
	model = Sequential()
	model.add(Conv2D(filters=Filters, kernel_size=Kernel, 
			strides=Strides, padding='valid', activation='relu',
			input_shape=(H_in, W_in, 1)))
	model.summary()
	parameters=((Kernel*Kernel)+1)*Filters
	hiddenSize=(H_in/Strides)-(Kernel-Strides)
	print("Predicted parameters=",parameters)
	print("Predicted hiddenSize=",hiddenSize)



print("parameters equals Filters*[(kernel_size * kernel_size)+strides]")
h1=10
SetupModel(1,2,1,h1,h1)
SetupModel(1,2,2,h1,h1)
SetupModel(1,3,1,h1,h1)
SetupModel(1,3,2,h1,h1)

SetupModel(10,2,1,h1,h1)
SetupModel(10,2,2,h1,h1)
SetupModel(10,3,1,h1,h1)
SetupModel(10,3,2,h1,h1)


h1=200
SetupModel(1,2,1,h1,h1)
SetupModel(1,2,2,h1,h1)
SetupModel(1,3,1,h1,h1)
SetupModel(1,3,2,h1,h1)

SetupModel(10,2,1,h1,h1)
SetupModel(10,2,2,h1,h1)
SetupModel(10,3,1,h1,h1)
SetupModel(10,3,2,h1,h1)





SetupModel(1,3,1,h1,h1)
SetupModel(1,3,2,h1,h1)


#SetupModel(1,2,1,200,200)

#SetupModel(2,2,1,200,200)

#SetupModel(1,2,3,200,200)

# model = Sequential()
# model.add(Conv2D(filters=1, kernel_size=h1, strides=1, padding='valid', 
#    activation='relu', input_shape=(h1, h1, 1)))
#
# model.summary()