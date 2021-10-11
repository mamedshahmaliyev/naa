@echo off
SET /a a=%2
SET /a b=%3
if "%1"=="sum" set /a c=%a%+%b%
if "%1"=="add" set /a c=%a%+%b%
if "%1"=="subtract" set /a c=%a%-%b%
if "%1"=="sub" set /a c=%a%-%b%
if "%1"=="multiply" set /a c=%a%*%b%
if "%1"=="mult" set /a c=%a%*%b%
if "%1"=="product" set /a c=%a%*%b%
if "%1"=="divide" set /a c=%a%/%b%
if "%1"=="div" set /a c=%a%/%b%
echo %c%