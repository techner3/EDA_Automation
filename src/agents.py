from crewai import Agent

class EDA_Agents:

    def data_researcher_agent(self,llm):
        return Agent(role='Senior Data Researcher',goal='Create Questions for Data Analysis which can provide valuable insights',
                        backstory="""You are a Senior Data Researcher at a leading data company.
                                     You are expert at performing Exploratory data anlaysis by asking the righ questions""",
                      allow_delegation=False,verbose=True,llm=llm)

    def data_analyst_agent(self,llm,csv_tool):
        return Agent(role='Senior Data Analyst',goal='Answer the questions asked by the data researcher by using the tool',
                     backstory="""
                            You are a software engineer that specializes in answering the questions asked by the data researcher. 
                            You are expert at providing accurate results so that we can derive as much as insights from the data""",
                        allow_delegation=False,verbose=True,llm=llm,tools=[csv_tool])

    def chief_da_agent(self,llm):
        return Agent(role='Chief Data Analyst',goal='Try to gather all the insights based on the context provided and create a report for the data analysis',
  		             backstory="""You feel that everyone always don't do a perfect job, so you are super dedicate to make high quality report.""",
		             allow_delegation=False,verbose=True,llm=llm)