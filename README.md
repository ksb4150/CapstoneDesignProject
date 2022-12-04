# CapstoneDesignProject (커넥티드 카 내부 네트워크 패킷 자동 분류 및 이상탐지 기술 개발)

### 1. 개발 이유
 현재 보편화 된 커넥티드 카는 차량 내부의 모듈 및 컨트롤러와 통신하기 위해 CAN 통신 프로토콜을 주로 이용하고 있다. 그러나 CAN은 데이터의 기밀성을 보장하는 보안 설계가 되어있지 않으며 암호화를 하고있지 않으므로 공격자가 악의적으로 데이터를 도청 및 재생 공격할 수 있다. 
 때문에 CAN 메시지를 분석하고 탐지하는 연구는 최근 AI와 더불어 활발히 이루어지고 있다. 그러나 CAN 메시지 분석 과정에서 차량마다 또는 제조사마다 CAN ID가 상이하고 식별되지 않아 난항을 겪고있다. 해당 프로젝트는 이러한 이유로 인해 CAN 데이터를 수집한 이후 분석방법을 제시하고 분석 시간을 단축하기 위한 알고리즘과 악의적인 데이터를 탐지하기 위한 알고리즘을 제안한다.

### 2. 개발환경
* Pycharm
* PCAN-VIEW
* My-SQL
* JavaScript
* HTML

### 3. 설계
### 시나리오
![image](https://user-images.githubusercontent.com/74931459/205486328-b26fa054-0b9f-4107-b660-c690ad24e286.png) <br>
 수집 시작 후 10초 동안은 시동을 킨 채 아무런 행위도 하지 않는다. 이때 저장되는 값들을 초기 데이터라 하고 이후 특정 구간에서의 값과 비교할 기준으로 사용
 10초 후 우측 방향 지시등을 키면서 도로에 진입
 30초가 되면 우측 방향 지시등을 키고 자동차 전용도로에 진입
 50초에 좌측 방향 지시등을 켜서 차로를 변경
 1분일 때 크루즈 컨트롤을 ON 후 7분 30초일 때 OFF
 5분일 때 20초 등안 비상등을 ON 후 8분이 되는 시점 OFF
 8분일 때 엑셀을 밟아 급가속 후 15초 이후 브레이크를 밟아 감속
 8분 40초에 수집 종료
 
 ### 모니터링 페이지
 ![image](https://user-images.githubusercontent.com/74931459/205486431-4c75f34e-0886-4966-b728-782d3ad9b693.png) <br>
 주행 중 수집한 CAN 데이터의 매 순간 변화량을 차트로 시각화 한 것이다. 상단의 분홍색 바 안의 숫자는 현재 초이며 오른쪽에 있는 단어는 현재 수햍하고 있는 행위이다. 상단 오른쪽에 있는 result page 버튼은 데이터의 변화량을 기반으로 분석 및 유추된 특정 기능별 ID의 결과를 볼 수 있는 이동 버튼이다.
![image](https://user-images.githubusercontent.com/74931459/205486438-e607a983-9f85-41ca-80be-f812564c922e.png) <br>
 특정 시간 대에 발생한 ID와 ID 데이터의 변화량을 분석한 결과를 표의 형태로 나타낸 페이지이다. A 사의 커넥티드 카를 기준으로 측 방향 지시등 아이디 유추는 97.7%, 우측 방향 지시등 2는 95.2%, 좌측 방향지시등은 97.7%, 비상등은 96.4%, 엑셀은 75%, 브레이크는 96.4%의 정확도를 보였다.
 ![image](https://user-images.githubusercontent.com/74931459/205489840-562fe019-8e4d-47b3-a921-e1ea9262c785.png) <br>
 이상 데이터라 판별하는 기준은 다음과 같다. CAN ID별 가장 많이 수집된 데이터의 개수와 비교하여 1% 이하의 데이터가 들어온 ID는 이상 데이터로 판별된다. CAN 데이터는 커넥티드 카가 시동이 걸린 이후로 부터 계속해서 수집되는 데이터이지만 이상 데이터의 경우 특정 구간, 시간에서만 들어오기 때문에 그 수가 적을 수 밖에 없기 때문에 이를 기준으로 하였다.
