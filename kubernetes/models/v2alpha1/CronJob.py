#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.md', which is part of this source code package.
#

import os
from kubernetes.models.unversioned.BaseModel import BaseModel
from kubernetes.models.v1.ObjectMeta import ObjectMeta
from kubernetes.models.v2alpha1.CronJobSpec import CronJobSpec
from kubernetes.models.v2alpha1.CronJobStatus import CronJobStatus
from kubernetes.utils import server_version


class CronJob(BaseModel):
    """
    http://kubernetes.io/docs/user-guide/cron-jobs/#creating-a-cron-job
    """

    def __init__(self, model=None):
        super(CronJob, self).__init__()

        if bool(os.environ.get('TRAVIS_SKIP_SERVER_VERSION', 0)):
            self.kind = 'ScheduledJob'
        else:
            v = server_version()
            if int(v['major']) == 1 and int(v['minor']) == 4:
                self.kind = 'ScheduledJob'
            if int(v['major']) == 1 and int(v['minor']) >= 5:
                self.kind = 'CronJob'

        self.api_version = "batch/v2alpha1"
        self.spec = CronJobSpec()
        self.status = CronJobStatus()

        if model is not None:
            self._build_with_model(model)

    def _build_with_model(self, model=None):
        if 'apiVersion' in model:
            self.api_version = model['apiVersion']
        if 'kind' in model:
            self.kind = model['kind']
        if 'metadata' in model:
            self.metadata = ObjectMeta(model['metadata'])
        if 'spec' in model:
            self.spec = CronJobSpec(model['spec'])
        if 'status' in model:
            self.status = CronJobStatus(model['status'])

    # ------------------------------------------------------------------------------------- spec

    @property
    def spec(self):
        return self._spec

    @spec.setter
    def spec(self, spec=None):
        if not isinstance(spec, CronJobSpec):
            raise SyntaxError('CronJob: spec: [ {} ] is invalid.'.format(spec))
        self._spec = spec

    # ------------------------------------------------------------------------------------- status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status=None):
        if not isinstance(status, CronJobStatus):
            raise SyntaxError('CronJob: status: [ {} ] is invalid.'.format(status))
        self._status = status

    # ------------------------------------------------------------------------------------- serialize

    def serialize(self):
        data = super(CronJob, self).serialize()
        if self.spec is not None:
            data['spec'] = self.spec.serialize()
        if self.status is not None:
            data['status'] = self.status.serialize()
        return data
