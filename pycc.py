from distutils.ccompiler import new_compiler
import setuptools
import subprocess
import sys

try:
    tool = sys.argv[1]
except IndexError:
    raise SystemExit("Usage: {} <tool>".format(sys.argv[0]))

tools = {'cc', 'linker', 'lib', 'rc', 'mc'}
if tool not in tools:
    raise SystemExit("Tool must be one of {}".format(', '.join(sorted(tools))))


cc = new_compiler()
cc.initialize()

tool = getattr(cc, tool)
if len(sys.argv) <= 2:
    print(tool)
else:
    cmd = [tool] + sys.argv[2:]
    subprocess.check_call(cmd)
