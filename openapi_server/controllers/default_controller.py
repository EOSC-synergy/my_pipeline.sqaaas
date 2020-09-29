import shelve
import uuid

from typing import List, Dict
from aiohttp import web

from openapi_server.models.pipeline import Pipeline
from openapi_server import util


def load_db_content():
    return shelve.open('sqaaas')


def store_db_content(d):
    with shelve.open('db.shelve') as db:
        db = d
        print('### Pipeline DB ##')
        for k in db.keys():
            print(k, db[k])
        print('##################')


async def add_pipeline(request: web.Request, body) -> web.Response:
    """Creates a pipeline.

    Provides a ready-to-use Jenkins pipeline based on the v2 series of jenkins-pipeline-library. 

    :param body: 
    :type body: dict | bytes

    """
    pipeline_id = str(uuid.uuid4())
    body = Pipeline.from_dict(body)
    d = {'id': body.pipeline_id, 'sqa_criteria': body.sqa_criteria}
    db = load_db_content()
    db[pipeline_id] = d
    store_db_content(db)

    return web.Response(status=200)


async def get_pipeline_by_id(request: web.Request, pipeline_id) -> web.Response:
    """Find pipeline by ID

    

    :param pipeline_id: ID of the pipeline to get
    :type pipeline_id: int

    """
    return web.Response(status=200)