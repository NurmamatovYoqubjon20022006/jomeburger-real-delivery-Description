@echo off
echo.
echo ====================================
echo    JOMEBURGER GLOBAL DEPLOYMENT
echo         REAL-TIME MONITOR
echo ====================================
echo.

:CHECK_LOOP
echo [%TIME%] Checking GitHub Pages status...

echo.
echo 1. Repository: https://github.com/NurmamatovYoqubjon20022006/jomeburger-real-delivery-Description
echo 2. Expected URL: https://nurmamatovyoqubjon20022006.github.io/jomeburger-real-delivery-description/
echo 3. Web App URL: https://nurmamatovyoqubjon20022006.github.io/jomeburger-real-delivery-description/app.html
echo.

echo Testing URLs...

REM Test main URL
echo Testing main page...
curl -s -o nul -w "Main Page: %%{http_code}" https://nurmamatovyoqubjon20022006.github.io/jomeburger-real-delivery-description/
echo.

REM Test app URL  
echo Testing Web App...
curl -s -o nul -w "Web App: %%{http_code}" https://nurmamatovyoqubjon20022006.github.io/jomeburger-real-delivery-description/app.html
echo.

echo.
echo Status Codes:
echo - 200 = SUCCESS! (Site is live)
echo - 404 = Not found (Still deploying or Pages not enabled)
echo - 000 = Connection failed
echo.

echo Press Ctrl+C to stop monitoring...
timeout /t 30 /nobreak > nul
goto CHECK_LOOP
