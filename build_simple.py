from distutils import ccompiler
import setuptools # Needed to monkeypatch msvccompiler for Python 2.7

cc = ccompiler.new_compiler()
objects = cc.compile(["simple.c"])
cc.link(cc.EXECUTABLE, objects, 'simple.exe')
