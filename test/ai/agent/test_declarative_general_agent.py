from ai.agent import DeclarativeGeneralAgent


if __name__ == "__main__":

    agent = DeclarativeGeneralAgent()

    result = agent(input="来週の午前中に京都の金閣寺に観光に行きたい。準備すべきタスクを提案して。")

    print(result)
