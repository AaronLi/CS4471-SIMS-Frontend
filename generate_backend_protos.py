import os
import subprocess
from importlib import util as iutil

grpc_tools_id = 'grpc_tools'

input_dir = os.path.join(os.getcwd(), 'proto', 'backend_proto')
output_dir = os.path.join(os.getcwd(), 'src')

if iutil.find_spec(grpc_tools_id) is None:
    print("grpcio-tools not installed")
    if input("install? (y/n)$ ").lower() == 'y':
        subprocess.run(['pip', 'install', 'grpcio-tools'], shell=True)

if iutil.find_spec(grpc_tools_id) is None:
    print('grpcio-tools python package is required')
    quit(1)

print(f'generating grpc files from {input_dir}')
os.makedirs(output_dir, exist_ok=True)
subprocess.run(['python', '-m', 'grpc_tools.protoc', f'-Iproto', f'--python_out={output_dir}', f'--pyi_out={output_dir}', f'--grpc_python_out={output_dir}', os.path.join('proto', 'backend_proto', '*.proto')], shell=True)
print(f'generated grpc files in {output_dir}')