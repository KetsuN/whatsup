# What's Up?

Ping URLs and verify expected status codes.

### Overview

Send POST requests to a simple Flask application with the following data:

```
{
	"environment": "dogsonscreek",
	"branch": "doing-reports-things"
    "jira_id": "tm-9001"
}
```

The key/value pair is added to the redis DB of your choice.

### Required Variables

- REDIS_HOSTNAME - Hostname of the Redis database
- REDIS_PASSWORD - Password to the Redis database
- REDIS_PORT - Port to the Redis database
- API_KEY - API key used to interact with this application