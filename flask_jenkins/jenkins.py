# coding=utf-8

import jenkins


class Jenkins:
    def __init__(self, app=None):
        self._server = None
        self.app = None

        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.app.jenkins = self

        self._load_config()

    def _load_config(self):
        host = self.app.config.get('JENKINS_HOST')
        username = self.app.config.get('JENKINS_USERNAME')
        password = self.app.config.get('JENKINS_PASSWORD')

        self._server = jenkins.Jenkins(
            'http://{}'.format(host), username=username, password=password)
