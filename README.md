# API Timezone
---
**Visão geral:** Este projeto consiste na API RESTful "Timezone" com o Swagger, num container Docker. 

**Objetivo:**    Essa aplicação possibilita obter o fuso horário nacional do usuário de acordo com seu CEP.

&nbsp;

---
### REQUERIMENTOS
A API Timezone está integrada à API PyCEPCorreios para consulta de endereço a partir do CEP. Ademais, a API possui integração às bibliotecas subcitadas:
* GeoPy: localiza as coordenadas de um endenreço
* TimezoneFinder: busca o fuso horário local conforme as coordenadas do usuário


&nbsp;

---
### EXECUÇÃO
Para executar esta aplicação, basta compilar o Docker e executar o mesmo por meio dos comandos **docke-compose buid** e **docker-compose up**.

&nbsp;

---
### A API foi desenvolvida por meio do tamplate disponibilizado pelo Patrick.  
* Link de acesso ao template: https://github.com/PatrickLdA/swagger_api

&nbsp;

---
