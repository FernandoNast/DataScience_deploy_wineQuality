# Deploy de Modelo em Produção
Quando se desenvolve um projeto em Ciência de Dados (CD) é preciso que este fique disponível para ser consultado por cliente ou mesmo por outros times. Dessa forma, faz-se necessário que uma requisição do modelo desenvolvido até então seja possível. Este projeto aborda então esta característica de um produto de CD.

Neste repositório encontram-se apenas os aquivos utilizados para se fazer requisização, ou seja, os que estão disponíveis no server.
* ``model/model_wine_quality.pkl`` - modelo de predição das notas sobre a qualidade dos vinhos;
* ``parameter/free_sulfur_dioxide_scaler.pkl total_sulfur_dioxide_scaler.pkl`` - arquivos com preparação de duas _features_ do conjunto de dados. Estes arquivos aplicam a normalização de ambas;
* ``wine_quality/WineQuality.py`` - a classe utilizada para aplicação das mudanças pelos dois arquivos anteriores;
* ``handler.py`` - API em Flask que receberá a requisição e retornará a predição do modelo;
* ``Procfile`` - arquivo sem extensão, utilizado pelo Heroku para inicializar a API na nuvem;
* ``requirements.txt`` - arquivo que contém os pacotes utilizados na coonstrução de todo o projeto;

## Objetivo
O objetivo principal deste projeto é obter conhecimentos das plataformas, API's, versionamentos, Servers que são necessários para deixar o modelo desenvolvido disponível e entender todo este processo, desde a criação do modelo, estruturas em arquivos .py de preparação dos dados até requisições do modelo.

## Metodologia
Para este projeto, foi utilizadado como base o canal [Seja Um Data Scientist](https://www.youtube.com/c/SejaUmDataScientist), onde se encontra uma série de vídeos sobre [Deploy de Modelos em Produção](https://www.youtube.com/watch?v=d6caxBhnf2I&list=PLZlkyCIi8bMpKoAicmYKrmAzZlkDFQVHY&index=4). 

Como base de dados, foi utilizado um conhecido conjunto de dados sobre a [qualidade de vinhos](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/) (winequality-red.csv), disponibilizado pela _University of California Irvine_ em seu repositório de _Machine Learning_ (ML). 

## Desenvolvimento
Para o desenvolvimento do modelo, primeiramente foi criado uma máquina virtual utilizando VirtualBox [Oracle VM](https://www.virtualbox.org/wiki/Downloads), onde foram desenvolvidos os demais processos. 
Para a criação do aplicativo web, foi utilizado o _framework_ [Flask](https://flask.palletsprojects.com/en/2.0.x/) e como server do modelo, foi utlizado o [Heroku](https://www.heroku.com/), uma plataforma nuvem para hospedagem de aplicações, gratuito e ser suficiente para os conhecimentos desejados nesse trabalho.

Os códigos estão em [Pickle](https://docs.python.org/3/library/pickle.html), um formato de compactação binarizada (serialização).

## Considerações
Este projeto visava apenas pôr em produção um modelo de ML, para que qualquer pessoa pudesse fazer uma requisição dele. Deste modo, o modelo em si ainda precisa passar por melhorias no seu desempenho, que não apresenta bons resultados para suas predições. Neste sentido, os próximos passos no desenvolviemento de projetos em CD é o ciclo completo, com modelo de ML funcionando com métricas desejadas.



*Fique a vontade para entrar em contato e discutir sobre esse ou outro projeto via [LinkedIn](https://www.linkedin.com/in/fernandonast/). Abs!*
