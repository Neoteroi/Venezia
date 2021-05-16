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

## Disclaimer
The instructions provided here illustrate the concepts using `Bash` scripts.
The following instructions describe how to create a DEV environment in Azure:
the same concepts apply to any kind of environment.

### Choosing a project name

The default project name for this demo is `Venezia`, to honour the Italian city.
To create a new deployment of this service, it is necessary to choose a
different name.

Since Azure provides default domains for the services, the project name must be
globally unique. Note that the project name is concatenated to the environment
name, so for example a project name `example` will result in the creation of an
app service at the URL: `https://dev-example.azurewebsites.net`, if this name
is available.

The name should be set in `./infrastructure/template.json`, editing the
parameter named `projectName` under `parameters`.

```json
    "projectName": {
      "type": "string",
      "minLength": 2,
      "defaultValue": "venezia"
    },
```

### Configuring GitHub Secrets

Before starting the first deployment, it is necessary to configure secrets in
GitHub, in detail:

* deployment credentials that are used by GitHub Actions to interact with the
  resource group in your subscription
* a database admin password

This guide illustrates how to use repository's secrets, which are avaiable also
for free private repositories. Another option would be to configure [GitHub
environments](https://docs.github.com/en/actions/reference/environments), but
this approach is not described here (the core concepts don't vary).

### List of secrets used by GitHub Workflows, for one environment

The following table lists the secrets that are required for a single `DEV`
environment:

| Secret name            | Description                                                                 |
| ---------------------- | --------------------------------------------------------------------------- |
| DEV_AZURE_SUBSCRIPTION | Azure subscription ID for the DEV environment.                              |
| DEV_AZURE_CREDENTIALS  | Deployment credentials scoped for the DEV resource group.                   |
| DEV_DB_MIGCONNSTRING   | Connection string used for database migrations.                             |
| DEV_DBSA_PASSWORD      | DBA password used to create services in Azure (used in the ARM deployment). |

#### Generating deployment credentials

Follow the instructions described here to generate deployment credentials and
configure them in GitHub secrets:
* [Deploy ARM templates by using GitHub Actions](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-github-actions)

**In summary:**

To generate deployment credentials, use the Azure CLI after signing-in to your
Azure account and selecting the desired subscription.

If the chosen project name is `example`, it is recommended to use a resource
group name such as `dev-example-rg` for the DEV environment.

```bash
# login
az login

# select the desired subscription
az account set --subscription "NAME"

SUBSCRIPTION_ID="your-subscription-id"

# generate deployment credentials
az ad sp create-for-rbac \
   --name "example-dev-agent" \
   --role contributor \
   --scopes /subscriptions/$SUBSCRIPTION_ID/resourceGroups/dev-example-rg \
   --sdk-auth
```

The output of the command looks like the following:

```bash
{
  "clientId": "*******************************",
  "clientSecret": "*******************************",
  "subscriptionId": "*******************************",
  "tenantId": "*******************************",
  "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
  "resourceManagerEndpointUrl": "https://management.azure.com/",
  "activeDirectoryGraphResourceId": "https://graph.windows.net/",
  "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
  "galleryEndpointUrl": "https://gallery.azure.com/",
  "managementEndpointUrl": "https://management.core.windows.net/"
}
```

The whole JSON fragment must be copied and configured as GitHub secret, to
enable automated deployments in GitHub Workflows.

Note that since the credentials are scoped on the subscription, it is necessary
to define a secret for each environment. For the DEV environment, create a
secret such as:

* _DEV_AZURE_CREDENTIALS_ --> the name must match what is used in `.github/workflows/infrastructure.yml`

#### Define a database password

Choose, or generate, a database password for the DEV environment.

**Tip:** use Python to generate passwords, instead of make them up.
The following script can be used to generate passwords of 60 characters:

``` python
import string
import secrets


def generate_temp_password(length):
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for i in range(length))


if __name__ == "__main__":
    print(generate_temp_password(60))
```

Example:

```bash
$ python3 genpass.py
SIqtKXqB8Pu61fuobHHBD1USt1m7dRXYR43EUJQvsX7oa79c4G4OSeuo4FPa
```

The database password configured in GitHub secrets will be used in
two ways:

* to configure the DB password when deploying the services in Azure
* to run database migrations

> Note: a possible improvement is to configure different credentials:
> the dba to run migrations, and credentials with lower privileges for
> the application server.

During development, it is convenient to have access to the database password of
the DEVELOPMENT environment, to work on the database structure using migrations
(described later).

---

#### Configure database secrets

```
postgres+psycopg2://pgsqladmin@dev-examplepg:DATABASE_PASSWORD_HERE@dev-examplepg.postgres.database.azure.com:5432/example
```
