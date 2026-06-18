# ClickUp API Testing Framework

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Pytest](https://img.shields.io/badge/Pytest-Latest-green)
![Coverage](https://img.shields.io/badge/Coverage-90%25-success)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-orange)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow)

---

# Summary

This project provides a API automation testing framework for ClickUp built with Python.

The framework focuses on:

* Scalability
* Maintainability
* Reusability
* Reporting
* Parallel execution
* Continuous Integration
* Schema validation
* Structured logging

The solution follows a layered architecture that separates business logic, API communication, validations, and test implementation.

---

# Technology Stack

| Category             | Tool                   | Purpose                          |
| -------------------- | ---------------------- | -------------------------------- |
| Language             | Python 3.12+           | Main programming language        |
| Test Runner          | pytest                 | Test execution and orchestration |
| HTTP Client          | httpx                  | API communication                |
| Schema Validation    | Pydantic v2            | Data validation and modeling     |
| Logging              | structlog              | Structured logging               |
| Configuration        | pydantic-settings      | Environment management           |
| Linting & Formatting | Ruff                   | Code quality                     |
| Coverage             | pytest-cov             | Coverage reporting               |
| Soft Assertions      | pytest-check           | Multiple validations per test    |
| Reporting            | pytest-html, JUnit XML | Test reports                     |
| Parallel Execution   | pytest-xdist           | Distributed execution            |
| CI/CD                | GitHub Actions         | Automation pipelines             |

---

# Architecture

```mermaid
flowchart TD

A[Tests]
B[Endpoints Layer]
C[Client Layer]
D[Request Manager]
E[HTTPX]
F[ClickUp API]

A --> B
B --> C
C --> D
D --> E
E --> F
```

---

# Design Principles

| Principle              | Description                               |
| ---------------------- | ----------------------------------------- |
| Separation of Concerns | Each layer has a single responsibility    |
| Reusability            | Shared components across tests            |
| Scalability            | Easy onboarding of new resources          |
| Maintainability        | Centralized configuration and validations |
| Observability          | Structured logging and reporting          |
| Performance            | Parallel execution support                |

---

# Project Structure

```text
clickup-api-framework/

├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── continuous-testing.yml
│
├── config/
│   ├── settings.py
│   ├── environments/
│   │   ├── dev.env
│   │   └── ci.env
│   └── constants.py
│
├── core/
│   ├── request_manager.py
│   ├── singleton.py
│   ├── logger.py
│   ├── schema_validator.py
│   ├── assertions.py
│   └── exceptions.py
│
├── clients/
│   └── clickup_client.py
│
├── domains/
│   ├── teams/
│   ├── spaces/
│   ├── folders/
│   ├── lists/
│   └── tasks/
│
├── helpers/
│   ├── data_builder.py
│   ├── random_generator.py
│   └── date_helper.py
│
├── tests/
│   ├── acceptance/
│   ├── functional/
│   ├── negative/
│   ├── smoke/
│   ├── regression/
│   └── unit/
│
├── reports/
├── docs/
│
├── conftest.py
├── pytest.ini
├── pyproject.toml
├── README.md
├── .env
├── .gitignore
└── requirements.txt
```

---

# ClickUp Resources

## Priority 1 Resources

| Resource | Description       |
| -------- | ----------------- |
| Teams    | Team management   |
| Spaces   | Workspace spaces  |
| Folders  | Folder management |
| Lists    | List management   |
| Tasks    | Task management   |

---

# CRUD Coverage Strategy

| Resource | Create | Read | Update | Delete |
| -------- | ------ | ---- | ------ | ------ |
|          | ✅     |      |       |         |
|          |        |     |       |      |
|          |        |     |       |         |
|          |        |     |       |   |
|          |        |     |       |       |

---

# Mandatory Assertions

Every automated test must validate the following:

| Validation        | Example                                   |
| ----------------- | ----------------------------------------- |
| Status Code       |  |
| Response Body     |          |
| Schema Validation |         |
| Data Integrity    |        |

---

# Request Manager

The framework uses a Singleton-based Request Manager.

## Responsibilities

| Responsibility     | Description                       |
| ------------------ | --------------------------------- |
| Connection Reuse   | Reuse HTTP connections            |
| Authentication     | Manage authorization headers      |
| Timeouts           | Centralized timeout configuration |
| Session Management | Single HTTPX instance             |
| Global Headers     | Shared request headers            |

### Rule

> No test should call HTTPX directly.
> All requests must pass through the Request Manager.

---

# Logging Strategy

Using **structlog**.

## Logged Events

| Event             |
| ----------------- |
| Test Started      |
| Request Sent      |
| Payload Sent      |
| Response Received |
| Validation Error  |
| Execution Time    |
| Final Result      |

---

# Fixtures

Global fixtures defined in ``.

| Fixture              | Purpose            |
| -------------------- | ------------------ |
|  |  |
|       |  |
|                |    |
|             |   |
|     |    |

---

# Test Lifecycle Hooks

## Before Session

* Initialize Logger
* Initialize Request Manager
* Load Configuration

## After Session

* Close HTTP Client
* Generate Reports

## Before Test

* Prepare Test Data

## After Test

* Cleanup Created Resources

---

# Test Categories

| Category   | Purpose                        |
| ---------- | ------------------------------ |
| Smoke      | Verify service availability    |
| Functional | Validate expected behavior     |
| Negative   | Validate error handling        |
| Acceptance | Validate end-to-end workflows  |
| Regression | Protect critical functionality |

---

# Test Markers

```python
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.negative
@pytest.mark.acceptance
@pytest.mark.regression
```

---

# Coverage Strategy

## Unit Test Coverage

| Component        |
| ---------------- |
| Request Manager  |
| Logger           |
| Schema Validator |
| Helpers          |
| Configuration    |


---

# Soft Assertions

Using **pytest-check**.

## Benefits

| Benefit                               |
| ------------------------------------- |
| Multiple validations in one execution |
| Better error visibility               |
| Richer reporting                      |
| Better debugging experience           |

---



---

# Naming Conventions

## Test Files

```text
test_create_space.py
test_update_task.py
test_delete_folder.py
```

## Schema Files

```text
space_schema.py
task_schema.py
```

## Endpoint Files

```text
space_endpoints.py
task_endpoints.py
```

## Payload Files

```text
space_payloads.py
task_payloads.py
```

---