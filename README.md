# Mini Port Scanner + Dashboard

**Mini Port Scanner + Dashboard**
Scanner de portas TCP com interface web em Flask, feito para portfólio.
Escaneia portas (IPv4/IPv6), usa `ThreadPoolExecutor` para paralelizar I/O e tenta capturar banners simples. Ideal para demonstrar conhecimentos de redes, Python e integração com web.

---

## 📌 Tópicos
* [Aviso legal / Ética](#aviso-legal--ética)
* [Sobre](#sobre)
* [Motivação](#motivação)
* [Funcionalidades](#funcionalidades)
* [Pré-requisitos](#pré-requisitos)
* [Instalação](#instalação)
* [Uso](#uso)
* [Exemplo de saída](#exemplo-de-saída)
* [Exportar resultados](#exportar-resultados)
* [Design e decisões técnicas](#design-e-decisoes-técnicas)
* [Contribuição](#contribuição)
* [Inspiração](#inspiração)

---
## ⚠️ Aviso legal / Ética

**Importante:** só escaneie hosts e redes **dos quais você é proprietário** ou onde você tem **autorização explícita**. Escanear sistemas alheios sem permissão é ilegal. 

---
## 🔍 Sobre

Pequeno projeto didático que combina:

* programação de sockets em Python (stdlib);
* paralelismo para I/O (threads);
* interface web simples com Flask para iniciar scans e visualizar resultados;
* exportação de resultados em JSON — tudo pensado para incluir no portfólio.

---

## 🎯 Motivação

Objetivo: demonstrar entendimento prático de operações de rede (sockets), otimização I/O (threads) e construção de uma interface web para automação e visualização de dados.

---

## ✅ Funcionalidades

* Suporte a IPv4 e IPv6 (usa `socket.getaddrinfo`).
* Escaneamento paralelo configurável (`threads`).
* Tentativa de leitura de banner (quando o serviço responde).
* Interface web (Flask) com formulário para host/portas/timeout/threads.
* Exportar resultados em JSON para análise posterior.
* Limites aplicados no front-end para evitar scans gigantes acidentais.

---

## ⚙️ Pré-requisitos

* Python 3.8+
* Dependências (instalar via pip):

```bash
pip install -r requirements.txt
# requirements.txt contém:
# flask
```

---

## 🛠️ Instalação (rápido)

1. Clone o repositório:

```bash
git clone <url-do-seu-repo>
cd scanPort
```

2. Crie e ative um virtualenv:

```bash
python -m venv venv
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Linux / macOS
source venv/bin/activate
```

3. Instale dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como rodar (local)

1. Certifique-se de estar na pasta do projeto e com o venv ativado.
2. Execute:

```bash
python app.py
```

3. Abra no navegador:

```
http://127.0.0.1:5000/
```

> Se quiser acessar de outro dispositivo na mesma rede, rode `app.run(host="0.0.0.0", port=5000)` e acesse `http://<SEU_IP_LOCAL>:5000/`.

---

## 🧭 Uso

* No campo **Host/IP**: informe `127.0.0.1`, `::1`, `192.168.x.x` ou domínio (ex.: `example.com`).
* **Ports**: intervalo (`20-1024`) ou lista (`22,80,443`).
* **Threads**: ajuste conforme sua máquina (50–300 recomendado).
* **Timeout(s)**: tempo de espera por porta (0.4–2.0).
* Clique em **Scan** e aguarde. Para scans maiores, use o modo em background (se implementado) para não bloquear o navegador.

---

## 📎 Exemplo de saída (formato JSON)

```json
{
  "host": "192.168.0.1",
  "scanned_ports": 100,
  "elapsed": 3.66,
  "results": [
    {"port": 22, "open": false, "banner": "", "error": null},
    {"port": 80, "open": true, "banner": "HTTP/1.1 200 OK ...", "error": null}
  ]
}
```

---

## 💾 Exportar resultados

Use o link **Exportar JSON** na interface (ou acesse `/export.json`) para baixar o último resultado como `scan_results.json`.

---

## 🧠 Design e decisões técnicas

* **Por que threads?** Escanear portas é uma operação I/O-bound (espera de rede). Threads aumentam simultaneidade e reduzem tempo total sem complicar com async.
* **`getaddrinfo`**: usado para suportar IPv4 e IPv6 de forma transparente.
* **Limites**: por segurança e para evitar sobrecarregar a rede/host, o front-end e o servidor impõem limites (max portas / max threads).
* **Não realiza UDP** (somente TCP) e não faz fingerprinting profundo — integração com `nmap` é sugestão futura.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sugestões:

1. Abra uma *issue* descrevendo a melhoria.
2. Faça um fork, crie uma branch `feature/my-change` e submeta um PR.
---

## Contato

Davi Sousa
<p align="left">
    <a href="https://www.linkedin.com/in/davisousavilela">
        <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>
    <a href="https://github.com/fireone-Ops">
        <img alt="GitHub" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
    </a>
</p>
