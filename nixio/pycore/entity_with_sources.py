# Copyright (c) 2016, German Neuroinformatics Node (G-Node)
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted under the terms of the BSD License. See
# LICENSE file in the root of the Project.

from .entity_with_metadata import EntityWithMetadata
from .source import Source
from .util import util


class EntityWithSources(EntityWithMetadata):

    def __init__(self, h5obj):
        super(EntityWithSources, self).__init__(h5obj)

    @classmethod
    def _create_new(cls, parent, name, type_):
        newentity = super(EntityWithSources, cls)._create_new(parent,
                                                              name, type_)
        newentity._h5obj.create_group("sources")
        return newentity

    # Source
    def _get_source_by_id(self, id_or_name):
        return Source(util.id_or_name_getter(self._h5obj["sources"], id_or_name))

    def _get_source_by_pos(self, pos):
        return Source(util.pos_getter(self._h5obj["sources"], pos))

    def _delete_source_by_id(self, id_or_name):
        util.deleter(self._h5obj["sources"], id_or_name)

    def _source_count(self):
        return len(self._h5obj["sources"])


util.create_link_methods(EntityWithSources, Source, "source")
EntityWithSources._remove_source_by_id = EntityWithSources._delete_source_by_id
