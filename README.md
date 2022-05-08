# faceswap-pytorch

Deepfakes_Faceswap using pytorch   *JUST FOR STUDY AND RESEARCH*

> This is pytorch version compared with https://github.com/joshua-wu/deepfakes_faceswap which using Keras.
> 
> This is a modernized fork of the pytorch version fork. 

![Processing image](https://github.com/Oldpan/faceswap-pytorch/blob/master/Screenshot%20from%202018-04-16%2015-36-47.png)


#### Source code you can download directly from the github page.
### Source code,training images and trained model(~300MB):
https://pan.baidu.com/s/197RIMB_Po96RZNFzV-wqjA    PW : z4wa 

## Requirement:
```
Python == 3.8
pytorch == 1.9.0
```
You need a modern GPU and CUDA support for better performance. *These requirements have been upgraded from the original head branch so as to fit modern needs and accelerate the training process.*

## How to run:

```
python train.py
```

if you don't use trained model, only after about 1000 epoch can you see the result and after 10000 epoch the result is the same with the above picture.

P.S. The Pytorch trains a little faster than Keras using tf backend.
