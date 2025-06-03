# 📄 Documentação L1 — Stress App

## 📌 Visão Geral  
O **Stress App** é uma ferramenta que permite desenvolvedores testarem a resiliência e capacidade de resposta de suas aplicações por meio de requisições simultâneas controladas. Ele ajuda a identificar gargalos e limitações de infraestrutura de forma prática e automatizada.

## 🎯 Objetivo  
Oferecer um mecanismo simples para que usuários possam submeter suas aplicações a cenários de carga e identificar o comportamento sob alta demanda, facilitando a avaliação de desempenho e estabilidade.

## ⚙️ Funcionalidades  

### 1️⃣ Testar a capacidade de resposta de uma aplicação via requisições múltiplas

- **O que permite?**  
  Permite que o usuário dispare múltiplas requisições HTTP para um endpoint de sua aplicação, simulando carga.

- **Como usar?**  
  Realize uma requisição HTTP `POST` para o endpoint `/dispatch` do Stress App, informando:
  - A URL da aplicação alvo.
  - A quantidade de requisições desejadas.

- **Requisitos / Parâmetros:**
  - `url` (string) → endereço completo da aplicação alvo.
  - `quantityRequest` (inteiro) → número de requisições a serem disparadas.
  - `file` (opcional) → arquivo a ser enviado junto das requisições (se necessário para o teste).

## 🔄 Fluxo de Funcionamento  

### 📌 Ação: Realizar teste de carga na aplicação alvo.

**1.** Usuário define o endereço da aplicação e a quantidade de requisições.  
**2.** Usuário realiza uma requisição `POST` para:

```
POST /dispatch
```

**Body (JSON ou multipart/form-data):**
```json
{
  "url": "https://minhaaplicacao.com/api/teste",
  "quantityRequest": 4000,
  "file": "<arquivo-opcional>"
}
```

**3.** O Stress App processa a quantidade solicitada de requisições para a URL informada.  
**4.** Retorna resposta:

```
Dispatch 4000 requests
```

**Importante:**  
Atualmente, o Stress App **não retorna informações detalhadas de desempenho** ou métricas das requisições realizadas, apenas confirma a execução.

## 📊 Impacto no Projeto  

1. Permite identificar falhas e limitações sob alta carga.
2. Auxilia no planejamento de escalabilidade e melhorias de infraestrutura.
3. Oferece uma ferramenta rápida para simular cenários críticos de forma controlada.
4. Facilita a validação de endpoints críticos em ambientes de homologação e produção.

## 🔌 Integrações  

Nenhuma integração externa implementada atualmente.

## 💡 Melhorias Futuras (Roadmap)

1. Implementar serviço de métricas, exibindo:
   - Tempo médio de resposta.
   - Quantidade de falhas.
   - Percentual de sucesso.
2. Permitir configuração de diferentes tipos de requisições (GET, POST, PUT, DELETE).
3. Adicionar níveis de logs para rastrear o status das execuções.
4. Implementar log rotativo para evitar arquivos de log muito grandes.
5. Adicionar autenticação para controle de acesso.
