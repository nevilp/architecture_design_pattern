1. Layered (N-Tier) Architecture
Definition: Organizes software into layers like Presentation, Business, and Data Access.
Use Case: Enterprise apps, CRUD systems.
Microproject: Web API (FastAPI) -> Service Layer -> SQLite DB.

2. Client-Server Architecture
Definition: Splits system into client (frontend) and server (backend).
Use Case: Web apps, chat apps.
Microproject: Flask server and React or Python CLI client that sends/receives data.

3. Event-Driven Architecture (EDA)
Definition: Components communicate via events (producers/consumers).
Use Case: Real-time systems, IoT.
Microproject: Sensor simulator publishing events (RabbitMQ), processor consuming and saving to DB.

4. Microservices Architecture
Definition: System broken into independent services that communicate via APIs.
Use Case: Scalable web apps, fintech.
Microproject: User service, Order service, Product service — all in FastAPI with Docker.

5. Monolithic Architecture
Definition: Entire application is a single unit.
Use Case: Simple, small applications.
Microproject: Blog app with user registration, post creation, all in one Flask app.

6. Service-Oriented Architecture (SOA)
Definition: Like microservices but uses ESB (Enterprise Service Bus) to coordinate.
Use Case: Large enterprises integrating legacy systems.
Microproject: SOAP/RESTful services exchanging messages via a central Flask ESB layer.

7. Pipe and Filter Architecture
Definition: Data passes through processing steps (filters) connected by pipes.
Use Case: Compilers, data transformation.
Microproject: ETL pipeline: CSV → Clean → Transform → Store in DB.

8. Broker Architecture
Definition: Mediator (broker) handles communication between components.
Use Case: Distributed systems.
Microproject: RPC-style system: client requests → broker → service → result.

9. Hexagonal Architecture (Ports and Adapters)
Definition: Core logic is isolated; interactions happen via ports/adapters.
Use Case: Domain-driven apps needing strong testability.
Microproject: Book catalog with domain logic, CLI & REST adapters, DB adapter.

10. Batch Processing Architecture
Definition: Processes large volumes of data periodically.
Use Case: Reporting, billing.
Microproject: Hourly script to pull data from SQLite, generate Excel report, and email it.



# 📘 Architecture Design Patterns

## 🔷 I. Layering & Separation of Concerns

| Pattern                     | Description                                                | Use Case                           |
| --------------------------- | ---------------------------------------------------------- | ---------------------------------- |
| Layered (N-tier)            | Divide responsibilities into layers (UI, Business, Data)   | Web apps, enterprise systems       |
| Model-View-Controller (MVC) | Separates Model, View, and Controller logic                | UI apps, web frameworks            |
| Model-View-ViewModel (MVVM) | View binds to ViewModel exposing data and commands         | Desktop/mobile apps (WPF, Android) |
| Model-View-Presenter (MVP)  | Presenter handles interaction logic between view and model | Legacy GUI frameworks              |

## 🔷 II. Distributed & Scalable Systems

| Pattern                             | Description                                          | Use Case                 |
| ----------------------------------- | ---------------------------------------------------- | ------------------------ |
| Microservices                       | Independent, loosely coupled services                | Scalable web platforms   |
| Service-Oriented Architecture (SOA) | Services interact via ESB or orchestration           | Enterprise systems, B2B  |
| Client-Server                       | Clients make requests to a central server            | Web apps, databases      |
| Peer-to-Peer (P2P)                  | Each node acts as client and server                  | Torrent, blockchain      |
| Broker                              | Middleware routes messages between components        | Message-based systems    |
| Message Bus                         | Centralized bus for service interaction via messages | Integration platforms    |
| Event-Driven                        | Components react to events asynchronously            | Real-time analytics, IoT |
| Serverless / FaaS                   | Functions triggered by events, managed by cloud      | APIs, async processing   |
| Space-Based Architecture            | Memory-centric shared data grid                      | High throughput systems  |

## 🔷 III. Data Flow & Processing

| Pattern                   | Description                                  | Use Case                                |
| ------------------------- | -------------------------------------------- | --------------------------------------- |
| Pipe and Filter           | Data flows through filters (stages)          | Compilers, ETL pipelines                |
| Batch Processing          | Scheduled large data jobs                    | Reporting, data aggregation             |
| Stream Processing         | Continuous processing of data streams        | Kafka Streams, Flink                    |
| Data-Centric / Blackboard | Shared data structure accessed by components | AI, scientific systems                  |
| Repository                | Centralized data access logic                | ORM, database logic                     |
| CQRS                      | Separate read and write models               | Event sourcing, high read/write systems |
| ETL                       | Data ingestion pattern                       | Data warehouses, pipelines              |

## 🔷 IV. Control Flow & Logic

| Pattern                 | Description                                        | Use Case                                  |
| ----------------------- | -------------------------------------------------- | ----------------------------------------- |
| Orchestration           | Central controller manages workflow                | BPM tools, workflow engines               |
| Choreography            | Services react based on events, no central control | Microservices, EDA                        |
| Rule-Based Architecture | Uses rules to drive decision-making                | Fraud detection, compliance (Drools, OPA) |
| State Machine           | Encapsulates transitions between states            | Protocols, games                          |
| Interpreter             | Defines language grammar and evaluation            | Scripting, query engines                  |
| Workflow Engine         | Declarative control of steps                       | BPMN, Airflow DAGs                        |

## 🔷 V. Modularity & Reusability

| Pattern               | Description                                     | Use Case              |
| --------------------- | ----------------------------------------------- | --------------------- |
| Component-Based       | Application built from replaceable components   | React, Angular        |
| Plugin Architecture   | Extend core functionality with external modules | IDEs, browsers        |
| Microkernel (Plug-in) | Core system with extensible plugins             | OS, compilers         |
| Hexagonal             | Core isolated via adapters                      | DDD, testable systems |
| Clean Architecture    | Layers around domain, with DI                   | Maintainable apps     |

## 🔷 VI. Security & Policy

| Pattern                     | Description                                  | Use Case              |
| --------------------------- | -------------------------------------------- | --------------------- |
| Policy Decision Point       | Separates policy evaluation from enforcement | OPA, Rego             |
| Access Control Architecture | RBAC/ABAC-based permission checks            | Enterprise systems    |
| Zero Trust Architecture     | Verifies identity on each access             | Cloud-native security |

## 🔷 VII. Reliability & Recovery

| Pattern                 | Description                             | Use Case                    |
| ----------------------- | --------------------------------------- | --------------------------- |
| Retry/Dead Letter Queue | Retry failed tasks and isolate failures | Task queues, email systems  |
| Circuit Breaker         | Prevents cascading failures             | Netflix Hystrix, resilience |
| Bulkhead                |                                         |                             |
