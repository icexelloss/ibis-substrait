"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
SPDX-License-Identifier: Apache-2.0"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Capabilities(google.protobuf.message.Message):
    """Defines a set of Capabilities that a system (producer or consumer) supports."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class SimpleExtension(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        URI_FIELD_NUMBER: builtins.int
        FUNCTION_KEYS_FIELD_NUMBER: builtins.int
        TYPE_KEYS_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_KEYS_FIELD_NUMBER: builtins.int
        uri: builtins.str

        @property
        def function_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            ...

        @property
        def type_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            ...

        @property
        def type_variation_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            ...

        def __init__(self, *, uri: builtins.str=..., function_keys: collections.abc.Iterable[builtins.str] | None=..., type_keys: collections.abc.Iterable[builtins.str] | None=..., type_variation_keys: collections.abc.Iterable[builtins.str] | None=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['function_keys', b'function_keys', 'type_keys', b'type_keys', 'type_variation_keys', b'type_variation_keys', 'uri', b'uri']) -> None:
            ...
    SUBSTRAIT_VERSIONS_FIELD_NUMBER: builtins.int
    ADVANCED_EXTENSION_TYPE_URLS_FIELD_NUMBER: builtins.int
    SIMPLE_EXTENSIONS_FIELD_NUMBER: builtins.int

    @property
    def substrait_versions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of Substrait versions this system supports"""

    @property
    def advanced_extension_type_urls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """list of com.google.Any message types this system supports for advanced
        extensions.
        """

    @property
    def simple_extensions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Capabilities.SimpleExtension]:
        """list of simple extensions this system supports."""

    def __init__(self, *, substrait_versions: collections.abc.Iterable[builtins.str] | None=..., advanced_extension_type_urls: collections.abc.Iterable[builtins.str] | None=..., simple_extensions: collections.abc.Iterable[global___Capabilities.SimpleExtension] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['advanced_extension_type_urls', b'advanced_extension_type_urls', 'simple_extensions', b'simple_extensions', 'substrait_versions', b'substrait_versions']) -> None:
        ...
global___Capabilities = Capabilities