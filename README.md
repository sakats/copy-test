# 概要
Zennに投稿した記事で利用したDB操作プログラムを管理するリポジトリ

psycopg2でスキーマを指定してCOPYする方法
https://zenn.dev/satoshiakatsuka/articles/e0bd200a58249d

# 記事冒頭
業務中に取り組んだ不具合解決のフローを記事にしてみました。
詳細は下記のとおりです。

* PostgreSQLにCSVファイルをCOPYする際、スキーマ指定ができない不具合が発生
* 原因はライブラリの更新で、psycopg2 2.9以降ではcopy_from関数でスキーマを指定出来なくなった為
* 上記の事象に対して、スキーマ検索パスを設定して解決した
* 今回は、不具合を再現する所から始め、問題の解決フローをなるべく細かく記事にしてみます！
