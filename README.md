

# Machine Learning Project(ISYE 6740)







### PART 1 Regression (49/50) [https://github.com/sd2beatles/MachineLearning_Mini_Projects/tree/main/Regression]

총 두 가지 project로 진행되었으며,과제기간이 너무 짧아서(4일) 제대로 교정도 못하고 허겁지겁 했던 기억이 있다.
covid-19 때문에 mid-term을 학교에서 볼 수가 없어서, 많은 과목들이 과제로 대신 제출했어야 했던 것인데 그 양이 너무 방대했다.기간은 단 일주일이고,data 역시 잘 정제된 것이 였기 때문에 기한내에 제출할 수 있었다. 사소한 실수로 인해서 1점 감점이 되었다. 

- 첫번째 과제는 이론적인 것이 대부분이였으며, cvpx 최적화 프로그래밍을 돌려서 구하는 간단한 문제여서 그렇게 어렵지 않았다.

- 두번째 과제는 실질적인 data를 이용해서, 분석하는 것이였다. 이미 회귀분석은 학부때 들었던 덕에,그렇게 어렵지 않았으며 단지 시간이 좀 더 있으었면 하는 바램이였다.같이 공부하는 동기들은 꽤나 어려웠다고 하는 것을 보고, 컴터공학을 배경을 지닌 아이들이 힘들어할 수도 있구나 하고 세삼스럽게 놀랐음. 교수님께서 작성하신 instruction 중, ridge 와 lasso 만 사용하라고 하셨는데, 그 이유를 project를 진행하면서 알 수 있었다. Hint는 unspervised learnig이라는 한글자. 정말 당혹스러웠지만, k-mean clustering을 실행한 후, 그룹이 두 개 이상으로 나뉘었고 silhouette score도 상당히 높았다.즉, 각 그룹의 특성들을 이용하여 그에 맞는 회귀를 써야 rmse가 낮게 나올 수 있는거 아닌가 생각을 했으며,이를 토대로 report를 작성했고,좋은 comment를 얻을 수 있었다. 이러한 경우에는 회귀나무(regression tree)를 이용하면 rmse가 상당히 낮아질거라 생각한다. 

- 동기 중에 data engineer에 종사햇던 친구가 apache airflow를 사용할것을 조언하여, document를 보면서 따라해봤다. parallelism, concurrency의 용어가 참 낮설었지만, 동시다발성으로 진행되는 특징이 흥미로웠다.  머신러닝 처리시간이 눈에 띄게 낮아지는 것을 알게 되었고,앞으로 자주 사용할 예정이다. 


<project 1>
 ![image](https://user-images.githubusercontent.com/53164959/114645278-1a3c5380-9d14-11eb-9410-639f8c4569ac.png)
 
 
<project 2>
![image](https://user-images.githubusercontent.com/53164959/115257116-c34ada00-a16a-11eb-9e03-a855fb38236e.png)



### PART 2 Clustering (scores 48/50)

####  1.K-means/Spectral Clustering (https://github.com/sd2beatles/MachineLearningProjectI-Interview-Preparation/tree/main/Unspervise_Learning/K-menas%2CK-medoids)_

<KOR> ISYE 6740 에서 배웠던 내용을 K-Mean 과 Spectral Clustering을 구현한것. 상당한 시간을 요구하는 과제였음. 
 
  ![image](https://user-images.githubusercontent.com/53164959/114559210-736d9e00-9ca6-11eb-9226-280b086293bd.png)

  

#### 2. Spectral Clustering_ (https://github.com/sd2beatles/Machine_Learning_Projects/tree/main/Unspervise_Learning/SpectralClustering)


#### Epilogue

<KOR> 몇 번의 online 면접에서 reject을 얻어먹고 난 후에, remote internship으로 기회를 얻었던 곳이다. 몇 회사는 국제적인 회사라고 하기에도 무례한 이유로 reject를  통보한적이 있었는데, 이유는 단순히 내 나이(37)이 인턴을 하기에는 너무 많다는 것이였다. 그 와중에 수십건의 인턴 요청중에,India에 위치한 머신러닝/딥러닝을 주로 당담하는 회사에서 연락이 왔다. 인터뷰 내용이 기본내용부터 응용, 실무과제는 머신러닝의 기본기를 테스트하는 느낌이 워낙 강했다. 이러한 점들이 낮설어 4일 동안 고생을 했던 아픈 기억이 있다. 더불어 아직까지 딥러닝 과목을 수강하지 못해서 GAN에 관련된 질문등에 적절하게 대답하지 못했다 인터뷰 담당자가 "넌 아직 석사생이니깐 깊은 topic에 대해서 대답을 못해도 괜찮다"라는 말을 듣고 안도했으며, 머신러닝은 (두 학기를 들었고 물론 많이 부족한 실력이였지만)  모니터에 가상보드를 띄어놓고 열심히 설명했던걸로 기억이 난다. 수 많은 인터뷰과제 속에서, 이것을 올려놓은 이유는 딱 세가지이다. 
  
 
  :point_right: 첫번째 
  
  크롤링을하던 api에서 데이터를 받던지 간에, 절대로 kaggle과 같은 사이트에서 data를 다운받지 말것. 또한 데이터 수집 코드를 꼭 첨부해야할 것
   
  :point_right: 두번째

다른 인턴 과제들과 차이점은, 적어도 한 머신러닝 tool을 외부 library없이, 직접 파이썬으로 구현을 해야한다는 한다는 의무사항이 있었다.K-means는 너무 자주 사용하다 보니깐, 
수업에 배웠던 spectral clustering과 DBSCAN등의 기법을 사용했는데, 그래서인지 인터뷰의 내용 또한 주로 비지도 학습에 관련된거 였다.
 
  
  :point_right: 세번째
  
  기간이 4일동안, 데이터 수집 -> 정제 -> 머신러닝 구현->분석을 하기에는 턱없는 시간이였다. 시간이 충분했다면, 빅데이터 수업에서 배웠던 hive를 사용하고 싶었는데아쉽다는 생각이 지금까지도 든다. 시간에 쫒겨, 시간의 모든 부분을 수집->정제에 들었으므로 분석이 다소 미약하다는 점은 어쩔 수가 없다는 것이 눈에 띈다.
  
  

### PART 3 Dimension Reduction (scores 50/50)

#### PCA (https://github.com/sd2beatles/MachineLearningProjectI-Interview-Preparation/tree/main/Dimesion_Reduction)

머신러닝 과목 중에서 처음으로 배웠던, 차원축소 방법을 자신의 코드로 구현해야하는 과제였다. 두 개의 차원으로 축소시킨 뒤에, 군집화를 실행시켰으나 
의미없는 결과를 도출하게 됨. silhouette score도 작았으며, 육안상으로도 군집화의 의미가 없었다. 추 후에 안것이지만, 군집화를 실행시키지 않는 것이 
더 좋은 점수를 얻을 수 있었다. 상당히 쉬운 과제였고, LDA VS PCA 사용법에 관한 책을 읽은 적이 있었는데, 그 부분에 대해서 더 공부할 필요가 있다고 판단했음.

![image](https://user-images.githubusercontent.com/53164959/114645574-b2d2d380-9d14-11eb-8546-3a19f4b2e993.png)


#### ISOMAP (https://github.com/sd2beatles/MachineLearningProjectI-Interview-Preparation/tree/main/Dimesion_Reduction)

일단 개념자체를 이해하는데, 시간이 너무 오래걸렸다. 사실 100% 이해를 하지 못한 상태에서,과제 제출기간은 다가오고 부랴부랴 구글에서 검색해서
자료를 올렸다. 일단, network의 알고리즘 floyd라던지 dijkextra라는 생소한 알고리즘은 구현하지 못한채, sklearn에  의존해서 제출을 했음. 일단 감점은 없었으나, 내 자신이  직접 구현하지 못한것에 대해선 반성하고 다음에 시간있을 때,제대로 구현해 볼 예정임. 

![image](https://user-images.githubusercontent.com/53164959/113539120-f4c69000-9617-11eb-8aa7-9d4e90dbce79.png)










