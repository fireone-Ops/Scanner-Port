# Mini Port Scanner + Dashboard

Scanner de portas TCP com interface web desenvolvido em Python e Flask. O projeto permite escanear portas em hosts IPv4 e IPv6, utilizando paralelismo com `ThreadPoolExecutor` para otimizar operações de rede e capturar banners de serviços quando disponíveis.

> **Aviso:** Este projeto foi desenvolvido para fins educacionais e de demonstração. Utilize-o apenas em redes e sistemas onde você possua autorização para realizar testes.

---

## Tecnologias

- Python
- Flask
- Socket
- ThreadPoolExecutor

---

## Funcionalidades

- Escaneamento de portas TCP.
- Suporte a IPv4 e IPv6.
- Paralelismo utilizando `ThreadPoolExecutor`.
- Captura de banners de serviços.
- Interface web desenvolvida em Flask.
- Exportação dos resultados em JSON.
- Configuração de timeout e quantidade de threads.
- Limites de segurança para evitar escaneamentos excessivos.

---

## Estrutura do Projeto

```text
.
├── app.py
├── scanner.py
├── templates/
├── static/
├── requirements.txt
└── README.md
```

---

## Requisitos

- Python 3.8+

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Como executar

Clone o repositório:

```bash
git clone https://github.com/fireone-Ops/scanPort.git
```

Entre na pasta:

```bash
cd scanPort
```

Crie um ambiente virtual (opcional):

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python app.py
```

Acesse:

```text
http://127.0.0.1:5000
```

---

## Funcionamento

O usuário informa:

- Host ou endereço IP.
- Intervalo de portas ou lista personalizada.
- Quantidade de threads.
- Timeout.

Após iniciar o escaneamento, o sistema verifica cada porta TCP e apresenta os resultados diretamente na interface web.

Também é possível exportar o resultado em formato JSON.

---

## Exemplo de saída

```json
{
  "host": "192.168.0.1",
  "elapsed": 3.66,
  "results": [
    {
      "port": 22,
      "open": false,
      "banner": ""
    },
    {
      "port": 80,
      "open": true,
      "banner": "HTTP/1.1 200 OK"
    }
  ]
}
```

---

## Arquitetura

```text
Usuário
      │
      ▼
 Interface Flask
      │
      ▼
 Scanner TCP
      │
      ▼
ThreadPoolExecutor
      │
      ▼
Sockets TCP
      │
      ▼
Resultados
      │
      ▼
 Dashboard / JSON
```

---

## Melhorias Futuras

- Escaneamento UDP.
- Fingerprinting de serviços.
- Histórico de escaneamentos.
- Exportação em CSV e PDF.
- Dashboard com gráficos.
- Autenticação de usuários.
- Docker.
- API REST.
- Integração com Nmap.

---

## Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos como:

- Programação de redes.
- Sockets TCP.
- IPv4 e IPv6.
- Concorrência com ThreadPoolExecutor.
- Desenvolvimento Web com Flask.
- Comunicação cliente-servidor.
- Exportação de dados em JSON.
- Estruturação de aplicações Python.

---

## Aviso de Uso

Este projeto possui finalidade exclusivamente educacional.

Não utilize o scanner em equipamentos, servidores ou redes sem autorização explícita do proprietário.

---

## Autor

<p align="left">
  <a href="https://github.com/fireone-Ops">
    <img alt="Davi Sousa" src="https://img.shields.io/badge/Davi%20Sousa-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>
