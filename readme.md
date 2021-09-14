# SSH Tunel

- Tenha o python instalado
- configure o arquivo conf.json indicando as portas que deseja criar o tunel
- preencha também seu usuario e senha

para abrir as conexões execute o comando
```sh
python main.py
```

para fecha-las
```sh
python main.py stop
```
```sh
"tunel": 
    [
        {
            "nome":"vv-crm",
            "porta": "8084",
            "ip": "10.128.145.9" #IP do tunelamento
        }
    ]
```
```sh
"user":"USUARIO",
"pass":"SENHA",
"ip":"10.128.145.9" #IP da conexão
```
