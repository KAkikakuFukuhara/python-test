# import に関して

packageのインポートはルートパッケージより上位のパッケージを指定することができない。

```
proj
|-lib
  |-__init__.py
  |-test.py
|-utils
  |-__init__.py
  |-myclass.py
```
のような構成の時 