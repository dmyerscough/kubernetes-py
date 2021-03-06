#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.md', which is part of this source code package.
#

from kubernetes.K8sObject import K8sObject
from kubernetes.models.v1alpha1.PetSet import PetSet


class K8sPetSet(K8sObject):
    """
    Starting in Kubernetes version 1.5, PetSet has been refactored into StatefulSet.

    To continue to use PetSets in Kubernetes 1.5 or higher, you must migrate your existing PetSets to StatefulSets.
    See https://kubernetes.io/docs/tasks/manage-stateful-set/upgrade-pet-set-to-stateful-set/
    """

    def __init__(self, config=None, name=None):

        super(K8sPetSet, self).__init__(
            config=config,
            name=name,
            obj_type='PetSet'
        )

    # -------------------------------------------------------------------------------------  override

    def get(self):
        self.model = PetSet(self.get_model())
        return self

    def create(self):
        super(K8sPetSet, self).create()
        self.get()
        return self

    def update(self):
        super(K8sPetSet, self).update()
        self.get()
        return self
