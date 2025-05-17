# Princípios SOLID em Python

## Demonstração prática dos princípios SOLID aplicados com Python orientado a objetos

[![Python](https://img.shields.io/badge/Python-Linguagem-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![POO](https://img.shields.io/badge/Paradigma-OO-orange?style=flat-square&logo=apachespark&logoColor=white)](https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_orientada_a_objetos)
[![SOLID](https://img.shields.io/badge/Princípios-SOLID-8E44AD?style=flat-square&logo=bookstack&logoColor=white)](https://en.wikipedia.org/wiki/SOLID)

---

## O que é SOLID?

**SOLID** é um acrônimo para cinco princípios da programação orientada a objetos que ajudam a criar sistemas mais coesos, desacoplados, reutilizáveis e fáceis de manter.

---

## Princípios Demonstrados

### 1. Single Responsibility Principle (SRP)
> Uma classe deve ter apenas um motivo para mudar.

Arquivo: `single_responsibility_principle.py`  
Demonstra a separação entre responsabilidades: `Usuario`, `Pedido` e `Notificador` são classes independentes.

---

### 2. Open/Closed Principle (OCP)
> Entidades devem estar abertas para extensão, mas fechadas para modificação.

Arquivo: `open_closed_principle.py`  
Novos processadores de pagamento podem ser criados sem modificar as classes existentes.

---

### 3. Liskov Substitution Principle (LSP)
> Objetos da superclasse devem poder ser substituídos por objetos da subclasse sem quebrar o código.

Arquivo: `liskov_substitution_principle.py`  
Substituições entre `EntregaNormal` e `EntregaExpressa` funcionam sem impacto na função cliente.

---

### 4. Interface Segregation Principle (ISP)
> Nenhum cliente deve ser forçado a depender de métodos que não utiliza.

Arquivo: `interface_segregation_principle.py`  
As classes `NotificadorEmail` e `NotificadorSMS` implementam apenas a interface que usam.

---

### 5. Dependency Inversion Principle (DIP)
> Dependa de abstrações, não de implementações concretas.

Arquivo: `dependency_inversion_principle.py`  
O sistema de pedidos depende da abstração `ProcessadorDePagamento`, o que permite mudar a lógica sem alterar a estrutura.

---
