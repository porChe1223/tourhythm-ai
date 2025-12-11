# データベーススキーマ - チャットセッション管理

## テーブル関係図

```
┌─────────────────┐       1:N       ┌─────────────────┐
│   ChatSession   │──────────────────│   ChatMessage   │
│                 │                  │                 │
│ - id (PK, UUID) │                  │ - id (PK, UUID) │
│ - created_at    │                  │ - session_id    │
│                 │                  │ - message       │
│                 │                  │ - assignee      │
│                 │                  │ - order_index   │
│                 │                  │ - score         │
│                 │                  │ - score_reason  │
│                 │                  │ - created_at    │
└─────────────────┘                  └─────────────────┘

┌─────────────────┐
│      Agent      │
│                 │
│ - id (PK, UUID) │
│ - name          │
│ - average_score │
│ - prompt        │
│ - updated_at    │
└─────────────────┘
```

## テーブル詳細

### ChatSession (`chat_sessions`)

| フィールド | 型       | キー | インデックス | NULL許可 | 説明               |
| ---------- | -------- | ---- | ------------ | -------- | ------------------ |
| id         | UUID     | PK   | Yes          | No       | UUID主キー         |
| created_at | DateTime |      |              | No       | セッション作成日時 |

### ChatMessage (`chat_messages`)

| フィールド   | 型         | キー | インデックス | NULL許可 | 説明                               |
| ------------ | ---------- | ---- | ------------ | -------- | ---------------------------------- |
| id           | UUID       | PK   | Yes          | No       | UUID主キー                         |
| session_id   | UUID       | FK   | Yes          | No       | ChatSessionへの外部キー            |
| message      | Text       |      |              | No       | メッセージ内容                     |
| assignee     | String(10) |      | Yes          | Yes      | エージェント名または人間の場合NULL |
| order_index  | Integer    |      |              | No       | セッション内のメッセージ順序       |
| score        | Integer    |      |              | Yes      | 品質スコア（AI評価）               |
| score_reason | Text       |      |              | Yes      | スコアの理由                       |
| created_at   | DateTime   |      |              | No       | メッセージ作成日時                 |

## インデックス

- `chat_messages.session_id` - セッション単位のクエリ効率化
- `chat_messages.assignee` - エージェント別フィルタリング
- `chat_messages.id` - 主キーインデックス
- `chat_sessions.id` - 主キーインデックス
- `agents.id` - 主キーインデックス
- `agents.name` - エージェント名インデックス（ユニーク）

## 主要機能

### メッセージ復元

```sql
-- 特定セッションの全メッセージを元の順番で取得
SELECT * FROM chat_messages
WHERE session_id = ?
ORDER BY order_index;
```

### エージェント分析

```sql
-- 特定エージェントの全メッセージ取得
SELECT * FROM chat_messages
WHERE assignee = 'General';

-- エージェント別平均スコア
SELECT assignee, AVG(score) as avg_score, COUNT(*) as total_messages
FROM chat_messages
WHERE assignee IS NOT NULL AND score IS NOT NULL
GROUP BY assignee;
```

### セッション管理

```sql
-- セッションと全メッセージを取得
SELECT s.*, m.*
FROM chat_sessions s
LEFT JOIN chat_messages m ON s.id = m.session_id
WHERE s.id = ?
ORDER BY m.order_index;
```

## エージェント値

- `'General'` - 汎用エージェント
- `'Trip'` - 旅行計画エージェント
- `'Schedule'` - スケジュール管理エージェント
- `'Task'` - タスク管理エージェント
- `'Supervisor'` - 監督エージェント
- `NULL` - 人間のメッセージ

### Agent (`agents`)

| フィールド    | 型         | キー   | インデックス | NULL許可 | 説明                   |
| ------------- | ---------- | ------ | ------------ | -------- | ---------------------- |
| id            | UUID       | PK     | Yes          | No       | UUID主キー             |
| name          | String(10) | UNIQUE | Yes          | No       | エージェント名（一意） |
| average_score | Float      |        |              | Yes      | メッセージの平均スコア |
| prompt        | Text       |        |              | Yes      | 最適化されたプロンプト |
| updated_at    | DateTime   |        |              | No       | 最終更新日時           |

## データフロー

1. **メッセージ格納**: AIメッセージを配列から個別レコードに分解
2. **セッション分類**: 会話コンテキストのためメッセージをセッション別に分類
3. **順序保持**: `order_index`で元のメッセージ順序を維持
4. **エージェント追跡**: 各AIメッセージでどのエージェントが生成したかを記録
5. **品質採点**: メッセージにスコアと理由を記録
6. **エージェント最適化**: Agentテーブルで各エージェントの平均スコアと最適化プロンプトを管理

# 新しいマイグレーション作成（モデル変更時）

uv run alembic revision --autogenerate -m "説明メッセージ"

# マイグレーション実行

uv run alembic upgrade head

# 現在の状態確認

uv run alembic current

# 履歴確認

uv run alembic history
