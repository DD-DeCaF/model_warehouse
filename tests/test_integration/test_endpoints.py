# Copyright (c) 2018, Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test expected functioning of the OpenAPI docs endpoints."""

import json


def test_models_get(client, db, model):
    """Test the /models GET API supposed to return all models in the DB."""
    db.session.commit()
    resp = client.get("/models")
    assert resp.status_code == 200


def test_models_post(client):
    """Test the /models POST API supposed to post a single model to the DB."""
    new_model = {
                  "name": "string",
                  "model_serialized": {},
                  "organism_id": 0,
                  "project_id": 0,
                  "default_biomass_reaction": "string"
                }

    resp = client.post("/models", json=new_model)
    assert resp.status_code == 200


def test_indvmodel_get(client):
    """
    Test the /models/<id> GET API supposed to get a single model by ID.

    """
    resp = client.get("/models/1")
    assert resp.status_code == 200


def test_indvmodel_put(client):
    """
    Test the /models/<id> PUT API supposed to modify a single model by ID.

    """
    updated_model = {
                      "created": "2018-08-24T13:53:42.030Z",
                      "updated": "2018-08-24T13:53:42.030Z",
                      "id": 0,
                      "name": "string",
                      "model_serialized": {},
                      "organism_id": 0,
                      "project_id": 0,
                      "default_biomass_reaction": "string"
                    }
    resp = client.put("/models/1", data=json.dumps(updated_model))
    assert resp.status_code == 200


def test_indvmodel_delete(client):
    """
    Test the /models/<id> PUT API supposed to remove a single model by ID.

    """
    resp = client.delete("/models/1")
    assert resp.status_code == 200
