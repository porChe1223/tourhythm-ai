import asyncio
from ai.agent import DeclarativeEvaluationAgent


async def main():
    agent = DeclarativeEvaluationAgent()

    trip_response = """京都観光スポット

1. 金閣寺（鹿苑寺）【歴史】
   - 金箔に覆われた三層の舎利殿
   - 鏡湖池に映る絶景
   - 世界遺産に登録

2. 嵐山・竹林の小径【自然】
   - 青竹が立ち並ぶ幻想的な散策路
   - 渡月橋からの桂川の景色
   - トロッコ列車でのアクセスも可

3. 伏見稲荷大社【歴史】
   - 約1万本の朱色の鳥居が連なる千本鳥居
   - 稲荷山山頂まで約2時間のハイキング
   - 夜間ライトアップも開催

4. 清水寺【歴史】
   - 高さ13mの清水の舞台からの眺望
   - 音羽の滝での祈願
   - 三年坂・二年坂の町並み散策

5. 祇園【グルメ・文化】
   - 石畳の花見小路通
   - 舞妓・芸妓との遭遇チャンス
   - 京料理・湯豆腐などのグルメ

6. 二条城【歴史】
   - 徳川家康が築いた世界遺産
   - ウグイス張りの廊下
   - 二の丸御殿の障壁画"""

    task_response = """京都・金閣寺旅行の準備リスト

【持ち物リスト】
- パスポート・身分証
- 財布・現金（拝観料：金閣寺500円、清水寺400円）
- ICカード（バス・電車用）
- スマートフォン・充電器
- カメラ
- 歩きやすいスニーカー
- 折り畳み傘・雨具
- 日焼け止め・帽子（夏季）
- ハンカチ・ティッシュ

【ToDoリスト】
- 宿泊先の予約確認
- 京都市バス一日券の購入検討
- 金閣寺の開門時間確認（9:00〜17:00）
- 混雑を避けるため早朝到着を計画
- 周辺観光スポット（龍安寺・仁和寺）のルート確認
- 昼食・夕食の候補店をリストアップ
- 帰りの交通手段・時刻表の確認"""

    print("=== Trip Agent Response Evaluation ===")
    trip_score = agent(input=trip_response)
    print(f"Score: {trip_score}")

    print("\n=== Task Agent Response Evaluation ===")
    task_score = agent(input=task_response)
    print(f"Score: {task_score}")


if __name__ == "__main__":
    asyncio.run(main())
