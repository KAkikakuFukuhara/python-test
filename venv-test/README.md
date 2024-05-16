# README

ここでは python の仮想環境である 'venv'に関して説明を行う。  

## venv とは

　venv は python においてライブラリがインストールされている環境を隔離するためのものである。この隔離された環境をしばしば仮想環境と呼ぶ。なお仮想環境は広い意味を持つのでこのvenvで作成した環境のみを指すわけではないことに注意するべし。  
　さて、通常のpython環境を用いている場合、ライブラリはその環境にインストールされ使い分けることができない。一方でvenvを用いることでプロジェクト単位でライブラリの使い分けができるようになる（その分ストレージ容量を食うが）  

## インストール

venv は pyenv と一緒に使うことが多いので、pyenvを使っていれば追加でインストールする必要はない。  
pyenvを使っていない場合は以下のようにしてインストールする。
```bash
$ apt update
$ apt install python3-venv
```

## 使い方

以下のようにして仮想環境を作成して仮想環境に移動する。  
```bash
$ cd test-project

# 仮想環境名は何でも良いが慣例として .venv とすることになっている。
$ python -m venv .venv

# 仮想環境に移動
# プロンプトを示す '$' の前に 仮想環境名が表示される
$ source .venv/bin/activate
(.venv)$

# 仮想環境から抜けたい時は deactivate を実行する
(.venv)$ deactivate
$

# pip と setuptools を最新にしといた方がよいのでする。
$ source .venv/bin/activate
(.venv)$ pip install -U pip setuptools

# 後は通常どおり pip install 等を行えばよい。
(.venv)$ pip install tqdm
# ライブラリのインストールは以下の場所にされている
(.venv)$ ls .venv/lib/python3.x/site-packages/
...
tqdm
...
```

このようにして ライブラリの環境を隔離することでクリーンなpython 環境を維持する。  
また pyenv + venv で活用されることが多く python のバージョン管理は pyenv ライブラリのバージョン管理は venv を使用することが現在のオススメ環境となっている。  
このようなモノは Anaconda が有名であるが、小規模もしくは非営利以外では有料となるため使用していない。  
