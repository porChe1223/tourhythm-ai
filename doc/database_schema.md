# データベーススキーマ - チャットセッション管理

## テーブル関係図

```
┌─────────────────┐       1:N        ┌─────────────────┐
│   ChatSession   │──────────────────│   ChatMessage   │
│                 │                  │                 │
│ - id (PK, UUID) │                  │ - id (PK, UUID) │
│ - created_at    │                  │ - session_id    │
│                 │                  │ - message       │
│                 │                  │ - assignee      │
│                 │                  │ - order_index   │
│                 │                  │ - score         │
│                 │                  │ - created_at    │
└─────────────────┘                  └─────────────────┘

┌─────────────────┐       1:N        ┌─────────────────┐
│      Agent      │──────────────────│     Prompt      │
│                 │                  │                 │
│ - id (PK, UUID) │                  │ - id (PK, INT)  │
│ - name (UNIQUE) │                  │ - agent_name    │
│ - average_score │                  │ - prompt        │
│ - prompt        │                  │ - created_at    │
│ - updated_at    │                  │                 │
└─────────────────┘                  └─────────────────┘
```

## テーブル詳細

### ChatSession (`chat_sessions`)

| フィールド | 型       | キー | インデックス | NULL許可 | 説明               |
| ---------- | -------- | ---- | ------------ | -------- | ------------------ |
| id         | UUID     | PK   | Yes          | No       | UUID主キー         |
| created_at | DateTime |      |              | No       | セッション作成日時 |

### ChatMessage (`chat_messages`)

| フィールド  | 型         | キー | インデックス | NULL許可 | 説明                               |
| ----------- | ---------- | ---- | ------------ | -------- | ---------------------------------- |
| id          | UUID       | PK   | Yes          | No       | UUID主キー                         |
| session_id  | UUID       | FK   | Yes          | No       | ChatSessionへの外部キー            |
| message     | Text       |      |              | No       | メッセージ内容                     |
| assignee    | String(10) |      | Yes          | Yes      | エージェント名または人間の場合NULL |
| order_index | Integer    |      |              | No       | セッション内のメッセージ順序       |
| score       | Integer    |      |              | Yes      | 品質スコア（AI評価）               |
| created_at  | DateTime   |      |              | No       | メッセージ作成日時                 |

### Agent (`agents`)

| フィールド    | 型         | キー   | インデックス | NULL許可 | 説明                                |
| ------------- | ---------- | ------ | ------------ | -------- | ----------------------------------- |
| id            | UUID       | PK     | Yes          | No       | UUID主キー                          |
| name          | String(10) | UNIQUE | Yes          | No       | エージェント名（一意）              |
| average_score | Float      |        |              | Yes      | メッセージの平均スコア              |
| prompt        | Text       |        |              | Yes      | 最新の最適化されたプロンプト        |
| updated_at    | DateTime   |        |              | No       | 最終更新日時（MIPROv2最適化時更新） |

**用途**: MIPROv2最適化結果の保存、エージェント統計管理

### Prompt (`prompts`)

| フィールド | 型         | キー | インデックス | NULL許可 | 説明               |
| ---------- | ---------- | ---- | ------------ | -------- | ------------------ |
| id         | Integer    | PK   | Yes          | No       | 連番主キー         |
| agent_name | String(10) | FK   | Yes          | No       | Agentへの外部キー  |
| prompt     | Text       |      |              | No       | プロンプトテキスト |
| created_at | DateTime   |      |              | No       | プロンプト作成日時 |

**用途**: プロンプト変更履歴の完全保持、ロールバック、A/Bテスト

## インデックス

- `chat_messages.session_id` - セッション単位のクエリ効率化
- `chat_messages.assignee` - エージェント別フィルタリング（MIPROv2で使用）
- `chat_messages.id` - 主キーインデックス
- `chat_sessions.id` - 主キーインデックス
- `agents.id` - 主キーインデックス
- `agents.name` - エージェント名インデックス（ユニーク）
- `prompts.agent_name` - エージェント別プロンプト履歴取得

## マイグレーション管理

### 新しいマイグレーション作成（モデル変更時）

```bash
uv run alembic revision --autogenerate -m "説明メッセージ"
```

### マイグレーション実行

```bash
# 最新バージョンに更新
uv run alembic upgrade head

# 1つ前に戻す
uv run alembic downgrade -1

# 特定リビジョンに移行
uv run alembic upgrade <revision_id>
```

### マイグレーション状態確認

```bash
# 現在の状態確認
uv run alembic current

# 履歴確認
uv run alembic history

# 詳細表示
uv run alembic history --verbose
```
