import os
import cv2
import numpy as np
from sklearn import preprocessing
from progress.bar import Bar
import time

def main():
    mainStartTime = time.time()
    trainImagePath = './images_split/train/'
    testImagePath = './images_split/test/'
    trainFeaturePathGrayHist = './features_labels/grayHist/train/'
    testFeaturePathGrayHist = './features_labels/grayHist/test/'
    trainFeaturePathHuMoments = './features_labels/huMoments/train/'
    testFeaturePathHuMoments = './features_labels/huMoments/test/'
    
    print(f'[INFO] ========= TRAINING IMAGES ========= ')
    trainImages, trainLabels = getData(trainImagePath)
    trainEncodedLabels, encoderClasses = encodeLabels(trainLabels)

    # Gray Histogram
    trainFeaturesGrayHist = extractGrayHistogramFeatures(trainImages)
    saveData(trainFeaturePathGrayHist,trainEncodedLabels,trainFeaturesGrayHist,encoderClasses)
    # Hu Moments
    trainFeaturesHuMoments = extractHuMomentsFeatures(trainImages)
    saveData(trainFeaturePathHuMoments,trainEncodedLabels,trainFeaturesHuMoments,encoderClasses)

    print(f'[INFO] =========== TEST IMAGES =========== ')
    testImages, testLabels = getData(testImagePath)
    testEncodedLabels, encoderClasses = encodeLabels(testLabels)

    # Gray Histogram
    testFeaturesGrayHist = extractGrayHistogramFeatures(testImages) 
    saveData(testFeaturePathGrayHist,testEncodedLabels,testFeaturesGrayHist,encoderClasses)
    # Hu Moments
    testFeaturesHu = extractHuMomentsFeatures(testImages) 
    saveData(testFeaturePathHuMoments,testEncodedLabels,testFeaturesHu,encoderClasses)

    elapsedTime = round(time.time() - mainStartTime,2)
    print(f'[INFO] Code execution time: {elapsedTime}s')

def getData(path):
    images = []
    labels = []
    if os.path.exists(path):
        for dirpath , dirnames , filenames in os.walk(path):   
            if (len(filenames)>0): #it's inside a folder with files
                folder_name = os.path.basename(dirpath)
                bar = Bar(f'[INFO] Getting images and labels from {folder_name}',max=len(filenames),suffix='%(index)d/%(max)d Duration:%(elapsed)ds')            
                for index, file in enumerate(filenames):
                    label = folder_name
                    labels.append(label)
                    full_path = os.path.join(dirpath,file)
                    image = cv2.imread(full_path)
                    images.append(image)
                    bar.next()
                bar.finish()
        #print(labels)
        return images, np.array(labels,dtype=object)
    
def extractGrayHistogramFeatures(images):
    bar = Bar('[INFO] Extrating Gray histogram features...',max=len(images),suffix='%(index)d/%(max)d  Duration:%(elapsed)ds')
    featuresList = []
    for image in images:
        if (np.ndim(image) > 2): # > 2 = colorida
            image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        bins = [256]
        hist  = cv2.calcHist([image], [0], None, bins, [0, 256])
        cv2.normalize(hist, hist)
        featuresList.append(hist.flatten())
        bar.next()
    bar.finish()
    return np.array(featuresList,dtype=object)

def extractHuMomentsFeatures(images):
    bar = Bar('[INFO] Extrating Hu Moments features...',max=len(images),suffix='%(index)d/%(max)d  Duration:%(elapsed)ds')
    featureList = []
    for image in images:
        if (np.ndim(image) > 2):  # > 2 = colorida
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Transformando a imagem para escala de cinza
            image = getBinaryImage(image) # Transformando a imagem em binária
        moments = cv2.moments(image) # Calcula os momentos da imagem
        hu_moments = cv2.HuMoments(moments) # Calcula os momentos Hu da imagem
        featureList.append(hu_moments.flatten())
        bar.next()
    bar.finish()
    return np.array(featureList,dtype=object)

def getBinaryImage(image):
    _, binaryImage = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY) # Transforma a imagem em binária
    return binaryImage

def encodeLabels(labels):
    startTime = time.time()
    print(f'[INFO] Encoding labels to numerical labels')
    encoder = preprocessing.LabelEncoder()
    encoded_labels = encoder.fit_transform(labels)
    elapsedTime = round(time.time() - startTime,2)
    print(f'[INFO] Encoding done in {elapsedTime}s')
    return np.array(encoded_labels,dtype=object), encoder.classes_

def saveData(path,labels,features,encoderClasses):
    startTime = time.time()
    print(f'[INFO] Saving data')
    #the name of the arrays will be used as filenames
    #f'{labels=}' gets both variable name and its corresponding values.
    #split('=')[0] gets the variable name from f'{labels=}'
    label_filename = f'{labels=}'.split('=')[0]+'.csv'
    feature_filename = f'{features=}'.split('=')[0]+'.csv'
    encoder_filename = f'{encoderClasses=}'.split('=')[0]+'.csv'
    np.savetxt(path+label_filename,labels, delimiter=',',fmt='%i')
    np.savetxt(path+feature_filename,features, delimiter=',') #float does not need format
    np.savetxt(path+encoder_filename,encoderClasses, delimiter=',',fmt='%s') 
    elapsedTime = round(time.time() - startTime,2)
    print(f'[INFO] Saving done in {elapsedTime}s')

if __name__ == "__main__":
    main()
