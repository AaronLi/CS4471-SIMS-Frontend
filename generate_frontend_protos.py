import os
import sys
import subprocess
from importlib import util as iutil

grpc_tools_id = 'grpc_tools'

# sys.path.append(os.path.dirname(__file__))
# print(sys.path)

input_dir = os.path.join(os.path.dirname(__file__), 'proto', 'frontend_proto')
output_dir = os.path.join(os.path.dirname(__file__), 'src')

if iutil.find_spec(grpc_tools_id) is None:
    print("grpcio-tools not installed")
    if input("install? (y/n)$ ").lower() == 'y':
        subprocess.run(['pip', 'install', 'grpcio-tools'], shell=True)

if iutil.find_spec(grpc_tools_id) is None:
    print('grpcio-tools python package is required')
    quit(1)

print(f'generating grpc files from {input_dir}')
os.makedirs(output_dir, exist_ok=True)
subprocess.run(['python3', '-m', 'grpc_tools.protoc', f'-Iproto', f'--python_out={output_dir}', f'--pyi_out={output_dir}', f'--grpc_python_out={output_dir}', os.path.join(os.path.dirname(__file__),'proto', 'frontend_proto', '*.proto')], shell=False)
print(f'generated grpc files in {output_dir}')