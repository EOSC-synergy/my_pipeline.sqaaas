import functools
import logging
import uuid

from aiohttp import web

from openapi_server.controllers import db
from openapi_server.controllers.jepl import JePLUtils

from github.GithubException import GithubException
from github.GithubException import UnknownObjectException


logger = logging.getLogger('sqaaas_api.controller')


def validate_request(f):
    @functools.wraps(f)
    async def decorated_function(*args, **kwargs):
        _pipeline_id = kwargs['pipeline_id']
        try:
            uuid.UUID(_pipeline_id, version=4)
            _db = db.load_content()
            if _pipeline_id in list(_db):
                logger.debug('Pipeline <%s> found in DB' % _pipeline_id)
            else:
                logger.warning('Pipeline not found!: %s' % _pipeline_id)
                return web.Response(status=404)
        except ValueError:
            logger.warning('Invalid pipeline ID supplied!: %s' % _pipeline_id)
            return web.Response(status=400)
        try:
            logger.debug('Running decorated method <%s>' % f.__name__)
            r = await f(*args, **kwargs)
        except (UnknownObjectException, GithubException) as e:
            logger.error('(GitHub) %s (exit code: %s)' % (e.data['message'], e.status))
            return web.Response(status=e.status)
        return r
    return decorated_function


def get_jepl_files(config_json, composer_json, jenkinsfile):
    config_yml, composer_yml = JePLUtils.get_sqa_files(
        config_json,
        composer_json)
    jenkinsfile = JePLUtils.get_jenkinsfile(jenkinsfile)

    return (config_yml, composer_yml, jenkinsfile)


def push_jepl_files(gh_utils, repo, config_json, composer_json, jenkinsfile, branch='sqaaas'):
    config_yml, composer_yml, jenkinsfile = get_jepl_files(
        config_json,
        composer_json,
        jenkinsfile)
    logger.debug('Pushing file to GitHub repository <%s>: .sqa/config.yml' % repo)
    gh_utils.push_file('.sqa/config.yml', config_yml, 'Update config.yml', repo, branch=branch)
    logger.debug('Pushing file to GitHub repository <%s>: .sqa/docker-compose.yml' % repo)
    gh_utils.push_file('.sqa/docker-compose.yml', composer_yml, 'Update docker-compose.yml', repo, branch=branch)
    logger.debug('Pushing file to GitHub repository <%s>: Jenkinsfile' % repo)
    gh_utils.push_file('Jenkinsfile', jenkinsfile, 'Update Jenkinsfile', repo, branch=branch)
    logger.info('GitHub repository <%s> created with the JePL file structure' % repo)