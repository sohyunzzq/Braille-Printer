# 💡 점자 번역 프린터  
![image](https://github.com/user-attachments/assets/3592ab4a-941b-4ef4-9080-a84da1bf5314)

---

## 📌 개요  

사용자가 문자를 입력하면 그 문자를 점자로 변환한 뒤, 솔레노이드를 돌출시켜 한 글자씩 해당 점자를 출력한다. 시각장애인이 손으로 직접 촉지하며 문자를 읽을 수 있도록 설계된 점자 번역 프로젝트이다.  

---

## 🔍 개발 배경  
 - 우리 사회에는 여전히 장애인을 위한 복지의 사각지대가 존재하며, 특히 시각장애인의 정보 접근권은 충분히 보장받지 못하고 있다. 우리는 그중에서도 점자 표기의 부족이 시각장애인의 일상에 큰 제약이 된다는 점에 주목하였다. 이에 따라, 언제 어디서든 원하는 문구를 점자로 변환해 출력할 수 있는 '점자 번역 프린터'를 설계하게 되었다.
 - 점자 번역 프린터는 입력된 문구를 점자로 변환한 뒤 종이에 인쇄하여 즉각적이고 실질적인 활용이 가능하도록 고안되었다. 이를 통해 점자 표기가 없는 물건이나 장소에도 점자 스티커를 직접 부착함으로써 기존의 미흡한 점자 표기를 보완하는 도구로 활용하는 것을 궁극적 목표로 개발에 임하였다. 그러나 개발 중 여러 제약으로 인해 종이 없이 손바닥으로 바로 감지할 수 있는 촉각 기반 점자 출력 장치로 최종 결정하였다.  

---

## 🛠 사용 기술 및 개발 환경  
- 언어: Python, C++ (Arduino)  
- 하드웨어: Arduino UNO   
- 툴: Arduino IDE, PyCharm, Cura (3D Printing)  

---

## 🧱 사용 부품  
- Arduino UNO
- 1.5V AAA배터리 24개, 배터리 홀더
- 솔레노이드 6개
- 릴레이 모듈 6개

---

## ⚙️ 환경 설정  
### HW
- Arduino UNO의 Digital Pin 6개와 솔레노이드 연결
### SW
- 연결한 Digital Pin 번호에 따라 brai.ino의 pins 배열 수정
- Arduino에 연결한 포트 번호에 따라 user.py의 PORT 변수 수정

---

## 🚦 작동 순서  
1. 📝 사용자의 문자열 입력  
2. 🐍 파이썬: 문자열 → 점자 변환  
3. 📤 점자 번호 리스트 → 시리얼 전송  
4. 🧠 아두이노: 번호 수신  
5. ⚙️ 핀 HIGH → 솔레노이드 작동 → 점자 돌출  
6. ✋ 손으로 점자 인식  

---

## 🧰 제작 과정  
![image](https://github.com/user-attachments/assets/07178ada-bafa-47cc-a50a-4bc741d99e6f)
![image](https://github.com/user-attachments/assets/4a533e03-6ad1-4b87-a81e-f8e9b0a84138)

![image](https://github.com/user-attachments/assets/c9c3ad43-f512-47d1-bd7b-18b3fea5631f)
![image](https://github.com/user-attachments/assets/5bd896d2-0d3c-4b73-8453-5fea8d48b1d5)

- 3D프린터로 몸체 제작 후 조립
- 배터리를 배터리 홀더에 연결 후 릴레이 모듈과 납땜
- 솔레노이드 6개를 3행 2열 형태로 부착
- 릴레이 모듈을 각 솔레노이드와 연결해 납땜
- 위 부품들을 몸체 아래에 배치

---

## 📁 디렉터리 구조

```
├── docs/
│   └── dev-log.md    
├── README.md
├── brai.ino
└── user.py
```

---

## 🚀 실행 방법  
1. Arduino 연결 후 brai.ino 업로드 (시리얼 모니터가 열려 있으면 실행이 되지 않으므로 꼭 닫아주기)
2. PyCharm에서 user.py 실행 후 문자열 입력
3. 솔레노이드 작동 확인
 
---

## 🏆 성과
- 프로젝트 완성 후, 12월에 동아리 자체 행사로써 프로젝트 전시 및 발표

---

## 💭 한계  
- 입력된 문구를 점자로 출력하기 위해 여러 방법을 시도해보았으나, 최종적으로는 촉각 기반 출력 장치로 방향을 전환하게 되었다. 관련 시도 및 시행착오는 [dev-log.md](docs/dev-log.md)에 적어두었다. 
- 한글 점자 체계는 구조가 매우 복잡하여 구현에 어려움이 있었기 때문에, 현재는 영문 소문자와 일부 문장 부호에 한해 점자 변환이 가능하도록 구현하였다.

---

## 📚 참고 자료
- Arduion UNO pin map
  
![image](https://github.com/user-attachments/assets/6f5a1a7b-1715-4d97-b8a0-a25e3f4411ce)
- 점자일람표
  
![image](https://github.com/user-attachments/assets/fd2986c2-bce5-44db-9058-67bc18e1bf90)
