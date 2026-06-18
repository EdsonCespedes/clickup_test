```text
clickup-api-framework/         # Root folder of the automation project.
├── .github/                   # GitHub-specific configurations.
│   └── workflows/             # CI/CD pipeline automation scripts (GitHub Actions).
├── config/                    # Global settings and configuration management.
│   └── environments/          # Environment-specific variables (like dev or CI).
├── core/                      # The main engine, base classes, and core framework logic.
├── clients/                   # API client wrappers and connection setup.
├── domains/                   # ClickUp API business resources and endpoint logic.
│   ├── teams/                 # Endpoints, schemas, and payloads for Teams.
│   ├── spaces/                # Endpoints, schemas, and payloads for Spaces.
│   ├── folders/               # Endpoints, schemas, and payloads for Folders.
│   ├── lists/                 # Endpoints, schemas, and payloads for Lists.
│   └── tasks/                 # Endpoints, schemas, and payloads for Tasks.
├── helpers/                   # Reusable utility functions (data generators, formatters).
├── tests/                     # The actual automated test suites.
│   ├── acceptance/            # End-to-end (E2E) complete user workflows.
│   ├── functional/            # Isolated CRUD operations and individual feature tests.
│   ├── negative/              # Error handling, security, and invalid input tests.
│   ├── smoke/                 # Quick health checks for critical API endpoints.
│   ├── regression/            # Tests to ensure existing features are not broken.
│   └── unit/                  # Tests for internal framework functions and methods.
├── reports/                   # Generated test results, logs, and coverage files.
└── docs/                      # Project documentation, guides, and manuals.
```