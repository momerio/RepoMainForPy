# contributor

# コントリビュータクラス
class Contributor:
    def __init__(self, name, commit_count):
        self.name         = name
        self.commit_count = commit_count
        self.insertions   = 0 # 追加した行数
        self.deletions    = 0 # 削除した行数

    # 情報のprint結果を定義
    def __repr__(self):
        return "commit: {:>4d} 【 {:s} 】".format(self.commit_count, str(self.name))

    # -----------
    # --- set ---
    # -----------

    # nameを更新
    def set_name(self, name):
        self.name = name
    
    # commit_countを更新
    def set_commit_count(self, commit_count):
        self.commit_count = commit_count

    # insertionsを更新
    def set_insertions(self, insertions):
        self.insertions = insertions

    # deletionsを更新
    def set_insertions(self, deletions):
        self.deletions = deletions

    # -----------
    # --- get ---
    # -----------

    # nameを取得
    def get_name(self):
        return self.name

    # commit_countを取得
    def get_commit_count(self):
        return self.commit_count

    # commit_countを取得
    def get_insertions(self):
        return self.insertions

    # commit_countを取得
    def get_deletions(self):
        return self.deletions

    # -----------
    # --- add ---
    # -----------

    # commit_countにnumを足す
    def add_commit_count(self, num):
        self.commit_count += num

    # insertionsを足す
    def add_insertions(self, insertions):
        self.insertions += insertions

    # deletionsを足す
    def add_deletions(self, deletions):
        self.deletions += deletions