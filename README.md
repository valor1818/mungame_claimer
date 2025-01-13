To configure the script, you must obtain an authentication key for your account.

1. Log in to your Telegram account from the web version. (https://t.me/MunGameBot)
2. Launch “Developer Tools” (F12 key), in the opened window find the “Network” window and open it.
3. Start the game, click the “Earn” button to get the points earned.
4. In the opened window there will be a new value “Gathering”, open it. Under “Request-Headers” find the value “Authorization” and copy it.
5. Open the config.ini file and paste your key there in the “SECRET” value.
6. Open “cmd.exe” on your Windows, or other bash, and type “pip install requests”.
7. Run the app.py file.
