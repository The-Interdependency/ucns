"""Compatibility wrapper for :mod:`ucns.object_record`.

The implementation moved to ``ucns.object_record``; this module remains so legacy
``ucns_recursive`` imports continue to work during the deprecation window.
"""

from importlib import import_module as _import_module

_module = _import_module("ucns.object_record")

for _name, _value in vars(_module).items():
    if _name not in {"__builtins__", "__cached__", "__doc__", "__file__", "__loader__", "__name__", "__package__", "__spec__"}:
        globals()[_name] = _value

__all__ = [
    _name for _name in globals()
    if _name not in {"__builtins__", "__cached__", "__doc__", "__file__", "__loader__", "__name__", "__package__", "__spec__", "_import_module", "_module"}
]
