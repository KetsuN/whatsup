# What's Up?

Keep track of testing environments through a simple flask app powered by a redis store.

### Overview

#### Update an environment
Send POST requests to `/whatsup` with the following data:

```
{
    "environment": "testing-env-1",
    "branch": "doing-reports-things",
    "jira_id": "tm-9001"
}
```

The key/value pair is added to the redis DB of your choice.

#### Retrieve all environment states
Send GET requests to `/whatsup` with the following data:

```
{
    "data": {
        "testing-env-1": {
            "branch": "doing-reports-things",
            "jira_id": "tm-9001"
        },
        ...
    }
}
```

The keys are the environment names on record and the values contain the branch and jira ticket IDs for the
environment.

### Required Variables

- REDIS_URL - Fully qualified redis URL
- API_KEY - API key used to interact with this application