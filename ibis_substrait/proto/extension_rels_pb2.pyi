"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
from . import substrait
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class AsOfJoinRel(google.protobuf.message.Message):
    """As-Of-Join relation"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class AsOfJoinKey(google.protobuf.message.Message):
        """As-Of-Join key"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ON_FIELD_NUMBER: builtins.int
        BY_FIELD_NUMBER: builtins.int

        @property
        def on(self) -> substrait.ibis.algebra_pb2.Expression:
            """A field reference defining the on-key
            The type and units of the referenced field must be the same across all inputs
            """

        @property
        def by(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[substrait.ibis.algebra_pb2.Expression]:
            """A list of field references defining the by-key
            The types corresponding to the referenced fields must be the same across all inputs
            """

        def __init__(self, *, on: substrait.ibis.algebra_pb2.Expression | None=..., by: collections.abc.Iterable[substrait.ibis.algebra_pb2.Expression] | None=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['on', b'on']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['by', b'by', 'on', b'on']) -> None:
            ...
    KEYS_FIELD_NUMBER: builtins.int
    TOLERANCE_FIELD_NUMBER: builtins.int

    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AsOfJoinRel.AsOfJoinKey]:
        """One key per input relation, each key describing how to join the corresponding input"""
    tolerance: builtins.int
    'As-Of tolerance, in units of the on-key'

    def __init__(self, *, keys: collections.abc.Iterable[global___AsOfJoinRel.AsOfJoinKey] | None=..., tolerance: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['keys', b'keys', 'tolerance', b'tolerance']) -> None:
        ...
global___AsOfJoinRel = AsOfJoinRel

class NamedTapRel(google.protobuf.message.Message):
    """Named tap relation

    A tap is a relation having a single input relation that it passes through, while also
    causing some side-effect, e.g., writing to external storage.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KIND_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    COLUMNS_FIELD_NUMBER: builtins.int
    kind: builtins.str
    'The kind of tap'
    name: builtins.str
    'A name used to configure the tap, e.g., a URI defining the destination of writing'

    @property
    def columns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Column names for the tap's output. If specified there must be one name per field.
        If empty, field names will be automatically generated.
        """

    def __init__(self, *, kind: builtins.str=..., name: builtins.str=..., columns: collections.abc.Iterable[builtins.str] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['columns', b'columns', 'kind', b'kind', 'name', b'name']) -> None:
        ...
global___NamedTapRel = NamedTapRel