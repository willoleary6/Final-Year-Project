
SETLOCAL ENABLEDELAYEDEXPANSION
SET count=1
FOR /F "tokens=* USEBACKQ" %%F IN (`protoc.exe`) DO (
  SET var!count!=%%F
  SET /a count=!count!+1
)
IF "%var1%"=="" (
   set /p id="protoc is not in the PATH, please download the file from the following webpage and add protoc-3.6.0-win32\bin\ folder to PATH"
   start microsoft-edge:https://github.com/protocolbuffers/protobuf/releases/download/v3.6.0/protobuf-python-3.6.0.zip
   PAUSE
)