# Arquitectura de Directorios Axiomind

## Estándares de Diseño
- **Clean Architecture**: Separación estricta de responsabilidades. Dependencias apuntan hacia adentro (hacia el Dominio).
- **Modular Monolith**: Organización por dominios de negocio (Módulos) en lugar de capas técnicas globales.
- **Microservicio**: Preparado para despliegue independiente.

## Árbol de Directorios

```text
Axiomind/
├── .dockerignore          # Exclusiones de contexto Docker
├── .gitignore             # Exclusiones de Git
├── README.md              # Documentación raíz
├── requirements.txt       # Dependencias
├── config/                # Configuración transversal
│   ├── __init__.py
│   ├── settings.py        # Clases Pydantic BaseSettings
│   └── logging.py         # Configuración de logs
├── docs/                  # Documentación del proyecto
│   ├── ARCHITECTURE.md    # Decisiones de arquitectura
│   └── API.md             # Especificaciones API
├── src/
│   ├── __init__.py
│   ├── shared/            # Shared Kernel (Kernel Compartido)
│   │   ├── __init__.py
│   │   ├── domain/        # Value Objects y Entidades genéricas
│   │   └── utils/         # Utilidades puras
│   ├── modules/           # Módulos de Negocio (Boundaries)
│   │   ├── __init__.py
│   │   └── synthesizer/   # Módulo de IA
│   │       ├── __init__.py
│   │       ├── domain/            # Core: Entidades y Lógica de Negocio
│   │       │   ├── __init__.py
│   │       │   ├── entities.py
│   │       │   └── rules.py
│   │       ├── application/       # Core: Casos de Uso y Puertos
│   │       │   ├── __init__.py
│   │       │   ├── use_cases.py
│   │       │   └── ports.py       # Interfaces (Abstract repositories/services)
│   │       └── infrastructure/    # Adapters: Implementación de IA
│   │           ├── __init__.py
│   │           ├── model_adapter.py # Wrapper para ML libs
│   │           └── repository.py    # Persistencia específica del módulo
│   └── adapters/          # Adaptadores de Infraestructura Global
│       ├── __init__.py
│       ├── api/           # Adaptador Primario (FastAPI)
│       │   ├── __init__.py
│       │   ├── main.py    # Entrypoint de la App
│       │   ├── dependencies.py
│       │   └── v1/        # Versionado de API
│       │       ├── __init__.py
│       │       └── router.py
│       └── persistence/   # Adaptador Secundario (DB Global si aplica)
│           ├── __init__.py
│           └── database.py
└── tests/
    ├── __init__.py
    ├── unit/
    ├── integration/
    └── e2e/
```

## Convenciones de Nombrado
- **Directorios**: `snake_case` (e.g., `use_cases`, `neural_net`).
- **Archivos**: `snake_case` (e.g., `user_controller.py`).
- **Clases**: `PascalCase` (e.g., `AudioSynthesizer`, `UserRepository`).
- **Funciones/Variables**: `snake_case` (e.g., `calculate_metrics`, `user_id`).
- **Constantes**: `UPPER_CASE` (e.g., `MAX_RETRY_ATTEMPTS`).
- **Interfaces**: Sufijo explícito opcional (e.g., `RepositoryProtocol`). Preferimos nombres semánticos.

## Reglas de Dependencia
1. **Core (Domain/Application)** NO debe importar nada de **Adapters** o **Infrastructure**.
2. **Setup/Configuration** puede importar de todos.
3. **Modules (Synthesizer)** deben exponer una API pública clara y minimizar acoplamiento.
4. **API (FastAPI)** solo coordina la petición HTTP y llama a los Casos de Uso (Application).
