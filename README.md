# delivery
Sistema de Delivery Modelo SAAS Base.



Dados Técnicos:

- Python: 3.12.2
- Django: 5.1.1
- SGBD: Qualquer banco de dados compatível com Django.


Gerar variável de ambiente com padronização:

Esse comando aqui você tem que executar com a venv ativada no terminal, para gerar arquivo local .env *ignorado no git
- executar "python contrib/env_gen.py" 

O arquivo .env gerado pelo env_gen.py tem variáveis que controlam modo Desenvolvimento / Produção, controle de Redis Cache e serviço de email e Secret Key.

Exemplo de definição do banco de dados no arquivo .env
- DATABASE_URL=mysql://root:@localhost:3306/nomedobanco
- Colocar a senha apos o root:

Para criar novos Apps:
- Entre no caminho digitando "CD sitecore\apps" no terminal
- Digite o comando padrão django-admin startapp nomedoapp
- Sempre volte para o caminho original usando cd .. até o pasta principal auto_store para poder rodar o projeto novamente.