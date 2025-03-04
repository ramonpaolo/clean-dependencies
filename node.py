import os
import subprocess

print(f'By default, only is deleted the \'node_modules\' inside {os.getenv('HOME')}! If you want to specify a specific path, type it now! ')

basePathToNodeModules = input(f'Base Path to search and delete node_modules! Default is {os.getenv('HOME')}.  ')

if basePathToNodeModules == "":
  basePathToNodeModules = os.getenv('HOME')

def format_size(data_kb):
    if data_kb < 1024:
        return f"{data_kb:,.0f} KB".replace(",", ".")
    elif data_kb < 1024 * 1024:
        total_mb = data_kb / 1024
        return f"{total_mb:,.2f} MB".replace(",", ".")
    else:
        total_gb = data_kb / (1024 * 1024)
        return f"{total_gb:,.2f} GB".replace(",", ".")

print(f"Searching for node_modules to delete on the \"{basePathToNodeModules}\" and sub folders")

proc = subprocess.run(['find', basePathToNodeModules, '-type', 'd', '-name', 'node_modules', '-print'], capture_output=True)

stdoutString = proc.stdout.__str__()

quantityPathsFound = stdoutString.split('\\n')

QUANTITY_NODE_MODULES_TO_DELETE = 0
SIZE_DIRECTORIES_TO_DELETE_IN_KB = 0
PATHS_TO_DELETE = []

print('Node modules to delete: ')

for nodeModules in quantityPathsFound:
  isNodeMobulesOfLib = nodeModules.count('node_modules')

  if isNodeMobulesOfLib >= 2:
    continue
  elif nodeModules.__contains__('/node_modules'):
    proc = subprocess.run(['du', '-k', nodeModules], capture_output=True)
    stdoutString = proc.stdout.__str__()

    isNodeModuleEmpty = stdoutString.split('\\n').__len__() == 1
    sizeOfDirectoryInKb = 0

    if isNodeModuleEmpty:
      continue
    else:
      sizeOfDirectoryInKb = int(stdoutString.split('\\n')[-2].split('\\t')[0].replace('b\'', ''))

    sizeOfDirectory = format_size(sizeOfDirectoryInKb)

    print(f'The path "{nodeModules}" occupe {sizeOfDirectory}')

    SIZE_DIRECTORIES_TO_DELETE_IN_KB += sizeOfDirectoryInKb
    QUANTITY_NODE_MODULES_TO_DELETE += 1
    PATHS_TO_DELETE.append(nodeModules)


confirmDelete = input(f'\nConfirm deletion of {QUANTITY_NODE_MODULES_TO_DELETE} node_modules listed above? The total size of node_modules is {format_size(SIZE_DIRECTORIES_TO_DELETE_IN_KB)}!    ').lower() == 'yes'

if confirmDelete:
  for path_to_delete in PATHS_TO_DELETE:
    os.system(f'rm -rf {path_to_delete}')
  print('Deleted with success!')