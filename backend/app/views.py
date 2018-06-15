from flask import request, make_response, json

from app import app, redis_db
from app.authentication import requires_auth


@app.route("/whatsup", methods=["POST"])
@requires_auth
def update():
    data = json.loads(request.data)
    environment = data.get("environment")
    branch = data.get("branch")
    jira_id = data.get("jira_id")

    # Ensure the correct data is provided in
    if not environment or not branch:
        return app.response_class(
            response=json.dumps(
                {
                    "title": "missing parameters",
                    "message": "Both 'environment' and `branch` fields are required",
                    "status:": 400,
                }
            ),
            status=400,
            mimetype="application/json",
        )

        return make_response()

    if environment not in app.config["ACTIVE_ENVIRONMENTS"]:
        return app.response_class(
            response=json.dumps(
                {
                    "title": "invalid environment",
                    "message": "'environment' must be one of the following: {}".format(
                        ",".join(app.config["ACTIVE_ENVIRONMENTS"])
                    ),
                    "status:": 400,
                }
            ),
            status=400,
            mimetype="application/json",
        )

    redis_db.set(environment, json.dumps({"branch": branch, "jira_id": jira_id}))
    return app.response_class(
        response=json.dumps({"data": "{} marked in used by {}".format(environment, branch), "status:": 201}),
        status=201,
        mimetype="application/json",
    )


@app.route("/whatsup", methods=["GET"])
@requires_auth
def retrieve():
    key_values = {}
    for key in app.config["ACTIVE_ENVIRONMENTS"]:
        value = redis_db.get(key)
        if value:
            key_values[key] = json.loads(value)
        else:
            key_values[key] = {"environment": None, "jira_id": None}
    return app.response_class(response=json.dumps({"data": key_values}), status=200, mimetype="application/json")
