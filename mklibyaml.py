from distutils import ccompiler
import setuptools # Needed to monkeypatch msvccompiler for Python 2.7
import os

here = os.path.dirname(os.path.abspath(__file__))

cc = ccompiler.new_compiler()

sources = [
    'api.c',
    'dumper.c',
    'emitter.c',
    'loader.c',
    'parser.c',
    'reader.c',
    'scanner.c',
    'writer.c'
]
abs_sources = [os.path.join(here, 'yaml-0.1.5', 'src', s) for s in sources]
out = os.path.join(here, 'out')

os.mkdir(out)
os.chdir(os.path.join(here, 'yaml-0.1.5', 'src'))
cc.add_include_dir(os.path.join(here, 'yaml-0.1.5', 'include'))
cc.add_include_dir(os.path.join(here, 'yaml-0.1.5', 'win32'))
cc.define_macro('HAVE_CONFIG_H')
cc.define_macro('YAML_DECLARE_STATIC')
cc.compile(sources, output_dir=out)
os.chdir(here)

objects = [os.path.join(out, o) for o in os.listdir(out)]

cc.create_static_lib(objects, output_libname='yaml', output_dir=here)
