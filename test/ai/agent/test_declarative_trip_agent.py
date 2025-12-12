from ai.agent import DeclarativeTripAgent


if __name__ == "__main__":

    agent = DeclarativeTripAgent()

    result = agent(input="来週の午前中に京都の金閣寺に観光に行きたい。おすすめの旅行プランを提案して。")

    print(result)
