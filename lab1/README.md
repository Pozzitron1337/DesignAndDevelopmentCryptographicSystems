# Design And Development Cryptographic Systems. Laboratory work 1 

## task:

Розробити програмний засіб захисту логічного каналу зв’язку, що використовує протокол TLS (версія 1.2). Програмний засіб повинен мати клієнт-серверну архітектуру, в якій клієнт повинен бути орієнтованим на операційні системи та платформи для мобільних телефонів та планшетних комп’ютерів. Дозволяється використання бібліотеки OpenSSL – реалізації з відкритим кодом.

Клієнт має підтримувати ОС Android 4.0 або вище, або ОС iOS 7.0 або вище. Серверна частина має підтримувати ОС Windows (версія ядра не менша за 6.1).

Програмний засіб має реалізовувати автентифікацію обох сторін згідно з протоколом TLS. Реалізація протоколу має детально відображати процес формування нового сеансу та відновлення існуючого (має відображатися кожен з типів пакетів, його вміст та всі параметри протоколу як на клієнті, так і на серверній частині), включаючи процес перевірки сертифікатів. Програмний засіб має надавати змогу користувачу безпосередньо впливати на цей процес з кожної із сторін, а саме блокувати перевірку сертифікатів, задавати конкретні значення випадкових змінних, задавати та згодом змінювати криптографічні методи, що використовуються. Після встановлення логічного каналу зв’язку програмний засіб повинен дозволяти проводити обмін довільними повідомлення за цим каналом.
Коректність релізації необхідно підтвердити за допогою використання програми для перехоплення та аналізу пакетів – Wireshark. Також необхідно продемонструвати атаку sslstrip на власну реалізацію протоколу (можна використовувати допоміжні програми) та обгрунтувати результати застосування.

Main info was investigated from this articles:
1. https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

# Instatiating

install libs:
```
pip3 install socket
pip3 install ssl
pip3 install flask
pip3 install pyopenssl
```

Create server sertificate:
```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

snapshot of terminal:
```
ippolit@MacBook-Pro-ippolit ~/University/DesAndDevCryptoSystems/lab1 % openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
Generating a 4096 bit RSA private key
...........++
.......++
writing new private key to 'key.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) []:UA
State or Province Name (full name) []:KYIV
Locality Name (eg, city) []:KYIV
Organization Name (eg, company) []:KPI
Organizational Unit Name (eg, section) []:KPI
Common Name (eg, fully qualified host name) []:KPI
Email Address []:the.vaho1337@gmail.com
```

run server:
```
python3 server.py
```

open separate terminal and run client:
```
python3 client.py
```