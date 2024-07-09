import os
import agentops
import pandas as pd
import streamlit as st
from crewai import Crew
from dotenv import load_dotenv
from src.tasks import EDA_Tasks
from src.agents import EDA_Agents
from langchain_groq import ChatGroq
from langchain.tools import StructuredTool
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

load_dotenv()

agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"))

def csv_agent(agent,query):
    return agent.invoke(query)["output"]


def main():
    
    st.title("Automated EDA")
    st.divider()

    data_description = st.text_area("Enter Data Description")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])


    if st.button("Submit"):

        llm = ChatGroq(temperature=0,model="Llama3-70b-8192",api_key=os.getenv("GROQ_API_KEY"))
        df = pd.read_csv(uploaded_file)
        agent=create_pandas_dataframe_agent(llm, df, verbose=False)
        csv_tool = StructuredTool.from_function(func=lambda input: csv_agent(agent,input),name='Data Agent',
                                              description='This function will help you to answer any questions related to the data with input passed to it')

        agents=EDA_Agents()
        tasks=EDA_Tasks()

        data_researcher=agents.data_researcher_agent(llm)
        data_analyst=agents.data_analyst_agent(llm,csv_tool)
        chief_da=agents.chief_da_agent(llm)

        ques_task=tasks.ques_task(data_researcher)
        ans_task=tasks.ans_task(data_analyst)
        summarize_task=tasks.summarize_task(chief_da)

        crew = Crew(agents=[data_researcher,data_analyst,chief_da],
                    tasks=[ques_task,ans_task,summarize_task],verbose=True)

        response = crew.kickoff(inputs=({"context": data_description}))

        st.write(response)
        agentops.end_session("Success")

if __name__ == "__main__":
    main()