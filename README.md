# python-excel
Pythonでエクセルを操作するリポジトリです。<br>
こちらはDockerで環境を構築しています。<br>

## 参考にしたサイト
https://qiita.com/jhorikawa_err/items/fb9c03c0982c29c5b6d5

# 初めに実行
```
docker-compose build
```

# Docker起動
```
docker-compose up -d
```

# コンテナ内へ（Python）
```
docker-compose exec python3 bash
```

# ライブラリのインストール(Python内でなければ)
```
python -m pip install numpy
pip install pandas
pip install xlrd
```

# コンテナ終了(先にctrl-DでPythonから抜けておきましょう)
```
docker-compose down
```