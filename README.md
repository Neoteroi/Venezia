# Venezia, service to handle localized topics and comments

Demo project for a BlackSheep web service deployed to Azure App Service, using
a PostgreSQL database, GitHub Workflows, and ARM templates.

This is an advanced project template, featuring:

* A `Python` web service using a **PostgreSQL** database
* Example of _onion architecture_ leveraging dependency injection to organize
  the code and efficiently reduce code repetition
* **GitHub Workflows** to automate the deployment of Azure services and the
  application server
* **ARM templates** to provision the necessary Azure services
* **Database migrations** implemented using `Alembic`, automatically deployed as
  part of the Continuous Delivery workflow
* Integration with **Azure Application Insights** to collect telemetries for
  performance, web requests, exceptions, failed requests, including tracking of
  PostgreSQL dependencies
* Workflows and ARM templates prepared to support multiple environments:
  _DEV, TEST, PROD_
* A `BlackSheep` API, including `OpenAPI Documentation`
* Instructions describing how to get started and configure GitHub Workflows and
  create environments in Azure

## Requirements

* A GitHub account
* An Azure subscription
* [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

For development:

* Python 3.7 or newer

## Overview: how to use this project template

1. Create a new repository starting from this template (using GitHub features),
   or fork the project
2. Choose a project name for your new deployment
3. Configure GitHub secrets
4. Run the `infrastructure` GitHub Workflow: this creates necessary services in
   Azure, in different environments
5. Run the `server` build GitHub Workflow: this builds the application and
   deploys it to the various environments

The following pages describe in detail the steps listed above:

* [Configuring CI/CD with GitHub Actions](./docs/configuring-github-actions.md)
