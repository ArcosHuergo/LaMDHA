@echo off
title Iniciar proyecto
cd /d "%~dp0"
echo =============================
echo    Iniciando GeoHuergo...
echo =============================

REM --- BACKEND ---
echo Iniciando backend...
cd backend
start cmd /k "uv run uvicorn app.main:app --reload"
cd ..

REM --- FRONTEND ---
timeout /t 5 /nobreak >nul
echo Iniciando frontend...
cd frontend
start cmd /k "npm run dev"
cd ..