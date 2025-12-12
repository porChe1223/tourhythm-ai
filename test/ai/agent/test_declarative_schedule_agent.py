from ai.agent import DeclarativeScheduleAgent


if __name__ == "__main__":

    agent = DeclarativeScheduleAgent()

    result = agent(input="来週の午前中に京都の金閣寺に観光に行きたい。詳細なスケジュールを提案して。")

    print(result)
