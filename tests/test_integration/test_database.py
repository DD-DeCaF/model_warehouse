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

from model_warehouse.models import Model


def test_commit(db, model):
    """Test actually committing the models from the model fixture."""
    db.session.commit()
    ecoli_model = db.session.query(Model).filter(Model.name == "iJO1366").one()
    assert ecoli_model.name == "iJO1366"


# def test_models_get(app, db, model):
#     """Test getting models ."""
#     Model()
#     ecoli_model = db.session.query(Model).filter(Model.name == "iJO1366")
#     assert ecoli_model.name == "iJO1366"
