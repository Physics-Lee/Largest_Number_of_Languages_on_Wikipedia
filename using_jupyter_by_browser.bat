@echo off
REM 启动 D:\Public_Repositories 下的 Jupyter Lab

echo Activating conda environment...
CALL conda activate base

echo Changing directory to D:\Public_Repositories...
D:
cd D:\Public_Repositories

echo Starting Jupyter Lab...
jupyter lab

pause