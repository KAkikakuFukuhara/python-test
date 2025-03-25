import os
import tempfile

with tempfile.NamedTemporaryFile(delete=True) as t:
    print(t.name)
    with open(t.name, 'w') as f:
        f.write('書込確認\n')

    with open(t.name, 'r') as f:
        print(f.read())

    print("Close前:" , t.name, os.path.isfile(t.name))

print('Close後: ', t.name, os.path.isfile(t.name))