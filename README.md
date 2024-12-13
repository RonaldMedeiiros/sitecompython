# Fake Pinterest

Aplicação feita em Python, usando Flask como Framework e sqlite como banco de dados, rodando em um docker na porta 5020, via link http://portfolio.mosetech.com.br:5020. 

Entre, crie o usuário e envie imagens em seu perfil. 

Ná página inicial, você pode ver todos as imagens enviadas, tanto por você quanto por outros usuários.

## Rodando com Docker

- Buildando a imagem

```bash
docker build -t sitecompython .
```

- Executando o Container

```bash
docker run -d -p 5010:5010 sitecompython
```

Após rodar, entrar em http://localhost:5010 

## Para rodar sem o Docker

- Iniciar o ambiente virtual do python no terminaal:

```bash
python -m venv venv
```
```bash
./venv/script/activate
```

- Após ativar, instalar os pacotes:

```bash
pip install requirementes.txt
```

- Rodando a aplicação:

```bash
python main.py
```

Aplicação feita junto com o Curso da Hashtag, porém com algumas atualizações pois os módulos estavam desatualizados.


