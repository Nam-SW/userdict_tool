# userdict_tool
사용자 단어사전 레이블링 도구  
v0.1 기준 맥에서만 사용 가능합니다.

# 사용방법
 ![main_ui](https://github.com/Nam-SW/userdict_tool/blob/main/resources/main_ui.png?raw=true)
 1. `find`를 클릭해 따로 주어진 `.xlsx` 파일을 선택합니다.   
 2. `userdict_filename`을 수정해 저장할 userdict 파일명을 정합니다. 이때, 경로는 위의 엑셀파일과 동일한 위치에서 선택되며, 파일이 없을 경우 새 파일을 생성합니다.
 3. `setup` 버튼을 클릭해 엑셀파일과 userdict 파일을 불러옵니다.
 4. `<-`, `->`를 클릭하거나 그 우측 번호를 입력해 엔터를 눌러 row를 이동합니다. 좌우 이동은 `command + [`, `command + ]`로도 가능합니다.
 5. `input_tokens`에 추가할 단어를 입력하고 엔터를 누르면 우측 textbox에 추가됩니다. 잘못 입력했다면 `command + backspace`로 마지막 입력을 지울 수 있습니다.
 6. `save` 버튼 혹은 `command + s`를 눌러 파일을 저장할 수 있습니다. 간혹 단축키가 먹히지 않는 경우가 있으니 꼭 확인해주세요.
 7. `quit` 버튼 혹은 `command + q`를 눌러 프로그램을 종료합니다. 저장하지 않았다면 저장 후 종료합니다. 단, 좌상단의 x를 눌러 종료한다면 저장이 되지 않으니 꼭 저장을 습관화해주세요.
 