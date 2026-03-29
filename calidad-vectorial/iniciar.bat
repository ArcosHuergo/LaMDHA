@echo off
title Iniciar proyecto
cd /d "%~dp0"
echo =============================
echo    Iniciando Bucher...
echo =============================

REM --- BACKEND ---
echo Iniciando backend...
cd backend/app
start cmd /k "uv run uvicorn main:app --reload"
cd ..