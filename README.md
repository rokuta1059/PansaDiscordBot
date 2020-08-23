# PansaDiscordBot

## 새롭게 개편중인 판화사랑 디스코드 봇

- :rainbow: 이전 버전 링크는 [여기 클릭](https://github.com/rokuta1059/PansaDiscordBot_old)
- 이전에 제작한 PansaDiscordBot을 조금씩 개편하고 기능을 수정한 버전

## :mobile_phone_off:**아직 공사중입니다!!!!**:mobile_phone_off:

- 아주 조금씩 기존 기능을 가져오는 중이기 때문에 완전하지 않습니다
- 지금 당장 기동시켜도 실행만 되는 수준입니다

## 기존 버전과의 차이점

1. Client 방식을 Bot 방식으로 변경

    ```python
    async def on_message(message):

        if message.content.startswith('!망언'):
    ```
    - 기존 방식의 경우 `on_message`를 이용하여 `if`문을 나열하여 커맨드를 판단하고 실행
    - `prefix`를 설정하지 않아도 되므로 다양한 커맨드를 사용할 수 있다는 장점이 있음
    - `if`문을 나열한 문장이므로 가독성이 매우 떨어지며, 커맨드 수정도 어려움

    ```python
    @bot.command(name='도움')
    async def bot_help(ctx):
    ```
    - 새로운 방식의 경우 `@bot.command` Annotation을 활용하여 커맨드를 저장하고, 함수를 구현하여 구동한다
    - 가독성이 좋고, 주석을 활용할 수 있어 필요한 커맨드를 바로 찾고 빠른 수정이 가능하다

2. 파일 구조 변경

    - 기존 방식의 경우 `run.py`와 `fairyfunc.py`로 구분되어 각각 실행 시 부분과 함수 부분이 구분되어 있음
    - 각각의 함수가 어디에 있는지 바로 판단이 어려움
    - 새로운 방식의 경우 모듈을 각각 나누어 각각의 기능별로 모듈을 두어 추가 및 수정이 용이하도록 구성

3. 토큰 수정

    - 기존 방식의 경우 하드코딩이 되어 있어 `Commit`시 토큰이 같이 업로드되는 문제가 있었음
    - 새로운 방식의 경우 파일을 따로 두고 해당 파일을 읽어서 토큰을 등록하도록 하여 하드코딩을 하지 않도록 함