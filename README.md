# Hu Moments Feature Extractor

## Equipe

-   André Luiz Terassi Avancini

## Hu Moments

Hu Moments ou Momentos da Imagem é um algoritmo que obtém uma média ponderada das intensidades dos pixels de uma imagem. Eles são frequentemente usados ​​para caracterizar a forma de um objeto em uma imagem. A ideia do descritor de imagem Hu Moments ser utilizado para extração de características mais complexas de uma imagem, como forma, circuferência, área e muito mais.

### Propósito

Projeto destinado a disciplina de Processamento de Imagens que tem como finalidade a implementação de um descritor para então utilizar classificadores e obter sua acurácia para uma determinada quantia de imagens de RaioX que estão divididas em imagens de pulmões normais e imagens de pulmões infectados por Covid-19.

## Repositório

-   https://github.com/andreluiz19/procimg-final

## Classificadores e Acurácia

| Classificador | Acurácia |
| :------------ | :------- |
| RF            | 58.93%   |
| SVM           | 53.57%   |
| MLP           | 50%      |

## Tecnologias

-   Python

    ### Bibliotecas

    -   Numpy
    -   Scikit-learn
    -   OpenCV
    -   Matplotlib

## Instruções de Uso

-   Dentro da pasta `source_images` estão localizadas as imagens `normal` e `covid` sem nenhuma formatação de nome ou separação.

-   De ínicio, deve-se copiá-las para para o diretório `images_full` mantendo a separação entre `normal` e `covid`.

-   Ao executar o script `data_splitting.py` as imagens serão separadas no diretório `images_split`. Dentro desse diretório haverá uma separação de 80% para imagens de treinamento e 20% para imagens de testes. Elas ainda continuarão divididas em `normal` e `covid`.

-   Após configurar o dataset das imagens, executa-se então o script `grayHistogramAndHuMoments_FeatureExtraction.py`, esse script irá utilizar os métodos descritores
    **Gray Histogram Feature Extraction** e **Hu Moments** para salvar os `labels`, `features` e `encoderClasses`.

-   Então pode-se executar qualquer um dos scripts de classificação, `svm_classifier.py`, `rf_classifier.py`, `mlp_classifier.py` ou `run_all_classifiers.py` para obter a acurácia ou precisão de cada um dos algoritmos.

-   Como resultado dos classicadores, será gravado dentro do diretório `results` a **Matriz de Confusão** ou **Acurácia** dos algoritmos.

-   Não se esqueça de realizar a instalação das bibliotecas citadas acima. Como instalador Python recomendo a utilização do **Miniconda**.

## Referências

-   [Learn OpenCV](https://learnopencv.com/shape-matching-using-hu-moments-c-python/)
-   [CV Explained](https://cvexplained.wordpress.com/2020/07/21/10-4-hu-moments/)
-   [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
